from datetime import datetime, timedelta

def build_cot_xml(uid: str, lat: float, lon: float, callsign: str = None) -> str:
    now = datetime.utcnow()
    stale = now + timedelta(minutes=10)

    cot_template = f"""<event version="2.0"
        uid="{uid}"
        type="a-f-G-U-C"
        how="m-g"
        time="{now.isoformat()}Z"
        start="{now.isoformat()}Z"
        stale="{stale.isoformat()}Z">
        <point lat="{lat}" lon="{lon}" hae="5.0" ce="3.0" le="1.0"/>
        <detail>
            <contact callsign="{callsign or uid}" />
            <takv device="Quectel EC25" os="ATcommand" version="1.0" platform="ESP32"/>
        </detail>
    </event>"""

    return cot_template
