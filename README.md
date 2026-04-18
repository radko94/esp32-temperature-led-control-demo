# BFU IoT Course Repository

This repository contains coursework and project work for a university Internet of Things course.

The repository currently has two main parts:

- `homework/` - the earlier Theme 5, Task 1 practical demo
- `course_project/` - the active Theme 5, Task 8 coursework project

## Current Focus

The active assignment target is:

**Theme 5, Task 8: Hybrid IoT architectures with Raspberry Pi and Arduino**

The selected coursework concept is:

**Smart greenhouse using a hybrid Arduino + Raspberry Pi architecture**

In this project:

- `Arduino` acts as the field controller
- `Raspberry Pi` acts as the edge node and local server
- `USB Serial` is the communication path between them

## Repository Structure

```text
.
├─ AGENTS.md
├─ README.md
├─ .assets/
├─ homework/
└─ course_project/
```

### `homework/`

This directory contains the completed Theme 5, Task 1 reference implementation:

- ESP32
- DHT22
- LED threshold logic
- Wokwi + PlatformIO setup

Use it as reference material unless there is a specific reason to modify it.

### `course_project/`

This directory contains the active Theme 5, Task 8 coursework implementation:

- Arduino firmware for greenhouse sensing and local control
- Raspberry Pi serial receiver, SQLite storage, and Flask dashboard
- architecture notes and test scenarios
- coursework report outline

See [course_project/README.md](/home/rapostolov/Desktop/programing/bfu_iot_course/course_project/README.md:1) for the detailed project description.

## Supporting Materials

The `.assets/` directory contains:

- local briefs
- course assignment files
- theory materials
- document templates

For Task 8 work, the main local brief is:

- [.assets/TASK_8_COURSEWORK_BRIEF.md](/home/rapostolov/Desktop/programing/bfu_iot_course/.assets/TASK_8_COURSEWORK_BRIEF.md:1)

## Recommended Reading Order

1. [AGENTS.md](/home/rapostolov/Desktop/programing/bfu_iot_course/AGENTS.md:1)
2. [.assets/TASK_8_COURSEWORK_BRIEF.md](/home/rapostolov/Desktop/programing/bfu_iot_course/.assets/TASK_8_COURSEWORK_BRIEF.md:1)
3. [course_project/README.md](/home/rapostolov/Desktop/programing/bfu_iot_course/course_project/README.md:1)

## Status

Implemented so far:

- the Task 1 ESP32 demo in `homework/`
- the Task 8 hybrid codebase scaffold in `course_project/`

Still in progress:

- the final coursework report package
- diagrams, screenshots, and final defense-ready evidence

## Notes

This repository is coursework-oriented, not production-oriented. The goal is a clean, explainable, defendable IoT implementation rather than a commercial system.
