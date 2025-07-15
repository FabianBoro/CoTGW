from app.cot.build_cot_xml import build_cot_xml
from app.cot.send_to_tak_server import send_to_tak_server

xml = build_cot_xml(uid="esp32-001.gps", lat=-7.0336, lon=110.421738, callsign="Tim SAR Alpha")
success = send_to_tak_server(xml)
print("Success:", success)
