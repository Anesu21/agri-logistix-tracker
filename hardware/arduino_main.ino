/*
 * Agri-Logistix Smart Tracker - integrated Arduino Uno firmware
 * Hardware: Arduino Uno, DHT22 (D2), magnetic reed switch (D3),
 * optional 128x64 I2C SSD1306 OLED (0x3C, SDA=A4, SCL=A5).
 *
 * Reed-switch assumption: the contact is CLOSED when the door is shut
 * and connects D3 to GND. With INPUT_PULLUP, LOW = closed, HIGH = open.
 * Change doorIsOpen() if your switch is wired the opposite way.
 *
 * Libraries: DHT sensor library (Adafruit), Adafruit Unified Sensor,
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
#define OLED_ADDRESS 0x3C
#define SAMPLE_INTERVAL_MS 2000UL

DHT dht(DHT_PIN, DHT_TYPE);
Adafruit_SSD1306 display(SCREEN_WIDTH, SCREEN_HEIGHT, &Wire, -1);
bool oledReady = false;
unsigned long lastSample = 0;

bool doorIsOpen() {
  return digitalRead(DOOR_PIN) == HIGH;
}

void updateDisplay(float temperature, float humidity, bool doorOpen, bool valid) {
  if (!oledReady) return;
  display.clearDisplay();
  display.setTextColor(SSD1306_WHITE);
  display.setTextSize(1);
  display.setCursor(0, 0);
  display.println(F("AGRI-LOGISTIX"));
  display.drawLine(0, 11, 127, 11, SSD1306_WHITE);
  display.setCursor(0, 17);
  if (valid) {
    display.print(F("Temp: "));
    display.print(temperature, 1);
    display.println(F(" C"));
    display.print(F("Humidity: "));
    display.print(humidity, 1);
    display.println(F(" %"));
  } else {
    display.println(F("DHT22 read error"));
  }
  display.print(F("Door: "));
  display.println(doorOpen ? F("OPEN") : F("CLOSED"));
  display.setCursor(0, 53);
  display.println((valid && temperature >= 5.0 && temperature <= 12.0 && !doorOpen) ? F("STATUS: NORMAL") : F("STATUS: CHECK"));
  display.display();
}

void setup() {
  pinMode(DOOR_PIN, INPUT_PULLUP);
  Serial.begin(9600);
  dht.begin();
  oledReady = display.begin(SSD1306_SWITCHCAPVCC, OLED_ADDRESS);
  if (oledReady) {
    display.clearDisplay();
    display.setTextColor(SSD1306_WHITE);
    display.setTextSize(1);
    display.setCursor(0, 0);
    display.println(F("Agri-Logistix boot"));
    display.display();
  }
  Serial.println(F("{\"status\":\"started\",\"baud\":9600}"));
}

void loop() {
  const unsigned long now = millis();
  if (now - lastSample < SAMPLE_INTERVAL_MS) return;
  lastSample = now;

  const float humidity = dht.readHumidity();
  const float temperature = dht.readTemperature();
  const bool valid = !isnan(humidity) && !isnan(temperature);
  const bool doorOpen = doorIsOpen();

  // One JSON object per line for Node-RED's Serial In + JSON nodes.
  Serial.print(F("{\"temp\":"));
  if (valid) Serial.print(temperature, 1); else Serial.print(F("null"));
  Serial.print(F(",\"humidity\":"));
  if (valid) Serial.print(humidity, 1); else Serial.print(F("null"));
  Serial.print(F(",\"door\":\""));
  Serial.print(doorOpen ? F("OPEN") : F("CLOSED"));
  Serial.print(F("\",\"sensor_ok\":"));
  Serial.print(valid ? F("true") : F("false"));
  Serial.println(F("}"));

  updateDisplay(temperature, humidity, doorOpen, valid);
}
