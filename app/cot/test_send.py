from build_cot_xml import build_cot_xml
from send_to_tak_server import send_to_tak_server

if __name__ == "__main__":
    uid = "esp32-001.gps"
    lat = -7.0336
    lon = 110.421738
    callsign = "ESP32 EC25"

    cot_xml = build_cot_xml(uid, lat, lon, callsign)
    print("[DEBUG] CoT XML:")
    print(cot_xml)

    print("\n[INFO] Mengirim ke TAK Server...")
    success = send_to_tak_server(cot_xml)
    print("Sukses kirim?" , success)
