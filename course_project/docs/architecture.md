# Architecture

## System Overview

The coursework system is a smart greenhouse built as a hybrid IoT architecture.

- `Arduino Uno` acts as the field controller.
- `Raspberry Pi` acts as the edge node, local gateway, and local server.
- `USB Serial` at `115200` baud carries the data between both layers.

This separation is the main academic point of the project. Arduino keeps direct control over sensors and actuators, while Raspberry Pi provides persistence and visualization.

## Layer Responsibilities

### Arduino field layer

Arduino is responsible for:

- reading the `DHT22` air temperature and humidity sensor on `D2`;
- reading the soil moisture sensor on `A0`;
- reading the `LDR` or `KY-018` light sensor on `A1`;
- evaluating simple threshold rules;
- controlling the warning `LED` on `D8`;
- controlling the `relay` on `D7`;
- sending one structured reading per line to the Raspberry Pi.

The Arduino side should remain usable even if the Raspberry Pi is temporarily unavailable. That is important for the hybrid model discussion in the report.

### Raspberry Pi edge layer

Raspberry Pi is responsible for:

- opening the USB serial port;
- reading and validating incoming JSON lines;
- storing readings locally in SQLite;
- exposing the latest readings in a Flask dashboard;
- keeping historical records for demonstration and review.

This side does not replace the Arduino controller. It extends it with storage and user-facing visibility.

## Data Flow

```text
Sensors -> Arduino -> USB Serial -> Raspberry Pi -> SQLite -> Flask dashboard
```

The intended sequence is:

1. Sensors produce readings.
2. Arduino samples the values.
3. Arduino converts raw analog values into simple percentages for soil and light.
4. Arduino applies local threshold logic.
5. Arduino updates the relay and LED states.
6. Arduino emits a JSON line over USB Serial.
7. Raspberry Pi parses the line, validates it, and saves it locally.
8. Flask renders the latest state for review.

## Serial Contract

The serial interface uses JSON lines, with one object per message.

Example payload:

```json
{"device":"arduino-greenhouse","uptime_ms":12345,"temperature_c":24.5,"humidity_pct":48.0,"soil_raw":612,"soil_pct":40,"light_raw":320,"light_pct":31,"dry_soil":1,"high_temp":0,"low_light":0,"relay_on":1,"led_on":1}
```

Field meaning:

- `device`: fixed identifier for payload validation.
- `uptime_ms`: Arduino uptime in milliseconds.
- `temperature_c`: air temperature in degrees Celsius.
- `humidity_pct`: relative air humidity in percent.
- `soil_raw`: raw soil moisture reading.
- `soil_pct`: soil moisture converted to `0..100`.
- `light_raw`: raw light reading.
- `light_pct`: light level converted to `0..100`.
- `dry_soil`, `high_temp`, `low_light`: local warning flags.
- `relay_on`, `led_on`: actuator state flags.

The Raspberry Pi may add a storage timestamp when writing the record to SQLite. The timestamp is part of the database record, not the serial payload itself.

## Control Rules

The baseline controller logic is intentionally simple:

- `dry_soil` when `soil_pct < 35`
- `high_temp` when `temperature_c > 30.0`
- `low_light` when `light_pct < 25`
- `relay_on` when `dry_soil`
- `led_on` when any warning flag is true

These rules are easy to demonstrate and easy to defend academically.

## Software Stack

### Arduino side

- Arduino framework
- C/C++ firmware
- sensor polling
- threshold-based control
- Serial output

### Raspberry Pi side

- Python 3
- `pyserial`
- `sqlite3`
- Flask

This stack is intentionally small. It is enough for a coursework defense and avoids unnecessary complexity.

## Current Baseline vs Future Work

### Baseline to document and defend

- sensor acquisition on Arduino;
- local LED and relay control;
- JSON line serial output;
- serial parsing on Raspberry Pi;
- SQLite logging;
- Flask dashboard.

### Future extensions

- MQTT transport;
- REST API exposure;
- remote cloud synchronization;
- mobile dashboard;
- multi-node greenhouse scaling.

These future items may be mentioned in the report as alternatives, but they are not the primary implementation path.

## Why This Architecture Fits the Coursework

The architecture is easy to explain academically because each layer has a distinct role:

- Arduino handles real-time I/O and deterministic control.
- Raspberry Pi handles storage, visualization, and extensibility.
- USB Serial keeps the communication path direct and easy to test.

That makes the system suitable for diagrams, live demonstration, and written evaluation of the hybrid IoT model.
