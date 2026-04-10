# AGENTS.md

## Project purpose
This repository is for a university Internet of Things assignment implemented with VS Code + Wokwi.

The current focus is Theme 5, Task 1.

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

Assume the deliverable is a simulation-first student project, not production firmware.

## Default constraints
- Keep implementations small and screenshot-friendly
- Prioritize readability over optimization
- Prefer common libraries that work cleanly in Wokwi
- Use stable, common parts only
- Do not introduce Raspberry Pi unless the task explicitly asks for it
- Do not add MQTT, REST, Adafruit IO, or IFTTT for Task 1

## Files expected
Common files may include:
- TASK_1_BRIEF.md
- AGENTS.md
- sketch.ino
- diagram.json
- wokwi.toml
- .assets/Тема 5 - Задачи - Обща характеристика на софтуера(1).docx
- .assets/Примерна структура на курсова задача .docx

## Definition of done for Task 1
A Task 1 implementation is done when:
- Wokwi simulation runs without errors
- sensor values are readable in serial output
- LED threshold behavior works
- the result is easy to screenshot and explain
- the code is suitable for an academic report

## Help expected from Codex
When asked to help:
1. Read TASK_1_BRIEF.md first
2. Read "Тема 5 - Задачи - Обща характеристика на софтуера(1).docx" after that
3. Make an online research on the best practices
4. CHeck if there an community solutions and discussion about the topic
5. Check how the community have solved such problem
6. Follow the assignment constraints
7. Propose a plan before large edits
8. Keep code and circuit minimal
9. Explain any file changes clearly
10. Suggest a short manual testing procedure