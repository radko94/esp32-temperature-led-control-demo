from __future__ import annotations

import json
import sys
import unittest
from pathlib import Path


PROJECT_DIR = Path(__file__).resolve().parents[1]
if str(PROJECT_DIR) not in sys.path:
    sys.path.insert(0, str(PROJECT_DIR))

from serial_reader import parse_serial_line


VALID_PAYLOAD = {
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


class SerialReaderTests(unittest.TestCase):
    def test_parse_valid_serial_line(self) -> None:
        reading = parse_serial_line(json.dumps(VALID_PAYLOAD))

        self.assertEqual(reading["device"], "arduino-greenhouse")
        self.assertEqual(reading["soil_pct"], 40)
        self.assertEqual(reading["relay_on"], 1)
        self.assertIn("received_at", reading)

    def test_missing_field_is_rejected(self) -> None:
        invalid_payload = dict(VALID_PAYLOAD)
        invalid_payload.pop("led_on")

        with self.assertRaises(ValueError):
            parse_serial_line(json.dumps(invalid_payload))

    def test_invalid_flag_is_rejected(self) -> None:
        invalid_payload = dict(VALID_PAYLOAD)
        invalid_payload["relay_on"] = 2

        with self.assertRaises(ValueError):
            parse_serial_line(json.dumps(invalid_payload))


if __name__ == "__main__":
    unittest.main()
