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


Библиография

[1] W3C, Web of Things (WoT) Architecture 1.1, W3C Recommendation, 2023.
Достъпно на: https://www.w3.org/TR/wot-architecture11/

[2] A. K. Dey, “Understanding and Using Context,” Personal and Ubiquitous Computing, vol. 5, no. 1, pp. 4–7, 2001.
Достъпно на: https://doi.org/10.1007/s007790170019

[3] M. Satyanarayanan, “The Emergence of Edge Computing,” Computer, vol. 50, no. 1, pp. 30–39, 2017.
Достъпно на: https://doi.org/10.1109/MC.2017.9

[4] Espressif Systems, Arduino ESP32 Documentation.
Достъпно на: https://docs.espressif.com/projects/arduino-esp32/

[5] Arduino, Using Functions in a Sketch; Getting Started with Arduino.
Достъпно на:
https://docs.arduino.cc/learn/programming/functions/
https://docs.arduino.cc/learn/starting-guide/getting-started-arduino/

[6] PlatformIO, Espressif 32 — PlatformIO Documentation; ESP32 Dev Module.
Достъпно на:
https://docs.platformio.org/en/latest/platforms/espressif32.html
https://docs.platformio.org/en/latest/boards/espressif32/esp32dev.html

[7] OASIS, MQTT Version 5.0.
Достъпно на: https://docs.oasis-open.org/mqtt/mqtt/v5.0/mqtt-v5.0.html

[8] Z. Shelby, K. Hartke, and C. Bormann, RFC 7252: The Constrained Application Protocol (CoAP), IETF, 2014.
Достъпно на: https://datatracker.ietf.org/doc/html/rfc7252

[9] M. Fagan, K. Megas, K. Scarfone, and M. Smith, NISTIR 8259A: IoT Device Cybersecurity Capability Core Baseline, National Institute of Standards and Technology, 2020.
Достъпно на: https://csrc.nist.gov/pubs/ir/8259/a/final

[10] Espressif Systems, ESP-IDF Programming Guide: Secure Boot v2 for ESP32.
Достъпно на: https://docs.espressif.com/projects/esp-idf/en/stable/esp32/security/secure-boot-v2.html

[11] Espressif Systems, ESP-IDF Programming Guide: Flash Encryption for ESP32.
Достъпно на: https://docs.espressif.com/projects/esp-idf/en/stable/esp32/security/flash-encryption.html

[12] Adafruit, DHT11, DHT22 and AM2302 Sensors; Using a DHTxx Sensor with Arduino.
Достъпно на:
https://learn.adafruit.com/dht/overview
https://learn.adafruit.com/dht/using-a-dhtxx-sensor-with-arduino

[13] Python Software Foundation, Python Documentation: More Control Flow Tools.
Достъпно на: https://docs.python.org/3/tutorial/controlflow.html

[14] W3C, Web of Things (WoT) Overview.
Достъпно на: https://www.w3.org/WoT/