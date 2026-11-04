import math
from pathlib import Path
import xml.etree.ElementTree as ET

sdf = ET.Element("sdf", version="1.9")
world = ET.SubElement(sdf, "world", name="agri_logistix_farm")

def add(parent, tag, text=None, **attrs):
    el = ET.SubElement(parent, tag, attrs)
    if text is not None:
        el.text = str(text)
    return el

def box(name, x, y, z, sx, sy, sz, color, static=True):
    m = add(world, "model", name=name)
    add(m, "static", str(static).lower())
    add(m, "pose", f"{x} {y} {z} 0 0 0")
    link = add(m, "link", name="body")
    for kind in ("visual", "collision"):
        obj = add(link, kind, name=kind)
        geom = add(obj, "geometry")
        add(add(geom, "box"), "size", f"{sx} {sy} {sz}")
        if kind == "visual":
            mat = add(obj, "material")
            add(mat, "ambient", color)
            add(mat, "diffuse", color)

# Lighting
light = add(world, "light", name="sun", type="directional")
add(light, "cast_shadows", "true")
add(light, "pose", "0 0 30 0 0 0")
add(light, "direction", "-0.4 0.2 -1")
add(light, "diffuse", "0.9 0.9 0.85 1")
add(light, "specular", "0.2 0.2 0.2 1")

# Ground and road network
box("farm_ground", 0, 0, -0.15, 70, 60, 0.3,
    "0.48 0.36 0.22 1")
box("main_road", 0, 0, 0.015, 70, 5, 0.03,
    "0.22 0.22 0.20 1")
box("farm_access_road", 12, 10, 0.02, 5, 24, 0.04,
    "0.25 0.25 0.23 1")

# Crop rows: green crop blocks on both sides of the main road
for row in range(8):
    x = -26 + row * 3
    if abs(x) < 4:
        continue
    for side in (-1, 1):
        y = side * 13
        box(f"crop_row_{row}_{side}", x, y, 0.45,
            0.65, 17, 0.9, "0.16 0.42 0.10 1")

# Warehouse: floor, walls and roof
box("warehouse_floor", 23, 12, 0.12, 12, 10, 0.24,
    "0.55 0.56 0.57 1")
box("warehouse_back", 23, 17, 2, 12, 0.25, 4,
    "0.72 0.74 0.76 1")
box("warehouse_left", 17, 12, 2, 0.25, 10, 4,
    "0.65 0.67 0.69 1")
box("warehouse_right", 29, 12, 2, 0.25, 10, 4,
    "0.65 0.67 0.69 1")
box("warehouse_roof", 23, 12, 4.1, 12, 10, 0.25,
    "0.18 0.25 0.32 1")

# Loading and delivery zones
box("loading_pad", 14, 3.5, 0.06, 8, 4, 0.12,
    "0.75 0.65 0.22 1")
box("delivery_pad", -19, 0, 0.06, 8, 6, 0.12,
    "0.20 0.45 0.72 1")

# Cargo pallets and produce crates
for i in range(3):
    box(f"pallet_{i}", 20 + i * 2, 7, 0.2, 1.4, 1.2, 0.25,
        "0.40 0.23 0.10 1")
    box(f"produce_crate_{i}", 20 + i * 2, 7, 0.65, 1.1, 0.9, 0.65,
        "0.76 0.30 0.08 1")

# Simple transport vehicle. Its chassis is one physical body.
m = add(world, "model", name="agri_transport_vehicle")
add(m, "static", "false")
add(m, "pose", "0 -1 0.65 0 0 0")
link = add(m, "link", name="base_link")
inertial = add(link, "inertial")
add(inertial, "mass", "80")
inertia = add(inertial, "inertia")
for key, val in (("ixx", 15), ("iyy", 30), ("izz", 35),
                 ("ixy", 0), ("ixz", 0), ("iyz", 0)):
    add(inertia, key, val)

collision = add(link, "collision", name="chassis_collision")
geom = add(collision, "geometry")
add(add(geom, "box"), "size", "2.2 1.3 0.5")
visuals = [
    ("chassis", "0 0 0", "2.2 1.3 0.5", "0.12 0.30 0.72 1"),
    ("cabin", "-0.55 0 0.55", "0.85 1.15 0.55", "0.18 0.65 0.80 1"),
    ("cargo", "0.55 0 0.43", "0.8 1.0 0.35", "0.80 0.42 0.10 1"),
    ("wheel_fl", "-0.65 0.72 -0.20", "0.42 0.18 0.42", "0.08 0.08 0.08 1"),
    ("wheel_fr", "-0.65 -0.72 -0.20", "0.42 0.18 0.42", "0.08 0.08 0.08 1"),
    ("wheel_rl", "0.70 0.72 -0.20", "0.48 0.18 0.48", "0.08 0.08 0.08 1"),
    ("wheel_rr", "0.70 -0.72 -0.20", "0.48 0.18 0.48", "0.08 0.08 0.08 1"),
]
for name, pose, size, color in visuals:
    v = add(link, "visual", name=name)
    add(v, "pose", pose)
    g = add(v, "geometry")
    add(add(g, "box"), "size", size)
    mat = add(v, "material")
    add(mat, "ambient", color)
    add(mat, "diffuse", color)

# Physics and scene
physics = add(world, "physics", name="physics", type="ignored")
add(physics, "max_step_size", "0.004")
add(physics, "real_time_factor", "1")
add(physics, "real_time_update_rate", "250")

scene = add(world, "scene")
add(scene, "ambient", "0.55 0.55 0.55 1")
add(scene, "background", "0.70 0.80 0.90 1")
add(scene, "shadows", "true")

path = Path.home() / "agri_logistix_sim/worlds/agri_farm.sdf"
ET.indent(sdf, space="  ")
ET.ElementTree(sdf).write(path, encoding="utf-8", xml_declaration=True)
print(f"World created: {path}")
