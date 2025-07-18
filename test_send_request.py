import requests
from datetime import datetime

url = "http://localhost:8000/cot/"

payload = {
    "id": "esp32-test1",
    "lat": -7.0336,
    "lon": 110.421738,
    "ts": datetime.utcnow().isoformat() + "Z"
}

print("[DEBUG] Sending to /cot/...")
response = requests.post(url, json=payload)
print("[DEBUG] Response status:", response.status_code)
print("[DEBUG] Response content:", response.text)
