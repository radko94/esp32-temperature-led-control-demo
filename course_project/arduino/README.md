# Arduino Smart Greenhouse Controller

This directory contains the Arduino Uno side of the Theme 5 Task 8 hybrid IoT coursework project.

The firmware acts as the field/controller layer:

- reads greenhouse sensors locally
- applies simple threshold logic
- drives a relay and status LED
- sends one JSON line per sample to the Raspberry Pi over USB Serial
- keeps running even if the Raspberry Pi is disconnected

## Project files

- `platformio.ini` - PlatformIO configuration for Arduino Uno
- `src/main.cpp` - firmware implementation

## Hardware wiring

Suggested pin assignment:

- `D2` - DHT22 data pin
- `A0` - soil moisture sensor analog output
- `A1` - LDR / light sensor analog output
- `D7` - relay module input
- `D8` - status LED

The relay output is configured as active-low in the code because many relay modules behave that way. If your relay board is active-high, change `kRelayActiveLow` in `src/main.cpp`.

## Serial contract

The firmware emits one compact JSON object per sample on USB Serial:

```json
{"device":"arduino-greenhouse","uptime_ms":12345,"temperature_c":24.5,"humidity_pct":48.0,"soil_raw":612,"soil_pct":40,"light_raw":320,"light_pct":31,"dry_soil":1,"high_temp":0,"low_light":0,"relay_on":1,"led_on":1}
```

No extra log lines are printed. This keeps the Raspberry Pi side simple to parse.

## Logic

The local control rules are intentionally simple and explainable:

- `dry_soil` when `soil_pct < 35`
- `high_temp` when `temperature_c > 30.0`
- `low_light` when `light_pct < 25`
- `relay_on` when `dry_soil`
- `led_on` when any warning flag is true

## Calibration notes

The analog sensors need calibration against the actual hardware. The code uses these default raw reference values:

- soil dry: `820`
- soil wet: `430`
- light dark: `860`
- light bright: `180`

Adjust them in `src/main.cpp` if your readings are inverted or if your specific sensors produce different ranges. The percent values are derived by linearly mapping the raw analog input into `0..100`.

For the DHT22, the code uses the standard Arduino DHT library. Readings are sampled every `2.5` seconds, which is safe for the DHT22 timing limits.

## Build and upload

From this directory:

```bash
pio run
pio run --target upload
pio device monitor
```

If you are using the Arduino Uno with a different serial speed, update `monitor_speed` in `platformio.ini` and keep it aligned with `Serial.begin(...)` in `src/main.cpp`.
