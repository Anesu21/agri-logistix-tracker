# Power Management — Agri-Logistix Smart Tracker

## 1. Scope and current prototype

This guide describes power for the current Arduino Uno demonstration. `hardware/arduino_main.ino` uses a DHT22 on D2, a magnetic door switch on D3, and an optional SSD1306 I2C OLED on A4/A5. The current build is not the ESP32/LoRa/GPS/solar architecture mentioned in an earlier draft; those are future options, not completed hardware.

## 2. Suitable power options

### USB power bank (recommended for demonstrations)
- Use a reputable regulated 5 V USB power bank and a suitable cable connected to the Uno USB socket.
- Check auto-shutoff behaviour because some power banks switch off when the load is very low.

### 9 V battery or external supply
- A 9 V source may be connected to the Uno DC barrel jack or VIN only within the board's input-voltage limits (typically 7–12 V for a classic Uno; check the exact board revision).
- The onboard regulator dissipates excess voltage as heat. A small PP3 9 V battery is generally not ideal for long-duration operation.
- Never connect 9 V directly to the DHT22, OLED, or the Uno 5 V pin.

### Computer USB
- USB power is suitable for bench development and serial monitoring. Avoid conflicting simultaneous supplies; follow the board's power-selection guidance.

## 3. 5 V and GND wiring

Use the Uno's regulated 5 V and GND pins as the common low-voltage rails:

| Module | Supply | Signal |
|---|---|---|
| DHT22 breakout | VCC → 5V; GND → GND | DATA → D2 |
| Magnetic reed switch | One contact → GND; other → D3 | Firmware uses `INPUT_PULLUP`; verify switch polarity |
| SSD1306 I2C OLED (optional) | VCC → module-rated supply (confirm 5V tolerance); GND → GND | SDA → A4; SCL → A5 |

All modules must share a common ground. For a bare DHT22 (not a breakout), fit the required DATA pull-up resistor, commonly 4.7–10 kΩ, following the sensor datasheet. Confirm the OLED breakout's voltage tolerance before connecting 5 V.

```text
USB 5 V power bank
        |
   Arduino Uno
   5V rail  ---------------- DHT22 VCC
      |                      OLED VCC (if 5V-tolerant)
   GND rail  ---------------- DHT22 GND / OLED GND
      |                      Reed switch contact
   D2 ----------------------- DHT22 DATA
   D3 ----------------------- Reed switch contact
   A4 ----------------------- OLED SDA (optional)
   A5 ----------------------- OLED SCL (optional)
```

## 4. Power-saving considerations

The current Uno firmware samples every 2 seconds and sends serial JSON at 9600 baud. It does not currently implement deep sleep, scheduled wake-up, or a low-power radio duty cycle. For a future battery deployment, measure the complete system's current in normal operation and idle states before estimating runtime. A lower-power controller, switched sensor power, and communications duty-cycling are future design options, not implemented features.

## 5. Battery-life calculation

A first-order estimate is:

`runtime (hours) ≈ usable battery capacity (mAh) ÷ measured average current (mA)`

Use usable capacity at the actual load and account for conversion efficiency. Record supply voltage, average current, sampling interval, and communications activity. No validated battery-runtime result is currently available for this prototype.

## 6. Safety and validation checklist

- [ ] Confirm the exact Uno revision and input-voltage limits.
- [ ] Check polarity and voltage before connecting the supply.
- [ ] Confirm every peripheral is compatible with its supply voltage.
- [ ] Check for shorts between 5V and GND before powering up.
- [ ] Measure the 5V rail under the complete sensor/display load.
- [ ] Measure average current during normal operation and startup.
- [ ] Test the power bank for unexpected auto-shutoff.
- [ ] Record a real discharge test before publishing runtime claims.

## 7. Current status and limitations

This guide documents safe power options and wiring for the current Uno prototype. It does not claim that a battery pack, solar charger, sleep mode, or multi-day field runtime has been implemented or tested. Complete the checklist with the physical build and add measured results before treating the power subsystem as field-validated.

## Related files
- `hardware/arduino_main.ino`
- `docs/HARDWARE_VALIDATION_CHECKLIST.md`
- GitHub issue #9 — Power Management
