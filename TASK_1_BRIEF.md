# TASK 1 BRIEF

## Assignment identity
This repository targets Theme 5, Task 1:
"Development of software methods for controlling IoT devices."

The final output is not just code. The code is a small practical proof used to support an academic report.

If broader course materials show cloud-connected examples, those examples are background context only. They are not required for this Task 1 implementation.

## What the written work must cover
The report should explain:

1. How programming enables IoT devices to:
   - react to environmental input
   - collect data
   - perform automated actions

2. Historical evolution of software methods:
   - 1970-2000: procedural / imperative programming (C, C++, Pascal)
   - 2000-2015: interpreted and web-oriented languages (Python, JavaScript)
   - 2015-2026: Blockly, low-code, AI-assisted programming, edge computing, context-aware logic, autonomous IoT algorithms

3. A real modern IoT device example:
   - what kind of software it runs
   - what logic structures it uses
   - how data is processed locally and/or in the cloud

4. Final conclusion:
   - which programming skills are most important for IoT development in 2026

## Chosen practical concept
We will build a small ESP32 simulation in Wokwi using VS Code and PlatformIO.

Its role is to provide a clean, easy-to-explain practical example for the report.

## Locked implementation profile
Use the following practical defaults unless the user explicitly changes them:

- Board: ESP32 DevKit v1
- Sensor: DHT22 temperature/humidity sensor
- Output: one external LED
- Resistor: one LED resistor, typically 220 ohm
- Development style: Arduino framework project for ESP32 in Wokwi/PlatformIO
- Serial baud rate: `115200`
- Temperature threshold: `28.0 C`
- Sensor read interval: `2000 ms` minimum
- DHT22 data pin: `GPIO15`
- LED pin: `GPIO18`
- Processing model: local only, on the device

## Library target
Prefer:
- `DHTesp`

Reason:
- it works cleanly with ESP32 and Wokwi, keeps the code small, and matches the current project implementation

## Required runtime behavior
The practical demo must do the following:

- initialize the serial monitor
- initialize the DHT22 sensor
- initialize the LED pin as output
- read temperature and humidity repeatedly
- print readable values to the serial monitor on every cycle
- compare the temperature against the threshold
- turn the LED on when the temperature is above the threshold
- turn the LED off when the temperature is at or below the threshold
- print the LED state in the serial monitor
- handle failed sensor readings with a clear error message and retry on the next cycle

## Why this project was chosen
This project is intentionally simple.

Its purpose is to demonstrate:
- firmware logic
- sensor reading
- threshold-based IF decision making
- repeated execution in `loop()`
- local processing on the device

This is enough to support the academic explanation required by Theme 5, Task 1.

## Scope limits
Do not add:

- Raspberry Pi
- MQTT
- REST networking
- Adafruit IO
- IFTTT
- cloud dashboards
- complex multi-sensor logic
- unnecessary libraries
- advanced UI or external integrations

These may be discussed in the report as future extensions, but they are not part of the practical implementation.

## ESP32 pin safety note
For this task, avoid using:
- `GPIO6-GPIO11` because they are commonly tied to flash hardware
- `GPIO34-GPIO39` for DHT data because they are input-only pins

Use ordinary, safe digital GPIOs for the DHT22 data line and LED output.

## Practical deliverables
We need:

1. A working Wokwi project
2. Code that compiles and runs without errors
3. A circuit diagram that matches the code
4. A screenshot of the circuit
5. A screenshot of the serial monitor in normal condition
6. A screenshot of the serial monitor in triggered condition
7. Evidence that the LED changes state correctly
8. Clean code that is easy to explain in the report

## Expected project files
The practical project should normally contain:
- `src/main.cpp`
- `platformio.ini`
- `diagram.json`
- `wokwi.toml`
- `libraries.txt` if external Arduino libraries are required

## What the report will use from this project
The report will use this project as the practical example for:

- `setup()` and `loop()`
- sensor libraries
- local firmware behavior
- IF-THEN threshold logic
- device-side data handling
- difference between local processing and possible cloud extension

## Success criteria
The implementation is successful if:

- the ESP32 reads the DHT22 correctly
- the serial monitor prints readable values
- the LED responds correctly to threshold changes
- the simulation is easy to screenshot
- the code is simple enough to explain in an academic report

## What Codex should help with
Codex should:

1. Create or update the Wokwi-compatible project files
2. Write clean Arduino code for the selected behavior
3. Keep the code simple and well commented
4. Use the locked practical defaults unless the user changes them
5. Avoid unnecessary complexity
6. Help produce a short manual test checklist
7. Prefer reliability and clarity over extra features
