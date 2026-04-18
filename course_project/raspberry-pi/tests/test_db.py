from __future__ import annotations

import sys
import tempfile
import unittest
from pathlib import Path


PROJECT_DIR = Path(__file__).resolve().parents[1]
if str(PROJECT_DIR) not in sys.path:
    sys.path.insert(0, str(PROJECT_DIR))

from db import count_readings, fetch_latest_reading, fetch_recent_readings, initialize_database, insert_reading


SAMPLE_READING = {
    "received_at": "2026-04-18T10:15:00+00:00",
    "device": "arduino-greenhouse",
    "uptime_ms": 12345,
    "temperature_c": 24.5,
    "humidity_pct": 48.0,
    "soil_raw": 612,
    "soil_pct": 40,
    "light_raw": 320,
    "light_pct": 31,
    "dry_soil": 1,
    "high_temp": 0,
    "low_light": 0,
    "relay_on": 1,
    "led_on": 1,
}


class DatabaseTests(unittest.TestCase):
    def test_round_trip_insert_and_fetch(self) -> None:
        with tempfile.TemporaryDirectory() as tmp_dir:
            db_path = Path(tmp_dir) / "greenhouse.sqlite3"
            initialize_database(db_path)

            row_id = insert_reading(db_path, SAMPLE_READING)
            latest = fetch_latest_reading(db_path)
            recent = fetch_recent_readings(db_path, limit=5)

            self.assertGreater(row_id, 0)
            self.assertIsNotNone(latest)
            assert latest is not None
            self.assertEqual(latest["device"], "arduino-greenhouse")
            self.assertEqual(latest["relay_on"], 1)
            self.assertEqual(count_readings(db_path), 1)
            self.assertEqual(len(recent), 1)


if __name__ == "__main__":
    unittest.main()
