# Theme 5 Task 8 Course Project

This project implements a hybrid IoT smart greenhouse for Theme 5, Task 8. The coursework model is deliberately split into two layers:

- `Arduino` is the field controller layer.
- `Raspberry Pi` is the edge node and local server layer.
- `USB Serial` is the communication bridge between the two.

The repository is separate from `../homework/`, which contains the earlier Theme 5 Task 1 ESP32/Wokwi demo and should be treated as reference material unless explicitly needed.

## Coursework Scope

The baseline smart greenhouse concept uses:

- `DHT22` for air temperature and humidity.
- A soil moisture sensor for substrate wetness.
- An `LDR` or `KY-018` light sensor for ambient light.
- One `LED` for status or warning indication.
- One `relay` module to represent a pump or fan.

The intended software stack on the Raspberry Pi side is:

- Python 3.
- `pyserial` for serial reception.
- `sqlite3` for local persistence.
- Flask for a lightweight dashboard.

The serial payload is defined as a JSON line with one object per reading:

```json
{"device":"arduino-greenhouse","uptime_ms":12345,"temperature_c":24.5,"humidity_pct":48.0,"soil_raw":612,"soil_pct":40,"light_raw":320,"light_pct":31,"dry_soil":1,"high_temp":0,"low_light":0,"relay_on":1,"led_on":1}
```

The Raspberry Pi adds a receive timestamp when saving records locally.

## How the Parts Fit Together

1. Arduino reads the sensors and applies simple local threshold logic.
2. Arduino updates the LED and relay state.
3. Arduino sends a structured JSON line over USB Serial.
4. Raspberry Pi reads, validates, and stores each message in SQLite.
5. Flask shows the latest readings and the current actuator state in a local dashboard.

This layout is academically useful because it separates deterministic hardware control from higher-level storage and visualization.

## Repository Layout

```text
course_project/
├─ README.md
├─ arduino/
│  ├─ README.md
│  ├─ platformio.ini
│  └─ src/main.cpp
├─ raspberry-pi/
│  ├─ README.md
│  ├─ app.py
│  ├─ db.py
│  ├─ serial_reader.py
│  ├─ requirements.txt
│  ├─ static/style.css
│  └─ templates/index.html
├─ docs/
│  ├─ architecture.md
│  └─ test-scenarios.md
└─ coursework-report/
   └─ report-outline.md
```

The code and documentation are intentionally kept separate so the project is easy to explain during coursework defense.

## Current Documentation Scope

Implemented so far:

- Arduino firmware for local sensing and actuator control;
- the JSON-line serial contract;
- a Raspberry Pi serial reader, SQLite storage, and Flask dashboard;
- the test scenarios needed for defense and evaluation.

Scaffolded but not finished:

- the coursework report outline;
- final diagrams and screenshots for the report package.

Deferred to future work:

- MQTT or REST transport;
- cloud synchronization;
- remote or multi-user access control;
- multi-node greenhouse scaling;
- wiring photos and final screenshots.

## Key Coursework Message

The project is not a cloud platform or a production greenhouse controller. It is a defendable coursework implementation of a real hybrid IoT pattern:

- Arduino handles field I/O and immediate control.
- Raspberry Pi handles edge processing, local storage, and visualization.
- USB Serial keeps the architecture simple, traceable, and easy to demonstrate.
