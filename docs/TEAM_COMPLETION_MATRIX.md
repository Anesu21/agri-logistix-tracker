# Agri-Logistix Team Completion Matrix

Audit basis: GitHub `main` branch and visible commit/issue history checked on 5 November 2026. This document distinguishes repository evidence from physical testing; an open issue is not proof that no work was done.

## Hardware issues and assigned members

| GitHub issue | Assignee | Evidence already in repository | Completion added in this update | Still needs real-world confirmation |
|---|---|---|---|---|
| [#5 Arduino Uno main firmware](https://github.com/Anesu21/agri-logistix-tracker/issues/5) | `@n02535292j-bit` | DHT22 and door-switch test sketches existed, but no integrated main sketch was present at audit time. | Added `hardware/arduino_main.ino`: reads DHT22 and reed switch, emits one JSON line every 2 seconds at 9600 baud, and updates the optional OLED. | Compile/upload on the actual Uno; verify switch contact polarity, sensor readings and Node-RED serial connection. |
| [#6 DHT22 wiring and calibration](https://github.com/Anesu21/agri-logistix-tracker/issues/6) | `@NUSTAno` | DHT22 test sketch and `docs/screenshots/DHT22 wiring .jpeg` existed. Existing issue comment documents ventilation and thermal isolation. | Prepared a clean standalone sketch at `hardware/dht22_test.ino`; integrated firmware also reads DHT22 on D2 and sends JSON output. | Verify wiring/photo, compare readings against a reference thermometer/hygrometer, and record calibration results. |
| [#8 LCD/OLED display integration](https://github.com/Anesu21/agri-logistix-tracker/issues/8) | `@debug-t16` | Display sketch was committed by `debug-t16`; PR #12 was closed unmerged, but the display code is present on `main` in the repository history. | Prepared a clean standalone sketch at `hardware/screen_display.ino`; replaced hard-coded demo values with live DHT22 and door readings. | Compile and test on the actual OLED; verify the physical screen photo is current and readable. |
| [#10 3D enclosure design](https://github.com/Anesu21/agri-logistix-tracker/issues/10) | `@Malvin-15` | No enclosure CAD/STL deliverables were present at audit time. | Added parametric OpenSCAD source. Exported `enclosure.stl`, `enclosure_lid.stl` and a CAD preview PNG as downloadable artifacts; the binary exports still need to be uploaded to the repository. | Check actual Uno, breadboard, OLED, connector and sensor dimensions; test fit and print before calling it production-ready. |
| [#11 Node-RED dashboard](https://github.com/Anesu21/agri-logistix-tracker/issues/11) | `@n02531364l-dev` | `docs/screenshots/nodered.png` existed; an exported flow file was absent at audit time. | Added `nodered/flow.json` with serial input, JSON parsing, temperature/humidity/door widgets and alert logic, plus a clearly labelled manual demo inject. | Import into the team's Node-RED installation, install the listed dashboard/serial nodes, select the correct serial port and verify with live Arduino data. |

## Other visible contributions

- `debug-t16`: commits include DHT22 and LCD/OLED implementation work on 5 November 2026.
- `NUSTAno`: commits include Gazebo farm world/autonomous-driver scaffolding and a sprint file. Gazebo operation is not claimed as part of the demonstrated Node-RED prototype.
- `n02531364l-dev`: commits include Ezra's sprint document and README updates; the Node-RED flow export was missing before this update.
- `Malvin-15`: a sprint file was created and later deleted in the visible history; no enclosure CAD was present before this update.
- Sprint documents for Anotida Chimhandamba, Ezra Kufazvineyi and Tonderai Tevera were present. A current Rasheed sprint file was not found in the repository tree.
- The issue list also contains closed issues #7 (door switch logic) and #9 (power management). Closure status is preserved; it is not treated as proof of a full physical validation.

## Important status rule

Files added to GitHub demonstrate that a software/design deliverable is present. They do not prove hardware has been assembled, code compiled on a board, a display physically tested, or a 3D enclosure successfully printed. Keep issues open until the evidence in the final column has been checked by the team.
