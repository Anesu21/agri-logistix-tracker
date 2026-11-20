# Agri-Logistix Node-RED Dashboard

This folder contains the Node-RED dashboard flow for
monitoring simulated or physical transport sensor readings.

## Setup

1. Install Node-RED and the dashboard/serial packages used by the flow.
2. Open the Node-RED editor.
3. Import `flow.json`.
4. Configure the serial port for your environment.
   The original Arduino setup uses COM6 at 9600 baud.
5. Deploy the flow and open the dashboard.

## Arduino serial format

The physical Arduino prototype sends one JSON object per line:

{"temperature":25.4,"humidity":65.0,"door":"CLOSED"}

The flow routes temperature, humidity and door readings
to dashboard widgets.

A battery gauge is also included, but the current Arduino
firmware does not send battery readings.

## Temperature alerts

- Below 5°C: TOO COLD
- 5°C through 12°C: NORMAL
- Above 12°C: TOO HOT

These thresholds match the ROS2 alert node.

## Notes

The Arduino serial port must not be open in another
application while Node-RED is reading it.
