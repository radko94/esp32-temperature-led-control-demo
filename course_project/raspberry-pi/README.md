# Raspberry Pi Edge Node

This directory contains the Raspberry Pi side of the Theme 5 Task 8 smart greenhouse coursework project.

The application does three things:

1. reads JSON lines from Arduino over USB Serial;
2. validates and stores the readings in SQLite;
3. shows the latest values and recent history in a local Flask dashboard.

## Payload contract

The Arduino side should send one JSON object per line using this schema:

```json
{"device":"arduino-greenhouse","uptime_ms":12345,"temperature_c":24.5,"humidity_pct":48.0,"soil_raw":612,"soil_pct":40,"light_raw":320,"light_pct":31,"dry_soil":1,"high_temp":0,"low_light":0,"relay_on":1,"led_on":1}
```

## Files

- `app.py` - Flask entry point and runtime wiring
- `db.py` - SQLite helpers
- `serial_reader.py` - USB serial reader and payload validation
- `templates/index.html` - dashboard view
- `static/style.css` - dashboard styling

## Setup

Install dependencies:

```bash
pip install -r requirements.txt
```

Run the dashboard:

```bash
python app.py
```

By default the app listens on `0.0.0.0:5000` and tries `/dev/ttyACM0` at `115200` baud so it matches the Arduino firmware.

## Configuration

Environment variables:

- `APP_HOST` - Flask bind host, default `0.0.0.0`
- `APP_PORT` - Flask port, default `5000`
- `DATABASE_PATH` - SQLite file path, default `data/greenhouse.sqlite3`
- `SERIAL_PORT` - USB serial device, default `/dev/ttyACM0`
- `SERIAL_BAUDRATE` - serial speed, default `115200`
- `SERIAL_TIMEOUT` - serial read timeout in seconds, default `1.0`
- `SERIAL_ENABLED` - set to `0`, `false`, `no`, or `off` to disable serial startup
- `START_SERIAL_READER` - set to `0`, `false`, `no`, or `off` to skip starting the reader thread
- `HISTORY_LIMIT` - number of recent rows shown on the dashboard, default `12`

Example:

```bash
APP_PORT=8000 SERIAL_PORT=/dev/ttyUSB0 python app.py
```

## Behavior when Arduino is unavailable

The app still starts if the serial port is missing or unavailable. The dashboard shows the current serial status instead of crashing, which makes it suitable for coursework demos and offline development.

## Testable entry points

The code keeps the main operations split into small functions so later tests can target them directly:

- `db.initialize_database`
- `db.insert_reading`
- `db.fetch_latest_reading`
- `serial_reader.parse_serial_line`
- `serial_reader.validate_payload`
- `create_app`
- `load_settings`
- `build_dashboard_context`
