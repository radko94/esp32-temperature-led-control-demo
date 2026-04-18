"""USB serial reader and payload validation for the greenhouse edge node."""

from __future__ import annotations

import json
import threading
from dataclasses import dataclass
from datetime import datetime, timezone
from typing import Any, Callable

try:
    import serial  # type: ignore
except ImportError:  # pragma: no cover - handled at runtime
    serial = None  # type: ignore[assignment]


SERIAL_DEVICE_NAME = "arduino-greenhouse"
BOOLEAN_FIELDS = ("dry_soil", "high_temp", "low_light", "relay_on", "led_on")
INTEGER_FIELDS = ("uptime_ms", "soil_raw", "soil_pct", "light_raw", "light_pct")
FLOAT_FIELDS = ("temperature_c", "humidity_pct")
REQUIRED_FIELDS = (
    "device",
    "uptime_ms",
    "temperature_c",
    "humidity_pct",
    "soil_raw",
    "soil_pct",
    "light_raw",
    "light_pct",
    "dry_soil",
    "high_temp",
    "low_light",
    "relay_on",
    "led_on",
)


@dataclass(slots=True)
class SerialStatus:
    state: str
    message: str
    port: str | None = None
    baudrate: int | None = None
    updated_at: str | None = None


def utc_now_iso() -> str:
    return datetime.now(timezone.utc).isoformat(timespec="seconds")


def _coerce_int(value: Any, field: str) -> int:
    if isinstance(value, bool):
        raise ValueError(f"{field} must be an integer")
    if isinstance(value, int):
        return int(value)
    if isinstance(value, float) and value.is_integer():
        return int(value)
    raise ValueError(f"{field} must be an integer")


def _coerce_float(value: Any, field: str) -> float:
    if isinstance(value, bool) or not isinstance(value, (int, float)):
        raise ValueError(f"{field} must be numeric")
    return float(value)


def _coerce_flag(value: Any, field: str) -> int:
    if isinstance(value, bool):
        return int(value)
    if isinstance(value, int) and value in (0, 1):
        return int(value)
    raise ValueError(f"{field} must be 0 or 1")


def validate_payload(payload: dict[str, Any]) -> dict[str, Any]:
    missing = [field for field in REQUIRED_FIELDS if field not in payload]
    if missing:
        raise ValueError(f"missing fields: {', '.join(missing)}")

    if payload["device"] != SERIAL_DEVICE_NAME:
        raise ValueError("unexpected device name")

    reading = {
        "received_at": utc_now_iso(),
        "device": str(payload["device"]),
    }

    for field in INTEGER_FIELDS:
        reading[field] = _coerce_int(payload[field], field)
    for field in FLOAT_FIELDS:
        reading[field] = _coerce_float(payload[field], field)
    for field in BOOLEAN_FIELDS:
        reading[field] = _coerce_flag(payload[field], field)

    if reading["soil_pct"] < 0 or reading["soil_pct"] > 100:
        raise ValueError("soil_pct must be between 0 and 100")
    if reading["light_pct"] < 0 or reading["light_pct"] > 100:
        raise ValueError("light_pct must be between 0 and 100")
    if reading["humidity_pct"] < 0 or reading["humidity_pct"] > 100:
        raise ValueError("humidity_pct must be between 0 and 100")
    if reading["temperature_c"] < -40 or reading["temperature_c"] > 125:
        raise ValueError("temperature_c out of expected range")
    if reading["uptime_ms"] < 0:
        raise ValueError("uptime_ms must be non-negative")

    return reading


def parse_json_line(line: str) -> dict[str, Any]:
    data = json.loads(line)
    if not isinstance(data, dict):
        raise ValueError("payload must be a JSON object")
    return validate_payload(data)


def parse_serial_line(line: str) -> dict[str, Any]:
    cleaned = line.strip()
    if not cleaned:
        raise ValueError("empty line")
    return parse_json_line(cleaned)


StatusCallback = Callable[[SerialStatus], None]
ReadingCallback = Callable[[dict[str, Any]], None]


class SerialReader(threading.Thread):
    """Background worker that reads and validates serial JSON lines."""

    daemon = True

    def __init__(
        self,
        port: str,
        baudrate: int,
        timeout: float,
        on_reading: ReadingCallback,
        on_status: StatusCallback | None = None,
        serial_factory: Callable[..., Any] | None = None,
    ) -> None:
        super().__init__(name="greenhouse-serial-reader")
        self.port = port
        self.baudrate = baudrate
        self.timeout = timeout
        self.on_reading = on_reading
        self.on_status = on_status or (lambda _status: None)
        self.serial_factory = serial_factory
        self.stop_event = threading.Event()
        self.last_status = SerialStatus(
            state="starting",
            message="serial reader is starting",
            port=port,
            baudrate=baudrate,
            updated_at=utc_now_iso(),
        )

    def stop(self) -> None:
        self.stop_event.set()

    def _emit_status(self, state: str, message: str) -> None:
        self.last_status = SerialStatus(
            state=state,
            message=message,
            port=self.port,
            baudrate=self.baudrate,
            updated_at=utc_now_iso(),
        )
        self.on_status(self.last_status)

    def run(self) -> None:  # pragma: no cover - exercised via integration
        if serial is None and self.serial_factory is None:
            self._emit_status("error", "pyserial is not installed")
            return

        factory = self.serial_factory or serial.Serial
        try:
            connection = factory(self.port, self.baudrate, timeout=self.timeout)
        except Exception as exc:  # noqa: BLE001 - serial errors are environment dependent
            self._emit_status("error", f"unable to open serial port: {exc}")
            return

        self._emit_status("connected", f"listening on {self.port} at {self.baudrate} baud")
        try:
            while not self.stop_event.is_set():
                raw = connection.readline()
                if not raw:
                    continue
                try:
                    line = raw.decode("utf-8", errors="replace")
                except Exception:
                    line = str(raw)
                try:
                    reading = parse_serial_line(line)
                except Exception as exc:  # noqa: BLE001 - validation should not stop the reader
                    self._emit_status("warning", f"invalid payload ignored: {exc}")
                    continue
                self.on_reading(reading)
        finally:
            try:
                connection.close()
            finally:
                self._emit_status("disconnected", f"serial reader stopped for {self.port}")


def start_serial_reader(
    port: str,
    baudrate: int,
    timeout: float,
    on_reading: ReadingCallback,
    on_status: StatusCallback | None = None,
    serial_factory: Callable[..., Any] | None = None,
) -> SerialReader:
    reader = SerialReader(
        port=port,
        baudrate=baudrate,
        timeout=timeout,
        on_reading=on_reading,
        on_status=on_status,
        serial_factory=serial_factory,
    )
    reader.start()
    return reader
