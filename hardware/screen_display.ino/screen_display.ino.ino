#include <Wire.h>
#include <Adafruit_GFX.h>
#include <Adafruit_SSD1306.h>

#define SCREEN_WIDTH 128
#define SCREEN_HEIGHT 64

Adafruit_SSD1306 display(SCREEN_WIDTH, SCREEN_HEIGHT, &Wire, -1);

float temp = 12.5;
bool doorOpen = false;

void setup() {
  if (!display.begin(SSD1306_SWITCHCAPVCC, 0x3C)) {
    for (;;); // Loop forever if initialization fails
  }
  display.clearDisplay();
  display.setTextColor(SSD1306_WHITE);
  display.setTextSize(1);
}

void loop() {
  display.clearDisplay();
  display.setCursor(0, 0);
  
  display.print("Temp: ");
  display.print(temp, 1);
  display.println("C");
  
  display.print("Door: ");
  display.println(doorOpen ? "Open" : "Closed");
  
  display.display();
  
  // Refresh every 2 seconds
  delay(2000);
}