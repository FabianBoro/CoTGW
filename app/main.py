# app/main.py

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.routers import devices, cot_endpoint

app = FastAPI(title="CoT Gateway Web Admin")

# CORS Middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],          # Terbuka untuk semua origin
    allow_credentials=False,      # HARUS False kalau pakai "*"
    allow_methods=["*"],
    allow_headers=["*"],
)

# Include routers
app.include_router(cot_endpoint.router, prefix="/cot", tags=["CoT Data"])
app.include_router(devices.router, prefix="/devices", tags=["Device Admin"])

# Sanity check endpoint
@app.get("/")
def root():
    return {"message": "CoT Gateway is running."}
