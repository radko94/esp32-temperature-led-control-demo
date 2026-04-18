#include <Arduino.h>
#include <DHT.h>

namespace {

constexpr uint8_t kDhtPin = 2;
constexpr uint8_t kRelayPin = 7;
constexpr uint8_t kLedPin = 8;
constexpr uint8_t kSoilPin = A0;
constexpr uint8_t kLightPin = A1;

constexpr uint8_t kDhtType = DHT22;

// Common relay boards are active-low. Keep this configurable so the logical
// state in the JSON contract stays stable even if the wiring changes.
constexpr bool kRelayActiveLow = true;

// Sensor calibration values. Adjust these to match the actual wiring and sensor
// response on the bench before final demonstration.
constexpr int kSoilDryRaw = 820;
constexpr int kSoilWetRaw = 430;
constexpr int kLightDarkRaw = 860;
constexpr int kLightBrightRaw = 180;

constexpr int kDrySoilThresholdPct = 35;
constexpr float kHighTempThresholdC = 30.0f;
constexpr int kLowLightThresholdPct = 25;

constexpr unsigned long kSampleIntervalMs = 2500UL;

DHT dht(kDhtPin, kDhtType);

float last_temperature_c = 0.0f;
float last_humidity_pct = 0.0f;
unsigned long last_sample_ms = 0UL;

int clampPercent(int value) {
  if (value < 0) {
    return 0;
  }
  if (value > 100) {
    return 100;
  }
  return value;
}

int scaleAnalogToPercent(int raw, int dark_raw, int bright_raw) {
  if (dark_raw == bright_raw) {
    return 0;
  }

  long pct = map(raw, dark_raw, bright_raw, 0, 100);
  return clampPercent(static_cast<int>(pct));
}

bool readDht(float &temperature_c, float &humidity_pct) {
  const float humidity = dht.readHumidity();
  const float temperature = dht.readTemperature();

  if (isnan(humidity) || isnan(temperature)) {
    return false;
  }

  humidity_pct = humidity;
  temperature_c = temperature;
  return true;
}

void writeRelay(bool relay_on) {
  const uint8_t pin_value = (relay_on ^ kRelayActiveLow) ? HIGH : LOW;
  digitalWrite(kRelayPin, pin_value);
}

void writeLed(bool led_on) {
  digitalWrite(kLedPin, led_on ? HIGH : LOW);
}

void printJsonLine(int soil_raw,
                   int soil_pct,
                   int light_raw,
                   int light_pct,
                   bool dry_soil,
                   bool high_temp,
                   bool low_light,
                   bool relay_on,
                   bool led_on) {
  Serial.print(F("{\"device\":\"arduino-greenhouse\""));
  Serial.print(F(",\"uptime_ms\":"));
  Serial.print(millis());
  Serial.print(F(",\"temperature_c\":"));
  Serial.print(last_temperature_c, 1);
  Serial.print(F(",\"humidity_pct\":"));
  Serial.print(last_humidity_pct, 1);
  Serial.print(F(",\"soil_raw\":"));
  Serial.print(soil_raw);
  Serial.print(F(",\"soil_pct\":"));
  Serial.print(soil_pct);
  Serial.print(F(",\"light_raw\":"));
  Serial.print(light_raw);
  Serial.print(F(",\"light_pct\":"));
  Serial.print(light_pct);
  Serial.print(F(",\"dry_soil\":"));
  Serial.print(dry_soil ? 1 : 0);
  Serial.print(F(",\"high_temp\":"));
  Serial.print(high_temp ? 1 : 0);
  Serial.print(F(",\"low_light\":"));
  Serial.print(low_light ? 1 : 0);
  Serial.print(F(",\"relay_on\":"));
  Serial.print(relay_on ? 1 : 0);
  Serial.print(F(",\"led_on\":"));
  Serial.print(led_on ? 1 : 0);
  Serial.println(F("}"));
}

void sampleAndPublish() {
  float temperature_c = last_temperature_c;
  float humidity_pct = last_humidity_pct;
  if (readDht(temperature_c, humidity_pct)) {
    last_temperature_c = temperature_c;
    last_humidity_pct = humidity_pct;
  }

  const int soil_raw = analogRead(kSoilPin);
  const int light_raw = analogRead(kLightPin);

  const int soil_pct = scaleAnalogToPercent(soil_raw, kSoilDryRaw, kSoilWetRaw);
  const int light_pct = scaleAnalogToPercent(light_raw, kLightDarkRaw, kLightBrightRaw);

  const bool dry_soil = soil_pct < kDrySoilThresholdPct;
  const bool high_temp = last_temperature_c > kHighTempThresholdC;
  const bool low_light = light_pct < kLowLightThresholdPct;
  const bool relay_on = dry_soil;
  const bool led_on = dry_soil || high_temp || low_light;

  writeRelay(relay_on);
  writeLed(led_on);
  printJsonLine(soil_raw, soil_pct, light_raw, light_pct, dry_soil, high_temp, low_light, relay_on, led_on);
}

}  // namespace

void setup() {
  pinMode(kRelayPin, OUTPUT);
  pinMode(kLedPin, OUTPUT);
  writeRelay(false);
  writeLed(false);

  Serial.begin(115200);
  dht.begin();

  // Let the USB serial port settle before the first reading is emitted.
  delay(1500);
  sampleAndPublish();
  last_sample_ms = millis();
}

void loop() {
  const unsigned long now = millis();
  if (now - last_sample_ms >= kSampleIntervalMs) {
    last_sample_ms = now;
    sampleAndPublish();
  }
}
