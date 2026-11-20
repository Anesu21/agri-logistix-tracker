# Hardware Bring-up and Validation Checklist

## Pin and wiring reference

| Component | Arduino Uno connection | Notes |
|---|---|---|
| DHT22 VCC | 5V | Use the correct module wiring; a bare sensor may require a pull-up resistor on DATA. |
| DHT22 GND | GND | Common ground. |
| DHT22 DATA | D2 | Firmware uses DHT22, not DHT11. |
| Magnetic reed switch | D3 and GND | Firmware assumes the contact is closed when the door is shut. `INPUT_PULLUP` makes LOW = closed and HIGH = open. Verify the actual switch type before use. |
| SSD1306 OLED VCC/GND | 5V/GND (check module rating) | Confirm module voltage rating. |
| SSD1306 SDA/SCL | A4/A5 | I2C address defaults to 0x3C. |

## Software setup

1. Install Arduino IDE.
2. Install `DHT sensor library` by Adafruit and `Adafruit Unified Sensor`.
3. Install `Adafruit GFX Library` and `Adafruit SSD1306` for the OLED.
4. Open `hardware/arduino_main.ino`, select Arduino Uno and the correct COM port, then compile and upload.
5. Open Serial Monitor at 9600 baud. Expect one JSON object per line, approximately every 2 seconds.
6. Import `nodered/flow.json` into Node-RED. Install `node-red-node-serialport` and `node-red-dashboard` if they are not already installed. Edit the serial-port configuration from `COM3` to the actual port (for example, `/dev/ttyACM0` on many Linux systems).
7. Test the manual demo inject separately from live serial readings; do not present injected sample data as physical sensor data.

## Acceptance checks to record

- [ ] DHT22 temperature and humidity readings are plausible and stable.
- [ ] Door switch reports CLOSED with the door shut and OPEN when opened.
- [ ] OLED shows live readings and door state (if fitted).
- [ ] Node-RED temperature gauge, humidity, door state and alert indicator update from live serial data.
- [ ] Alerts activate when temperature is above 12 °C or below 5 °C, or when the door is OPEN; sensor errors are visible.
- [ ] Photograph the assembled wiring and powered display; save genuine photos under `docs/screenshots/`.
- [ ] Confirm enclosure clearances against the actual components before printing.
