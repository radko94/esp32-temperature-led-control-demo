# ESP32 DHT22 Threshold Demo

Small Wokwi + PlatformIO project for a university Internet of Things assignment.

The project demonstrates local sensing, local decision making, and local actuation:
- an ESP32 reads temperature and humidity from a DHT22 sensor
- the measured temperature is compared against a fixed threshold
- an external LED turns on when the temperature is above the threshold
- the serial monitor prints readable sensor values and LED status

## Hardware and Simulation

The project uses:
- ESP32 DevKit v1
- DHT22 temperature/humidity sensor
- 1 external LED
- 1 LED resistor (`220 ohm`)
- Wokwi simulator
- PlatformIO in VS Code

## Current Configuration

- Board: `esp32dev`
- Framework: `Arduino`
- Serial baud rate: `115200`
- DHT22 data pin: `GPIO15`
- LED pin: `GPIO18`
- Temperature threshold: `28.0 C`
- Sensor read interval: `2000 ms`
- Library: `DHTesp` / `DHT sensor library for ESPx`

## Behavior

On startup, the ESP32:
- initializes the serial monitor
- initializes the DHT22 sensor
- configures the LED pin as output

During runtime, it:
- reads temperature and humidity every 2 seconds
- prints temperature and humidity to the serial monitor
- compares temperature against the `28.0 C` threshold
- turns the LED on when temperature is above the threshold
- turns the LED off when temperature is at or below the threshold
- prints the current threshold state and LED state
- reports sensor read errors if the sensor cannot be read

## Wiring

- `DHT22 VCC -> ESP32 3V3`
- `DHT22 SDA -> ESP32 GPIO15`
- `DHT22 GND -> ESP32 GND`
- `LED anode -> resistor -> ESP32 GPIO18`
- `LED cathode -> ESP32 GND`

## Project Structure

- [src/main.cpp](src/main.cpp) - firmware logic
- [diagram.json](diagram.json) - Wokwi circuit diagram
- [platformio.ini](platformio.ini) - PlatformIO build configuration
- [wokwi.toml](wokwi.toml) - Wokwi firmware path configuration
- [libraries.txt](libraries.txt) - Wokwi library list
- [TASK_1_BRIEF.md](TASK_1_BRIEF.md) - local task brief
- [AGENTS.md](AGENTS.md) - project guidance

## How To Run

### Option 1: VS Code + PlatformIO

1. Open the project in VS Code.
2. Install the PlatformIO extension if needed.
3. Build the project.
4. Open `diagram.json` in the Wokwi simulator.
5. Start the simulation.

### Option 2: Terminal Build

Use the local PlatformIO binary:

```bash
~/.platformio/penv/bin/pio run
```

Then run the simulation from `diagram.json`.

## Testing in Wokwi

1. Start the simulation.
2. Open the DHT22 popup in Wokwi.
3. Set the temperature below `28.0 C`.
Expected result:
`Threshold status: NORMAL`
`LED state: OFF`
4. Raise the temperature above `28.0 C`.
Expected result:
`Threshold status: ABOVE LIMIT`
`LED state: ON`

## Example Serial Output

```text
Theme 5 - Task 1
ESP32 + DHT22 + LED threshold demo
DHT data pin: GPIO15
Temperature threshold: 28.0 C
Minimum DHT sampling period: 2000 ms

Temperature: 24.0 C
Humidity: 40.0 %
Threshold status: NORMAL
LED state: OFF
```

When the temperature is raised above the threshold:

```text
Temperature: 36.9 C
Humidity: 42.5 %
Threshold status: ABOVE LIMIT
LED state: ON
```

## Notes

- This project is intentionally small and beginner-friendly.
- It focuses on device-side logic only.
- Cloud services, dashboards, MQTT, and REST integrations are intentionally out of scope for this task.
