"""Flask dashboard for the Raspberry Pi side of the smart greenhouse."""

from __future__ import annotations

import atexit
import os
import threading
from dataclasses import dataclass, field
from pathlib import Path
from typing import Any

from flask import Flask, render_template

from db import (
    count_readings,
    fetch_latest_reading,
    fetch_recent_readings,
    initialize_database,
    insert_reading,
)
from serial_reader import SerialReader, SerialStatus, start_serial_reader, utc_now_iso


@dataclass(slots=True)
class Settings:
    host: str = "0.0.0.0"
    port: int = 5000
    database_path: Path = Path("data/greenhouse.sqlite3")
    serial_port: str | None = "/dev/ttyACM0"
    serial_baudrate: int = 115200
    serial_timeout: float = 1.0
    serial_enabled: bool = True
    history_limit: int = 12
    start_reader: bool = True


@dataclass(slots=True)
class RuntimeState:
    started_at: str = field(default_factory=utc_now_iso)
    status: SerialStatus = field(
        default_factory=lambda: SerialStatus(
            state="idle",
            message="serial reader has not started yet",
            updated_at=utc_now_iso(),
        )
    )
    last_reading: dict[str, Any] | None = None
    last_error: str | None = None
    inserted_rows: int = 0
    lock: threading.Lock = field(default_factory=threading.Lock, repr=False)

    def update_status(self, status: SerialStatus) -> None:
        with self.lock:
            self.status = status
            if status.state == "error":
                self.last_error = status.message

    def record_reading(self, db_path: Path, reading: dict[str, Any]) -> None:
        insert_reading(db_path, reading)
        with self.lock:
            self.last_reading = reading
            self.inserted_rows += 1
            self.last_error = None

    def snapshot(self) -> dict[str, Any]:
        with self.lock:
            return {
                "started_at": self.started_at,
                "status": self.status,
                "last_reading": self.last_reading,
                "last_error": self.last_error,
                "inserted_rows": self.inserted_rows,
            }


def parse_bool(value: str | None, default: bool = True) -> bool:
    if value is None:
        return default
    return value.strip().lower() not in {"0", "false", "no", "off"}


def load_settings() -> Settings:
    return Settings(
        host=os.getenv("APP_HOST", "0.0.0.0"),
        port=int(os.getenv("APP_PORT", "5000")),
        database_path=Path(os.getenv("DATABASE_PATH", "data/greenhouse.sqlite3")),
        serial_port=os.getenv("SERIAL_PORT", "/dev/ttyACM0") or None,
        serial_baudrate=int(os.getenv("SERIAL_BAUDRATE", "115200")),
        serial_timeout=float(os.getenv("SERIAL_TIMEOUT", "1.0")),
        serial_enabled=parse_bool(os.getenv("SERIAL_ENABLED"), True),
        history_limit=int(os.getenv("HISTORY_LIMIT", "12")),
        start_reader=parse_bool(os.getenv("START_SERIAL_READER"), True),
    )


def build_dashboard_context(settings: Settings, state: RuntimeState) -> dict[str, Any]:
    latest = fetch_latest_reading(settings.database_path)
    history = fetch_recent_readings(settings.database_path, limit=settings.history_limit)
    snapshot = state.snapshot()
    return {
        "settings": settings,
        "latest": latest,
        "history": history,
        "runtime": snapshot,
        "total_rows": count_readings(settings.database_path),
    }


def create_serial_status_message(settings: Settings) -> SerialStatus:
    if not settings.serial_enabled:
        return SerialStatus(
            state="disabled",
            message="serial reader disabled by configuration",
            updated_at=utc_now_iso(),
        )
    if not settings.serial_port:
        return SerialStatus(
            state="disabled",
            message="no serial port configured",
            updated_at=utc_now_iso(),
        )
    return SerialStatus(
        state="starting",
        message=f"waiting for Arduino on {settings.serial_port}",
        port=settings.serial_port,
        baudrate=settings.serial_baudrate,
        updated_at=utc_now_iso(),
    )


def create_app(settings: Settings | None = None) -> Flask:
    settings = settings or load_settings()
    initialize_database(settings.database_path)

    app = Flask(__name__)
    state = RuntimeState(status=create_serial_status_message(settings))
    app.config["GREENHOUSE_SETTINGS"] = settings
    app.config["GREENHOUSE_STATE"] = state
    app.config["GREENHOUSE_READER"] = None

    def on_status(status: SerialStatus) -> None:
        state.update_status(status)

    def on_reading(reading: dict[str, Any]) -> None:
        try:
            state.record_reading(settings.database_path, reading)
        except Exception as exc:  # noqa: BLE001 - dashboard should keep running
            state.update_status(
                SerialStatus(
                    state="error",
                    message=f"database write failed: {exc}",
                    port=settings.serial_port,
                    baudrate=settings.serial_baudrate,
                    updated_at=utc_now_iso(),
                )
            )

    def start_reader() -> SerialReader | None:
        if not settings.start_reader:
            state.update_status(
                SerialStatus(
                    state="disabled",
                    message="serial reader start skipped by configuration",
                    port=settings.serial_port,
                    baudrate=settings.serial_baudrate,
                    updated_at=utc_now_iso(),
                )
            )
            return None
        if not settings.serial_enabled or not settings.serial_port:
            state.update_status(create_serial_status_message(settings))
            return None
        reader = start_serial_reader(
            port=settings.serial_port,
            baudrate=settings.serial_baudrate,
            timeout=settings.serial_timeout,
            on_reading=on_reading,
            on_status=on_status,
        )
        app.config["GREENHOUSE_READER"] = reader
        return reader

    reader = start_reader()

    @atexit.register
    def _shutdown_reader() -> None:
        running = app.config.get("GREENHOUSE_READER")
        if isinstance(running, SerialReader):
            running.stop()

    @app.route("/")
    def index() -> str:
        context = build_dashboard_context(settings, state)
        return render_template("index.html", **context)

    @app.route("/healthz")
    def healthz() -> tuple[str, int]:
        return "ok", 200

    app.config["GREENHOUSE_START_TIME"] = state.started_at
    app.config["GREENHOUSE_READER"] = reader
    return app


def main() -> None:
    settings = load_settings()
    app = create_app(settings)
    app.run(host=settings.host, port=settings.port, debug=False, use_reloader=False, threaded=True)


if __name__ == "__main__":
    main()
