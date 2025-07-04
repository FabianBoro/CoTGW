#ECHO is on.
# app/routers/cot_endpoint.py
from fastapi import APIRouter, Request
from pydantic import BaseModel

router = APIRouter()

class CoTData(BaseModel):
    id: str
    lat: float
    lon: float
    ts: str  # timestamp

@router.post("/")
async def receive_cot(data: CoTData):
    # TODO: kirim ke TAK Server di sini
    return {"status": "received", "id": data.id}
