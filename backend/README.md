# Agri-Logistix Backend

Prototype REST API implemented using FastAPI.

## Setup

From this directory:

python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
uvicorn main:app --reload

## API endpoints

- GET / - API status
- GET /health - Health check
- POST /api/vehicle/{vehicle_id}/readings - Submit sensor readings
- GET /api/vehicle/{vehicle_id} - Read a vehicle's latest data
- GET /api/vehicles - List recorded vehicles

## Limitations

Readings are stored in memory and are lost when
the server restarts.

This is a prototype, not a production backend.
