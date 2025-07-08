#ECHO is on.
# app/cot.py

import ssl
import socket
from datetime import datetime, timedelta

def build_cot_xml(uid, lat, lon, callsign="ESP32 EC25"):
    now = datetime.utcnow()
    stale = now + timedelta(minutes=10)

    cot_template = f"""<event version="2.0" uid="{uid}" type="a-f-G-U-C" how="m-g"
        time="{now.isoformat()}Z" start="{now.isoformat()}Z" stale="{stale.isoformat()}Z">
        <point lat="{lat}" lon="{lon}" hae="5.0" ce="3.0" le="1.0"/>
        <detail>
            <contact callsign="{callsign}"/>
            <takv device="Quectel EC25" os="ATcommand" version="1.0" platform="ESP32"/>
        </detail>
    </event>"""

    return cot_template.strip()

def send_to_tak_server(xml_string, host="172.15.5.160", port=8089, cert="atak.pem"):
    try:
        context = ssl.create_default_context(ssl.Purpose.SERVER_AUTH)
        context.load_cert_chain(certfile=cert, keyfile=cert)
        context.check_hostname = False
        context.verify_mode = ssl.CERT_NONE  # Gunakan CERT_REQUIRED jika CA disediakan

        with socket.create_connection((host, port)) as sock:
            with context.wrap_socket(sock, server_hostname=host) as ssock:
                ssock.sendall(xml_string.encode("utf-8"))
                return True
    except Exception as e:
        print(f"[ERROR] send_to_tak_server: {e}")
        return False
