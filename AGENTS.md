# AGENTS.md

## Project purpose
This repository is for a university Internet of Things assignment implemented with VS Code and Wokwi.

The active assignment target is Theme 5, Task 1:
"Development of software methods for controlling IoT devices."

The deliverable is a small simulation-first student project that supports an academic report. It is not production firmware.

## Source priority
Use the project sources in this order:

1. `TASK_1_BRIEF.md` for the local implementation plan
2. `.assets/Тема 5 - Задачи - Обща характеристика на софтуера(1).docx` for the official Theme 5 task wording
3. `.assets/Примерна структура на курсова задача .docx` only as a report structure/template reference
4. The remaining `.assets` lecture files as theory and context support

If the local brief and the official Theme 5 task wording ever conflict, follow the official task wording and then adjust the local brief.

If the generic course template suggests cloud integrations, dashboards, or IFTTT-style workflows, do not expand Task 1 scope unless the user explicitly asks for that.

## Working style
Prefer:
- simple solutions
- stable Wokwi-compatible implementations
- clear code comments
- beginner-friendly structure
- easy-to-document outputs

Avoid:
- feature creep
- unnecessary abstraction
- extra hardware not requested
- cloud/network complexity unless explicitly requested
- changing the assignment scope

## Technical stack
Use:
- ESP32 DevKit
- Arduino-style sketch
- Wokwi simulation
- VS Code workflow

## Default constraints
- Keep implementations small and screenshot-friendly
- Prioritize readability over optimization
- Prefer common libraries that work cleanly in Wokwi
- Use stable, common parts only
- Do not introduce Raspberry Pi unless the task explicitly asks for it
- Do not add MQTT, REST, Adafruit IO, or IFTTT for Task 1
- Prefer local device logic over network features for the practical demo

## Task 1 implementation target
The default practical concept for Task 1 is:
- ESP32 DevKit
- DHT22 temperature/humidity sensor
- one external LED
- one LED resistor
- serial output with readable sensor values
- threshold-based LED control based on temperature

The practical demo should show local sensing, local decision making, and local actuation.

## Practical guidance
- Keep the circuit minimal and easy to explain in a report
- Use safe, conventional ESP32 GPIOs for the selected parts
- Avoid problematic ESP32 pins for the DHT data line, especially flash pins and input-only pins
- Prefer stable polling intervals for DHT sensors
- Make the serial output easy to screenshot

## Files expected
Common files may include:
- `TASK_1_BRIEF.md`
- `AGENTS.md`
- `sketch.ino`
- `diagram.json`
- `wokwi.toml`
- `libraries.txt`
- `.assets/Тема 5 - Задачи - Обща характеристика на софтуера(1).docx`
- `.assets/Примерна структура на курсова задача .docx`

## Definition of done for Task 1
A Task 1 implementation is done when:
- the Wokwi simulation runs without errors
- the ESP32 reads the sensor values correctly
- the serial monitor shows readable temperature and humidity values
- the LED threshold behavior works reliably
- the circuit and output are easy to screenshot and explain
- the code is simple enough to support an academic report

## Help expected from Codex
When asked to help:
1. Read `TASK_1_BRIEF.md` first
2. Verify it against `.assets/Тема 5 - Задачи - Обща характеристика на софтуера(1).docx`
3. Use `.assets/Примерна структура на курсова задача .docx` only for report formatting ideas
4. Review the other `.assets` materials for course context, especially Themes 5, 6, and 7
5. Make brief online research on relevant best practices
6. Check for community examples or discussion that improve reliability or clarity
7. Propose a plan before larger edits
8. Keep the code and circuit minimal
9. Explain file changes clearly
10. Suggest a short manual testing procedure
