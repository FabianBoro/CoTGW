from pydantic import BaseModel
from datetime import datetime

class LocationCreate(BaseModel):
    device_id: str
    latitude: float
    longitude: float
    timestamp: datetime
