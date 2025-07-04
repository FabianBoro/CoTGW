#ECHO is on.
# app/main.py
from fastapi import FastAPI
from app.routers import devices, cot_endpoint

app = FastAPI(title="CoT Gateway Web Admin")

app.include_router(cot_endpoint.router, prefix="/cot", tags=["CoT Data"])
app.include_router(devices.router, prefix="/devices", tags=["Device Admin"])