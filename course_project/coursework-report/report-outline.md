# Coursework Report Outline

This outline follows the Task 8 brief and keeps the report focused on the actual hybrid smart greenhouse system.

## 1. Title Page

- Project title
- Author
- Faculty / course details
- Supervisor
- Academic year

## 2. Goal of the Coursework

- explain the purpose of the smart greenhouse;
- show why a hybrid Arduino + Raspberry Pi model is appropriate;
- define the role of USB Serial in the system.

## 3. Skills Acquired Through Development

- embedded sensor integration;
- basic actuator control;
- serial communication;
- local data storage;
- lightweight web visualization;
- system decomposition into field and edge layers.

## 4. Introduction

- define IoT and hybrid architectures;
- explain why greenhouse monitoring is a suitable example;
- state the chosen platform split.

## 5. Chronological Retrospective of Hybrid IoT Architectures

- microcontroller-based control;
- mini-computer and edge computing growth;
- separation of field control and local services;
- relevance of the approach for small IoT systems.

## 6. System Concept: Smart Greenhouse

- monitored parameters;
- actuator goals;
- why the greenhouse problem is practical for coursework;
- what the system demonstrates.

## 7. Role of Arduino in the System

- sensor acquisition;
- threshold logic;
- LED and relay control;
- structured serial output;
- local autonomy when the Pi is unavailable.

## 8. Role of Raspberry Pi in the System

- serial reception;
- data validation;
- SQLite storage;
- Flask dashboard;
- local review and extensibility.

## 9. Communication Between the Two Layers

- USB Serial as the fixed transport;
- JSON line payload structure;
- why the format is easy to parse and defend;
- comparison with MQTT and REST as future alternatives.

## 10. Materials and Components Used

- Arduino board;
- Raspberry Pi board;
- DHT22;
- soil moisture sensor;
- LDR or KY-018;
- LED;
- relay module;
- USB cable and wiring.

## 11. Working / Architecture Diagram

- overall block diagram;
- data flow from sensors to dashboard;
- layer separation;
- optional placement of the SQLite database.

## 12. Setup / Wiring / Deployment Scheme

- sensor and actuator connections;
- serial connection between the boards;
- power and placement notes;
- screenshot or wiring photo placeholders.

## 13. Software Implementation

- Arduino firmware structure;
- Raspberry Pi serial reader;
- SQLite schema and storage logic;
- Flask dashboard endpoints or page structure;
- serial payload example.

## 14. Tests and Results

- normal conditions;
- dry soil;
- high temperature;
- low light;
- serial interruption;
- malformed message handling.

## 15. Reliability and Advantages of the Hybrid Model

- Arduino advantages for field control;
- Raspberry Pi advantages for storage and visualization;
- benefits of the split architecture;
- local resilience and maintainability.

## 16. Conclusion

- summarize what the system demonstrates;
- evaluate whether the coursework goal was achieved;
- state the educational value of the hybrid model.

## 17. Findings

- what worked well in practice;
- what was easy to explain;
- what design choices simplified testing and defense.

## 18. Problems Encountered During Development

- sensor noise or calibration issues;
- serial parsing issues;
- dashboard refresh or storage edge cases;
- how they were handled.

## 19. Bibliography

- official Arduino documentation;
- Raspberry Pi documentation;
- Python and Flask documentation;
- serial communication references;
- any course materials or standards used.

## 20. Appendices

- source code excerpts;
- serial payload example;
- screenshots of the dashboard;
- test evidence;
- wiring notes;
- additional diagrams.

## Report Truthfulness Rules

- Clearly mark what is implemented and what is future work.
- Do not present MQTT, REST, or cloud integration as implemented if they are only discussed as extensions.
- Keep the hybrid split visible in every major chapter.
- Use concrete test results and screenshots where possible.

## Suggested Writing Order

1. Write the architecture and system concept first.
2. Draft the Arduino and Raspberry Pi roles.
3. Add the serial contract and implementation details.
4. Insert test scenarios and recorded results.
5. Finish with conclusions, findings, and future work.
