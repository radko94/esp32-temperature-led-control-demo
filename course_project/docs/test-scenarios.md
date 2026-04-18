# Test Scenarios

This document defines the coursework test set for the smart greenhouse hybrid architecture. The scenarios are chosen to show that the system can be defended academically, not just technically.

## Test Goals

- verify sensor acquisition on Arduino;
- verify local actuator logic on Arduino;
- verify JSON serial output;
- verify serial reception on Raspberry Pi;
- verify local storage in SQLite;
- verify the Flask dashboard shows the latest state.

## Scenario 1: Normal Conditions

**Setup**

- temperature is within the expected range;
- soil moisture is acceptable;
- light level is acceptable;
- relay should remain off;
- LED should indicate normal operation.

**Expected result**

- Arduino sends a valid JSON line;
- Raspberry Pi stores the reading;
- dashboard shows stable values;
- no warning state is triggered.

## Scenario 2: Dry Soil

**Setup**

- soil moisture drops below the threshold.

**Expected result**

- Arduino turns the relay on to represent irrigation;
- the LED may indicate a warning state if that rule is configured;
- Raspberry Pi records the actuator state as `relay_on: 1`;
- dashboard reflects the irrigation condition.

## Scenario 3: High Temperature

**Setup**

- temperature rises above the configured limit.

**Expected result**

- Arduino triggers the warning rule;
- the LED turns on or changes state to indicate a problem;
- Raspberry Pi logs the message correctly;
- dashboard shows the high-temperature condition.

## Scenario 4: Low Light

**Setup**

- ambient light falls below the expected level.

**Expected result**

- Arduino records the low-light state;
- Arduino sends `low_light: 1` in a valid JSON payload;
- the dashboard highlights the condition;
- the serial message remains valid and readable.

## Scenario 5: Serial Link Interrupted

**Setup**

- USB Serial is disconnected or the Raspberry Pi receiver is stopped.

**Expected result**

- Arduino continues local sensor and actuator logic;
- the field controller still behaves predictably;
- when the link is restored, data reception resumes.

## Scenario 6: Invalid Serial Line

**Setup**

- a malformed line is sent to the Raspberry Pi receiver.

**Expected result**

- the receiver rejects the invalid message;
- the application does not crash;
- only valid readings are stored.

## Evidence to Capture

For report defense, capture:

- serial monitor output or terminal logs;
- SQLite entries or sample query output;
- Flask dashboard screenshot;
- a short photo or diagram of the wiring setup;
- a screenshot showing at least one threshold-triggered state.

## Acceptance Criteria

The system is considered suitable for coursework defense when:

- the data flow works from Arduino to Raspberry Pi;
- the payload format is stable and machine-readable;
- the local storage contains historical readings;
- the dashboard presents the latest state clearly;
- the hybrid role split is obvious in the implementation and the explanation.
