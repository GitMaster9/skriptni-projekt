import requests

def get_station_json_file(station_url):
    url = f"https://api.neverin.hr/v2/stations/?station={station_url}"
    response = requests.get(url)
    json_file = response.json()
    
    if 'error' in json_file:
        return None
        
    return json_file

def get_station_info_from_json(json_file):
    name = json_file.get("data").get("station").get("name")
    if name is None:
        name = "Nema podataka"

    url = json_file.get("data").get("station").get("url")
    if url is None:
        url = "Nema podataka"

    lat = json_file.get("data").get("station").get("lat")
    if lat is None:
        lat = 0

    lon = json_file.get("data").get("station").get("lon")
    if lon is None:
        lon = 0

    datetime = json_file.get("data").get("last").get("datetime")
    if datetime is None:
        datetime = "Nema podataka"

    temp = json_file.get("data").get("last").get("temp")
    if temp is None:
        temp = 0

    heat = json_file.get("data").get("last").get("heat")
    if heat is None:
        heat = 0

    rh = json_file.get("data").get("last").get("rh")
    if rh is None:
        rh = 0

    press = json_file.get("data").get("last").get("press")
    if press is None:
        press = 0

    wavg = json_file.get("data").get("last").get("wavg")
    if wavg is None:
        wavg = 0

    precip = json_file.get("data").get("last").get("precip24")
    if precip is None:
        precip = 0

    station_info = {
        "name": name,
        "url": url,
        "lat": lat,
        "lon": lon,
        "datetime": datetime,
        "temp": temp,
        "heat": heat,
        "rh": rh,
        "press": press,
        "wavg": wavg,
        "precip24": precip,
    }

    return station_info