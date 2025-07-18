# app/routers/cot_endpoint.py

from fastapi import APIRouter, Depends, HTTPException, Request
from sqlalchemy.orm import Session
from datetime import datetime

from app import models, database

from pydantic import BaseModel

# from app.cot import build_cot_xml1, send_to_tak_server1
from app.cot.build_cot_xml import build_cot_xml
from app.cot.send_to_tak_server import send_to_tak_server

router = APIRouter()

# Data yang dikirim dari ESP32
class CoTData(BaseModel):
    id: str      # ID unik ESP32 (bisa IMEI, MAC, atau serial)
    lat: float
    lon: float
    ts: datetime = None  # optional, kalau tidak ada pakai now()

@router.post("/")
async def receive_cot(
    request: Request,
    data: CoTData,
    db: Session = Depends(database.get_db)
):
    client_verify = request.headers.get("x-ssl-client-verify")
    client_dn = request.headers.get("x-ssl-client-dn")

    if client_verify != "SUCCESS":
        raise HTTPException(status_code=401, detail="Client certificate not valid")

    # Misalnya hanya client dengan CN=esp32-001 yang diizinkan
    if not client_dn or "CN=esp32-001" not in client_dn:
        raise HTTPException(status_code=403, detail="Unauthorized device")
    # Cari device, jika belum ada, buat
    device = db.query(models.Device).filter(models.Device.id == data.id).first()
    if not device:
        device = models.Device(id=data.id, last_seen=datetime.utcnow(), callsign=data.id)
        db.add(device)
    else:
        device.last_seen = datetime.utcnow()
        if not device.callsign:
            device.callsign = data.id  # Amankan agar tidak None

    # Simpan lokasi baru
    location = models.Location(
        device_id=data.id,
        lat=data.lat,
        lon=data.lon,
        timestamp=data.ts or datetime.utcnow()
    )
    db.add(location)
    db.commit()
    callsign = device.callsign or data.id
    cot_xml = build_cot_xml(
        uid=f"{data.id}.gps",
        lat=data.lat,
        lon=data.lon,
        callsign=callsign
    )
    success = send_to_tak_server(cot_xml)
    print("[DEBUG] Sending XML to TAK Server:")
    print(cot_xml)
    print("\n[INFO] Mengirim ke TAK Server...")
    print("Sukses kirim?" , success)


    # return {"status": "received", "device": data.id}
    return {
        "status": "sent" if success else "failed",
        "device": data.id,
        "callsign": device.callsign
    }
