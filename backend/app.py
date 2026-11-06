import math
import os
from flask import Flask, jsonify, request
from flask_cors import CORS

app = Flask(__name__)
origins = os.getenv("FRONTEND_ORIGIN", "http://localhost:5173")
CORS(app, resources={r"/api/*": {"origins": [o.strip() for o in origins.split(",")]}})

MATERIALS = [
    {"id":"silicon","name":"Silicon","formula":"Si","category":"Semiconductor","structure":"Diamond cubic","density":2.329,"melting_point":1414,"band_gap":1.12,"description":"A foundational semiconductor used in integrated circuits and photovoltaic cells."},
    {"id":"graphene","name":"Graphene","formula":"C","category":"Nanomaterial","structure":"2D hexagonal lattice","density":2.267,"melting_point":">3000","band_gap":0.0,"description":"A single layer of carbon atoms arranged in a hexagonal lattice."},
    {"id":"copper","name":"Copper","formula":"Cu","category":"Metal","structure":"Face-centred cubic","density":8.96,"melting_point":1084.6,"band_gap":0.0,"description":"A highly conductive metal widely used in electrical wiring."},
    {"id":"tio2","name":"Titanium dioxide","formula":"TiO₂","category":"Ceramic / Nanomaterial","structure":"Rutile / Anatase","density":4.23,"melting_point":1843,"band_gap":3.0,"description":"A functional oxide used in pigments, photocatalysis and UV protection."},
    {"id":"cnt","name":"Carbon nanotube","formula":"C","category":"Nanomaterial","structure":"Cylindrical graphene sheet","density":1.3,"melting_point":"~3550","band_gap":"Varies","description":"A nanoscale carbon cylinder with exceptional mechanical and electrical properties."}
]

@app.get("/")
def root():
    return jsonify({"name":"MATTERVERSE API","status":"online","docs":"See README.md"})

@app.get("/api/health")
def health():
    return jsonify({"status":"ok","service":"matterverse-api"})

@app.get("/api/materials")
def materials():
    return jsonify({"materials": MATERIALS})

@app.get("/api/materials/<material_id>")
def material_detail(material_id):
    item = next((m for m in MATERIALS if m["id"] == material_id), None)
    if item is None:
        return jsonify({"error":"Material not found"}), 404
    return jsonify(item)

@app.post("/api/compare")
def compare():
    payload = request.get_json(silent=True) or {}
    ids = payload.get("ids", [])
    selected = [m for m in MATERIALS if m["id"] in ids]
    return jsonify({"materials": selected})

@app.post("/api/nano/sphere")
def sphere():
    payload = request.get_json(silent=True) or {}
    try:
        diameter_nm = float(payload.get("diameter_nm", 50))
        density_g_cm3 = float(payload.get("density_g_cm3", 2.267))
        if diameter_nm <= 0 or density_g_cm3 <= 0:
            raise ValueError()
    except (TypeError, ValueError):
        return jsonify({"error":"Diameter and density must be positive numbers."}), 400
    radius_cm = diameter_nm * 1e-7 / 2
    volume_cm3 = (4 / 3) * math.pi * radius_cm ** 3
    mass_g = volume_cm3 * density_g_cm3
    return jsonify({
        "diameter_nm": diameter_nm,
        "density_g_cm3": density_g_cm3,
        "volume_cm3": volume_cm3,
        "mass_g": mass_g,
        "mass_fg": mass_g * 1e15,
        "surface_area_nm2": math.pi * diameter_nm ** 2
    })

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=int(os.getenv("PORT", 5000)), debug=True)
