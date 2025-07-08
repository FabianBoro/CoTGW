# app/routers/cot_endpoint.py

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from datetime import datetime

from app import models, database

from pydantic import BaseModel

from app.cot import build_cot_xml, send_to_tak_server

router = APIRouter()

# Data yang dikirim dari ESP32
class CoTData(BaseModel):
    id: str      # ID unik ESP32 (bisa IMEI, MAC, atau serial)
    lat: float
    lon: float
    ts: datetime = None  # optional, kalau tidak ada pakai now()

@router.post("/")
def receive_cot(data: CoTData, db: Session = Depends(database.get_db)):
    # Cari device, jika belum ada, buat
    device = db.query(models.Device).filter(models.Device.id == data.id).first()
    if not device:
        device = models.Device(id=data.id, last_seen=datetime.utcnow())
        db.add(device)
    else:
        device.last_seen = datetime.utcnow()

    # Simpan lokasi baru
    location = models.Location(
        device_id=data.id,
        lat=data.lat,
        lon=data.lon,
        timestamp=data.ts or datetime.utcnow()
    )
    db.add(location)
    db.commit()

    cot_xml = build_cot_xml(uid=f"{data.id}.gps", lat=data.lat, lon=data.lon)
    success = send_to_tak_server(cot_xml)
    # return {"status": "received", "device": data.id}
    return {"status": "sent" if success else "failed", "device": data.id}
