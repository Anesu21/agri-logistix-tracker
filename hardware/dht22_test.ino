/* Standalone DHT22 check: DATA -> D2, VCC -> 5V, GND -> GND. */
#include <DHT.h>
#define DHT_PIN 2
#define DHT_TYPE DHT22
DHT dht(DHT_PIN, DHT_TYPE);

void setup() {
  Serial.begin(9600);
  dht.begin();
  Serial.println(F("DHT22 test ready"));
}

void loop() {
  delay(2000);
  const float humidity = dht.readHumidity();
  const float temperature = dht.readTemperature();
  if (isnan(humidity) || isnan(temperature)) {
    Serial.println(F("ERROR: DHT22 read failed"));
    return;
  }
  Serial.print(F("Humidity: "));
  Serial.print(humidity, 1);
  Serial.print(F(" % | Temperature: "));
  Serial.print(temperature, 1);
  Serial.println(F(" C"));
}
