# Power Management - Agri-Logistix Tracker

## Goal
Extend battery life for field-deployed IoT tracker nodes using sleep modes, solar charging, and efficient transmission.

## Current Problem
- Node drains battery in < 48h with continuous GPS + LoRa
- No sleep scheduling
- No solar charge monitoring

## Solution

### 1. Sleep Modes (ESP32)
- Deep Sleep: 10uA - use between readings
- Light Sleep: 0.8mA - use for short waits
- Wake every 15 min to read sensors + transmit

### 2. Solar Charging
- 6V 3W solar panel + TP4056 charger
- Monitor battery voltage via ADC
- Log charge/discharge cycles

### 3. Transmission Strategy
- Batch readings, send every 15 min (not continuous)
- Use LoRa SF7 for low power when close to gateway
- Increase SF only when signal weak

### 4. Power Budget
| Component | Active | Sleep |
| --- | --- | --- |
| ESP32 | 160mA | 10uA |
| GPS NEO-6M | 45mA | 0mA (off) |
| LoRa SX1276 | 120mA TX | 0.2uA |
| Sensors | 5mA | 0mA |

Target: 14+ days on 18650 3000mAh + solar

## Tasks
- [ ] Implement deep sleep wake timer
- [ ] Add battery voltage reading
- [ ] Add solar charge status
- [ ] Test 7-day field run

## Related
Closes #9
