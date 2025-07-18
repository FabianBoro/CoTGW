import requests

# Konfigurasi endpoint TAK Server
TAK_SERVER_URL = "https://172.15.5.150:8089/"  # Ganti IP dengan IP aktual
CERT_FILE = "webadmin.pem"  # Gabungan client cert + key
CA_FILE = "webadmin.pem"    # CA cert (bisa sama file jika bundle)

def send_to_tak_server(cot_xml: str) -> bool:
    try:
        response = requests.post(
            TAK_SERVER_URL,
            data=cot_xml,
            headers={"Content-Type": "application/xml"},
            cert=CERT_FILE,
            verify=CA_FILE,
            timeout=5
        )
        print(f"Status: {response.status_code}")
        print(f"Response: {response.text}")
        return response.status_code == 200
    except requests.exceptions.ChunkedEncodingError as e:
        print("[WARNING] TAK Server tidak mengirim response standar, tapi CoT kemungkinan diterima.")
        return True
    except Exception as e:
        print(f"[ERROR] Gagal kirim CoT ke TAK Server: {e}")
        return False