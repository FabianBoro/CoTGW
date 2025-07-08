#ECHO is on.
# app/database.py

from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# Lokasi database SQLite
DATABASE_URL = "sqlite:///./cotgw.db"

# Buat engine koneksi
engine = create_engine(
    DATABASE_URL, connect_args={"check_same_thread": False}
)

# Factory untuk session
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Base class untuk semua model
Base = declarative_base()

# Dependency untuk dapatkan session di route
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
