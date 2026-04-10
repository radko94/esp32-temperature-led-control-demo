# TASK 1 BRIEF

## University context

This task is from Theme 5, Task 1:
"Development of software methods for controlling IoT devices."

The final output is NOT just code.
The code is a small practical proof used to support an academic report.

## What the task must cover

The written work must explain:

1. How programming enables IoT devices to:
   - react to environmental input
   - collect data
   - perform automated actions

2. Historical evolution of software methods:
   - 1970–2000: procedural / imperative programming (C, C++, Pascal)
   - 2000–2015: interpreted and web-oriented languages (Python, JavaScript)
   - 2015–2026: Blockly, low-code, AI-assisted programming, edge computing, context-aware logic, autonomous IoT algorithms

3. A real modern IoT device example:
   - what kind of software it runs
   - what logic structures it uses
   - how data is processed locally and/or in the cloud

4. Final conclusion:
   - which programming skills are most important for IoT development in 2026

## Chosen practical concept

We will build a small, simple ESP32 simulation in Wokwi using VS Code.

### Selected hardware

- ESP32 DevKit
- DHT22 temperature/humidity sensor
- 1 LED
- 1 resistor for the LED

### Selected behavior

- The ESP32 reads temperature and humidity from the DHT22
- The values are printed to the serial monitor
- If temperature is above a threshold, the LED turns on
- If temperature is below the threshold, the LED turns off
- The behavior must be stable and easy to demonstrate with screenshots

## Why this project was chosen

This project is intentionally simple.
Its purpose is to demonstrate:

- firmware logic
- sensor reading
- threshold-based IF decision making
- repeated execution in loop()
- local processing on the device

This is enough to support the academic explanation required by Task 1.

## Scope limits

Do NOT add:

- Raspberry Pi
- MQTT
- REST networking
- Adafruit IO
- IFTTT
- cloud dashboards
- complex multi-sensor logic
- unnecessary libraries
- advanced UI or external integrations

Those may be discussed in the written report as future extensions, but they are NOT part of this implementation.

## Deliverables needed from the practical side

We need:

1. A working Wokwi project
2. Code that compiles/runs without errors
3. Screenshot of the circuit
4. Screenshot of the serial monitor in normal condition
5. Screenshot of the serial monitor in triggered condition
6. Evidence that the LED changes state correctly
7. Clean code that is easy to explain in the report

## What the report will use from this project

The report will use this project as the practical example for:

- setup() and loop()
- sensor libraries
- local firmware behavior
- IF–THEN threshold logic
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
4. Use conventional pin assignments
5. Avoid unnecessary complexity
6. Help produce a short manual test checklist
7. Prefer reliability and clarity over extra features

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
4. Use conventional pin assignments
5. Avoid unnecessary complexity
6. Help produce a short manual test checklist
7. Prefer reliability and clarity over extra features
