/*
 Agri-Logistix Smart Tracker enclosure - parametric OpenSCAD source
 Units: mm. Designed as a starting fit for Arduino Uno + small breadboard.
 Check actual board, cable and OLED dimensions before fabrication.
 Export BASE and LID separately by setting part="base" or part="lid".
*/
$fn = 48;
part = "base"; // "base", "lid", or "assembly"
L = 200; W = 140; H = 50;
wall = 3; floor_t = 3; corner_r = 6;
lid_t = 3; lid_skirt_h = 7; lid_clearance = 0.35;

module rounded_prism(x,y,z,r) {
  hull() {
    translate([r,r,0]) cylinder(h=z,r=r);
    translate([x-r,r,0]) cylinder(h=z,r=r);
    translate([r,y-r,0]) cylinder(h=z,r=r);
    translate([x-r,y-r,0]) cylinder(h=z,r=r);
  }
}

module base_shell() {
  difference() {
    rounded_prism(L,W,H,corner_r);
    translate([wall,wall,floor_t])
      rounded_prism(L-2*wall,W-2*wall,H-floor_t+0.2,max(1,corner_r-wall));
    // USB access opening on the left wall
    translate([-0.2,61,18]) cube([wall+0.4,18,10]);
    // Door-switch cable opening on the right wall
    translate([L-wall-0.2,18,15]) rotate([0,90,0]) cylinder(h=wall+0.4,d=8);
    // Ventilation slots on the front wall for ambient-air exchange
    for (x=[130:12:178]) translate([x,-0.2,25]) cube([5,wall+0.4,12]);
  }
  // Lid screw bosses; pilot holes accept self-tapping M3 screws.
  for (x=[9,L-9]) for (y=[9,W-9]) {
    translate([x,y,floor_t]) difference() {
      cylinder(h=10,d=8);
      translate([0,0,-0.1]) cylinder(h=10.2,d=2.6);
    }
  }
  // Arduino Uno mounting standoffs (nominal 58 x 49 mm hole spacing)
  for (x=[25,83]) for (y=[43,92]) {
    translate([x,y,floor_t]) difference() {
      cylinder(h=7,d=8);
      translate([0,0,-0.1]) cylinder(h=7.2,d=3.2);
    }
  }
  // Low tie-down tabs for securing a breadboard with cable ties
  for (x=[105,178]) for (y=[38,96]) {
    translate([x,y,floor_t]) difference() {
      cube([9,7,2],center=true);
      cube([3,3,2.2],center=true);
    }
  }
}

module lid() {
  difference() {
    union() {
      rounded_prism(L,W,lid_t,corner_r);
      // locating lip on the underside
      translate([wall+lid_clearance,wall+lid_clearance,-lid_skirt_h])
        difference() {
          rounded_prism(L-2*(wall+lid_clearance),W-2*(wall+lid_clearance),lid_skirt_h,corner_r-wall);
          translate([wall,wall,-0.1])
            rounded_prism(L-2*(2*wall+lid_clearance),W-2*(2*wall+lid_clearance),lid_skirt_h+0.2,max(1,corner_r-2*wall));
        }
    }
    // OLED window on lid (nominal 30 x 14 mm aperture)
    translate([119,91,-0.2]) cube([34,18,lid_t+0.4]);
    // Four lid fastener clearance holes
    for (x=[9,L-9]) for (y=[9,W-9])
      translate([x,y,-0.2]) cylinder(h=lid_t+0.4,d=3.4);
    // DHT22 airflow perforations near the sensor end
    for (x=[164:7:185]) for (y=[15:7:36])
      translate([x,y,-0.2]) cylinder(h=lid_t+0.4,d=3);
  }
}

if (part == "base") base_shell();
else if (part == "lid") lid();
else {
  base_shell();
  translate([L+12,0,H-lid_t]) lid();
}
