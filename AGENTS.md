# AGENTS.md

## Project purpose
This repository is for a university Internet of Things coursework project implemented with VS Code.

The active assignment target is:

**Theme 5, Task 8: Hybrid IoT architectures with Raspberry Pi and Arduino**

The selected coursework concept is:

**Smart greenhouse using a hybrid Arduino + Raspberry Pi architecture**

The deliverable is a coursework-grade implementation and accompanying academic/project documentation. It is not a commercial or production-ready IoT system.

---

## Active assignment scope

The project must demonstrate a hybrid IoT model in which:

- **Arduino** acts as the field/controller layer
- **Raspberry Pi** acts as the edge/gateway/local server layer
- communication between the two layers is implemented through **USB Serial**
- the system is explained and documented as a smart greenhouse

The implementation should be real, demonstrable, and suitable for coursework defense.

---

## Repository layout

The active Theme 5 Task 8 coursework implementation lives in:

- `course_project/`

The existing `homework/` directory contains the earlier Theme 5 Task 1 ESP32/Wokwi demo and should be treated as reference material unless the user explicitly asks to modify it.

The `.assets/` directory contains assignment materials, research notes, and local planning context.

---

## Source priority
Use project sources in this order:

1. `.assets/TASK_8_COURSEWORK_BRIEF.md` for the full local implementation and documentation context
2. `.assets/Тема 5 - Задачи - Обща характеристика на софтуера(1).docx` for the official Theme 5 Task 8 wording
3. `.assets/Примерна структура на курсова задача .docx` as the main structure/template reference for the coursework document
4. The remaining `.assets` course materials as theory and background support
5. Online official documentation and standards for implementation details and best practices

If the local brief and the official task wording ever conflict, follow the official task wording and then adjust the local brief.

---

## Working style
Prefer:
- simple and robust solutions
- coursework-grade quality
- real implementation over empty theory
- clean separation between Arduino and Raspberry Pi responsibilities
- architecture that is easy to explain in the final report
- clear diagrams, test scenarios, and screenshot-friendly outputs
- truthful documentation of what is implemented vs what is proposed as future work

Avoid:
- feature creep
- production-grade complexity
- unnecessary frameworks
- fake cloud-heavy architecture
- claiming features are implemented when they are only proposed
- overengineering beyond coursework needs

---

## Technical architecture

### Arduino role
Arduino is the field controller.

Responsibilities:
- read sensors
- perform basic local threshold logic
- control simple actuators
- send structured data to Raspberry Pi over USB Serial
- continue basic local behavior independently of Raspberry Pi if needed

### Raspberry Pi role
Raspberry Pi is the edge node / local gateway / local server.

Responsibilities:
- receive serial data from Arduino
- parse and validate incoming payloads
- store readings locally
- provide local visualization/dashboard
- support higher-level monitoring and future extensibility

### Communication model
The actual implementation baseline is:

**USB Serial between Arduino and Raspberry Pi**

MQTT, REST, or cloud integrations may be discussed only as:
- future work
- architectural alternatives
- optional extensions

They are not the default implementation path.

---

## Recommended hardware scope

### Controllers
- Arduino Nano or Arduino Uno
- Raspberry Pi 4 or Raspberry Pi 5

### Sensors
Use these as the default smart greenhouse sensor set:
- DHT22 for air temperature and humidity
- soil moisture sensor
- LDR / light sensor (e.g. KY-018)

### Outputs / actuators
Use:
- one LED for status indication
- one relay module to represent a pump or fan

Optional:
- buzzer
- second LED for warning/error state

---

## Recommended software stack

### Arduino side
Use:
- Arduino framework
- C/C++ firmware
- Serial output
- simple threshold logic
- clean, readable sensor polling

### Raspberry Pi side
Use:
- Python 3
- `pyserial` for USB Serial communication
- `sqlite3` or SQLite for local storage
- Flask for a lightweight local dashboard

Prefer a small and explainable implementation over a complicated one.

---

## Default functional goal
The system should:
- read greenhouse sensor values
- send them from Arduino to Raspberry Pi over USB Serial
- store them locally on Raspberry Pi
- show them in a local dashboard
- control at least one simple actuator state
- be easy to test, explain, and document

---

## Serial payload guidance
Prefer a structured machine-readable format.

Recommended option:
- JSON on a single line per reading

Example:
`{\"temperature\":24.5,\"humidity\":48.0,\"soil\":612,\"light\":320,\"relay\":0,\"led\":1}`

Alternative only if needed:
- simple key-value line format

---

## Implementation philosophy
This is a coursework implementation, not a production system.

That means:
- local-only is acceptable
- simple dashboard is enough
- SQLite is enough
- one serial link is enough
- one greenhouse node is enough

Do not add:
- mobile apps
- full cloud backend
- enterprise auth
- production-grade security infrastructure
- multi-user management
- multi-node orchestration

unless the user explicitly asks.

---

## Files expected
Common files may include:
- `.assets/TASK_8_COURSEWORK_BRIEF.md`
- `AGENTS.md`
- `course_project/README.md`
- `course_project/arduino/src/main.cpp`
- `course_project/arduino/platformio.ini`
- `course_project/raspberry-pi/app.py`
- `course_project/raspberry-pi/serial_reader.py`
- `course_project/raspberry-pi/db.py`
- `course_project/raspberry-pi/templates/index.html`
- `course_project/raspberry-pi/requirements.txt`
- `course_project/docs/architecture.md`
- `course_project/docs/diagrams/`
- `course_project/docs/screenshots/`

Exact file structure may evolve, but it should remain simple and well organized.

---

## Definition of done for Task 8
A Task 8 coursework implementation is done when:

- Arduino reads the selected greenhouse sensors correctly
- Arduino applies at least one meaningful local control rule
- Arduino sends structured data reliably over USB Serial
- Raspberry Pi receives and parses the incoming data
- Raspberry Pi stores readings locally
- Raspberry Pi displays the latest readings in a local dashboard
- the architecture clearly demonstrates a hybrid Arduino + Raspberry Pi model
- the system is easy to explain in diagrams, screenshots, and the final coursework report

---

## Documentation expectations
The final coursework document should be project-oriented and should align with the course template for coursework structure.

It should include:
- title page
- goal
- acquired skills
- introduction
- historical/architectural background
- system concept
- Arduino role
- Raspberry Pi role
- communication model
- hardware/materials
- architecture and setup diagrams
- software implementation
- tests and results
- conclusions
- findings
- problems encountered
- bibliography
- appendices

---

## Help expected from Codex
When asked to help:

1. Read `.assets/TASK_8_COURSEWORK_BRIEF.md` first
2. Verify against the official Theme 5 Task 8 wording
3. Use `.assets/Примерна структура на курсова задача .docx` for coursework document structure
4. Keep the hybrid architecture central
5. Preserve USB Serial as the implementation baseline
6. Work inside `course_project/` for the Task 8 implementation unless the user explicitly asks otherwise
7. Propose a practical implementation plan before major edits
8. Keep the code and architecture simple, modular, and explainable
9. Distinguish clearly between implemented features and future extensions
10. Suggest realistic test scenarios
11. Prioritize coursework quality over unnecessary complexity
