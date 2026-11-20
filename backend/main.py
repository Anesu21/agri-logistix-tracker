from fastapi import FastAPI
from datetime import datetime
from typing import Optional

app = FastAPI(
    title="Agri-Logistix API",
    description="Fleet monitoring API for perishable goods transport",
    version="1.0.0"
)

# Temporary in-memory storage
vehicle_data = {}


@app.get("/")
def home():
    return {
        "message": "Agri-Logistix API is running",
        "status": "online"
    }


@app.get("/health")
def health():
    return {"status": "healthy"}


@app.post("/api/vehicle/{vehicle_id}/readings")
def receive_readings(vehicle_id: str, data: dict):

    vehicle_data[vehicle_id] = {
        "data": data,
        "received_at": datetime.now().isoformat()
    }

    return {
        "message": "Vehicle readings received successfully",
        "vehicle_id": vehicle_id,
        "status": "success"
    }


@app.get("/api/vehicle/{vehicle_id}")
def get_vehicle(vehicle_id: str):

    if vehicle_id not in vehicle_data:
        return {
            "message": "Vehicle not found",
            "vehicle_id": vehicle_id
        }

    return vehicle_data[vehicle_id]


@app.get("/api/vehicles")
def get_all_vehicles():
    return vehicle_data
