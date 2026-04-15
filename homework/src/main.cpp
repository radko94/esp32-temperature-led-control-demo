#include <Arduino.h>
#include "DHTesp.h"

// Task 1: read temperature/humidity and control an LED using a simple threshold.
const int DHT_PIN = 15;
const int LED_PIN = 18;
const float TEMP_THRESHOLD_C = 28.0;
const unsigned long READ_INTERVAL_MS = 2000;

DHTesp dhtSensor;

void printStartupMessage() {
  Serial.println();
  Serial.println("Theme 5 - Task 1");
  Serial.println("ESP32 + DHT22 + LED threshold demo");
  Serial.print("DHT data pin: GPIO");
  Serial.println(DHT_PIN);
  Serial.print("Temperature threshold: ");
  Serial.print(TEMP_THRESHOLD_C, 1);
  Serial.println(" C");
  Serial.print("Minimum DHT sampling period: ");
  Serial.print(dhtSensor.getMinimumSamplingPeriod());
  Serial.println(" ms");
  Serial.println();
}

void setup() {
  Serial.begin(115200);

  pinMode(LED_PIN, OUTPUT);
  digitalWrite(LED_PIN, LOW);

  dhtSensor.setup(DHT_PIN, DHTesp::DHT22);
  printStartupMessage();
}

void loop() {
  TempAndHumidity data = dhtSensor.getTempAndHumidity();

  if (dhtSensor.getStatus() != 0) {
    digitalWrite(LED_PIN, LOW);
    Serial.print("Sensor read error: ");
    Serial.println(dhtSensor.getStatusString());
    Serial.println("LED state: OFF");
    Serial.println();
    delay(READ_INTERVAL_MS);
    return;
  }

  bool thresholdExceeded = data.temperature > TEMP_THRESHOLD_C;
  digitalWrite(LED_PIN, thresholdExceeded ? HIGH : LOW);

  Serial.print("Temperature: ");
  Serial.print(data.temperature, 1);
  Serial.println(" C");

  Serial.print("Humidity: ");
  Serial.print(data.humidity, 1);
  Serial.println(" %");

  Serial.print("Threshold status: ");
  Serial.println(thresholdExceeded ? "ABOVE LIMIT" : "NORMAL");

  Serial.print("LED state: ");
  Serial.println(thresholdExceeded ? "ON" : "OFF");
  Serial.println();

  delay(READ_INTERVAL_MS);
}
