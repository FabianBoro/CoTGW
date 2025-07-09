# 🛰️ CoT Gateway Web Admin

Web admin berbasis FastAPI untuk menerima data koordinat dari ESP32 via HTTPS dan meneruskannya ke TAK Server dalam format CoT (Cursor on Target).

## 📌 Fitur

- Menerima koordinat (`lat`, `lon`) dari ESP32 dengan HTTPS (EC25)
- Validasi & pencatatan data ke database SQLite
- Konversi ke XML format CoT v2.0
- Kirim data ke TAK Server (`port 8089`) dengan TLS Two-Way Auth
- Manajemen device dan callsign melalui Web Admin (akan datang)
- Mode keamanan dengan NGINX reverse proxy (TLS One-Way)

## 🛠 Teknologi

- Python 3.12
- FastAPI
- Uvicorn
- SQLite (via SQLAlchemy)
- GitHub Actions (optional CI/CD)
- NGINX (reverse proxy with TLS)
- Quectel EC25 (ESP32 HTTP Push)

## 📦 Instalasi Lokal (Pengembangan)

```bash
git clone https://github.com/FabianBoro/CoTGW.git
cd CoTGW
python -m venv .venv
.venv\Scripts\activate  # or source .venv/bin/activate on Linux
pip install -r requirements.txt
python run.py
