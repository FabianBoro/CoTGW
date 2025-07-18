# init_db.py
from app.database import Base, engine
from app import models  # Ini penting: agar Base tahu model apa yang harus dibuat

print("Membuat tabel database...")
Base.metadata.create_all(bind=engine)
print("Selesai.")
