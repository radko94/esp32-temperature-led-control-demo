"""SQLite helpers for the Raspberry Pi greenhouse dashboard."""

from __future__ import annotations

import json
import sqlite3
from pathlib import Path
from typing import Any


SCHEMA_SQL = """
CREATE TABLE IF NOT EXISTS readings (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    received_at TEXT NOT NULL,
    device TEXT NOT NULL,
    uptime_ms INTEGER NOT NULL,
    temperature_c REAL NOT NULL,
    humidity_pct REAL NOT NULL,
    soil_raw INTEGER NOT NULL,
    soil_pct INTEGER NOT NULL,
    light_raw INTEGER NOT NULL,
    light_pct INTEGER NOT NULL,
    dry_soil INTEGER NOT NULL,
    high_temp INTEGER NOT NULL,
    low_light INTEGER NOT NULL,
    relay_on INTEGER NOT NULL,
    led_on INTEGER NOT NULL,
    payload_json TEXT NOT NULL
);

CREATE INDEX IF NOT EXISTS idx_readings_received_at
    ON readings(received_at DESC);
"""


READING_COLUMNS = (
    "received_at",
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
    "payload_json",
)


def ensure_parent_directory(db_path: str | Path) -> None:
    Path(db_path).expanduser().resolve().parent.mkdir(parents=True, exist_ok=True)


def open_connection(db_path: str | Path) -> sqlite3.Connection:
    conn = sqlite3.connect(str(db_path))
    conn.row_factory = sqlite3.Row
    return conn


def initialize_database(db_path: str | Path) -> None:
    ensure_parent_directory(db_path)
    with open_connection(db_path) as conn:
        conn.executescript(SCHEMA_SQL)
        conn.commit()


def _row_to_dict(row: sqlite3.Row | None) -> dict[str, Any] | None:
    if row is None:
        return None
    return dict(row)


def insert_reading(db_path: str | Path, reading: dict[str, Any]) -> int:
    payload_json = json.dumps(reading, ensure_ascii=True, separators=(",", ":"))
    values = (
        reading["received_at"],
        reading["device"],
        reading["uptime_ms"],
        reading["temperature_c"],
        reading["humidity_pct"],
        reading["soil_raw"],
        reading["soil_pct"],
        reading["light_raw"],
        reading["light_pct"],
        reading["dry_soil"],
        reading["high_temp"],
        reading["low_light"],
        reading["relay_on"],
        reading["led_on"],
        payload_json,
    )

    placeholders = ", ".join("?" for _ in READING_COLUMNS)
    columns = ", ".join(READING_COLUMNS)
    with open_connection(db_path) as conn:
        cursor = conn.execute(
            f"INSERT INTO readings ({columns}) VALUES ({placeholders})",
            values,
        )
        conn.commit()
        return int(cursor.lastrowid)


def fetch_latest_reading(db_path: str | Path) -> dict[str, Any] | None:
    with open_connection(db_path) as conn:
        row = conn.execute(
            "SELECT * FROM readings ORDER BY id DESC LIMIT 1"
        ).fetchone()
    return _row_to_dict(row)


def fetch_recent_readings(db_path: str | Path, limit: int = 10) -> list[dict[str, Any]]:
    with open_connection(db_path) as conn:
        rows = conn.execute(
            "SELECT * FROM readings ORDER BY id DESC LIMIT ?",
            (limit,),
        ).fetchall()
    return [dict(row) for row in rows]


def count_readings(db_path: str | Path) -> int:
    with open_connection(db_path) as conn:
        row = conn.execute("SELECT COUNT(*) AS count FROM readings").fetchone()
    return int(row["count"]) if row is not None else 0
