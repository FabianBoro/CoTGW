# #ECHO is on.
# # app/routers/devices.py
# from fastapi import APIRouter

# router = APIRouter()

# @router.get("/")
# def list_devices():
#     return {"devices": []}
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app import models, schemas
from app.database import get_db
from datetime import datetime

router = APIRouter()

@router.post("/location")
def submit_location(data: schemas.LocationCreate, db: Session = Depends(get_db)):
    # Cek apakah device sudah terdaftar
    device = db.query(models.Device).filter(models.Device.device_id == data.device_id).first()
    if not device:
        raise HTTPException(status_code=404, detail="Device not found")

    location = models.Location(
        device_id = device.id,
        latitude = data.latitude,
        longitude = data.longitude,
        timestamp = data.timestamp
    )
    db.add(location)
    db.commit()
    db.refresh(location)

    return {"status": "ok", "location_id": location.id}
