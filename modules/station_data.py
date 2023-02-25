import requests

def get_station_data(station_name):
    url = f"https://api.neverin.hr/v2/stations/?station={station_name}"
    response = requests.get(url)
    data = response.json()
    
    if 'error' in data:
        return None
        
    return data