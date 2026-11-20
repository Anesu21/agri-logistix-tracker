/*
 * Agri-Logistix OLED integration test.
 * DHT22 data D2, door reed switch D3 (closed contact pulls to GND),
 * SSD1306 I2C OLED at 0x3C (SDA=A4, SCL=A5).
 * Libraries: DHT sensor library, Adafruit Unified Sensor,
 * Adafruit GFX Library, Adafruit SSD1306.
 */
#include <DHT.h>
#include <Wire.h>
#include <Adafruit_GFX.h>
#include <Adafruit_SSD1306.h>

#define DHT_PIN 2
#define DHT_TYPE DHT22
#define DOOR_PIN 3
#define SCREEN_WIDTH 128
#define SCREEN_HEIGHT 64
DHT dht(DHT_PIN, DHT_TYPE);
Adafruit_SSD1306 display(SCREEN_WIDTH, SCREEN_HEIGHT, &Wire, -1);

void setup() {
  pinMode(DOOR_PIN, INPUT_PULLUP);
  Serial.begin(9600);
  dht.begin();
  if (!display.begin(SSD1306_SWITCHCAPVCC, 0x3C)) {
    Serial.println(F("OLED not detected; check I2C wiring/address"));
    while (true) delay(1000);
  }
  display.clearDisplay();
  display.setTextColor(SSD1306_WHITE);
  display.display();
}

void loop() {
  const float humidity = dht.readHumidity();
  const float temperature = dht.readTemperature();
  const bool doorOpen = digitalRead(DOOR_PIN) == HIGH;
  display.clearDisplay();
  display.setTextSize(1);
  display.setCursor(0, 0);
  display.println(F("AGRI-LOGISTIX"));
  display.drawLine(0, 11, 127, 11, SSD1306_WHITE);
  display.setCursor(0, 17);
  if (isnan(humidity) || isnan(temperature)) {
    display.println(F("DHT22 read error"));
  } else {
    display.print(F("Temp: ")); display.print(temperature, 1); display.println(F(" C"));
    display.print(F("Humidity: ")); display.print(humidity, 1); display.println(F(" %"));
  }
  display.print(F("Door: ")); display.println(doorOpen ? F("OPEN") : F("CLOSED"));
  display.display();
  delay(2000);
}
