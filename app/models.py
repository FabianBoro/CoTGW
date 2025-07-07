#ECHO is on.
from sqlalchemy import Column, Integer, String, Float, ForeignKey, DateTime
from sqlalchemy.orm import relationship
from datetime import datetime

from app.database import Base

class Device(Base):
    __tablename__ ="devices"

    id = Column(String, primary_key=True, index=True)
    device_id = Column(String, unique=True, index=True)
    name = Column(String, default="Unnamed Device")
    last_seen = Column(DateTime, default=datetime.utcnow)

    #relasi dengan loc
    locations = relationship("Location", back_populates="device")

class Location(Base):
    __tablename__ = "locations"

    id = Column(Integer, primary_key=True, index=True)
    device_id = Column(String, ForeignKey("devices.id"))
    lat = Column(Float, nullable=False)
    lon = Column(Float, nullable=False)
    timestamp = Column(DateTime, default=datetime.utcnow)

    #relationship kembali ke device
    device = relationship("Device", back_populates="locations")