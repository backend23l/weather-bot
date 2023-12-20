import requests
from settings import get_api_key


def get_current(lat: float, lon: float) -> dict:
    url = 'https://api.openweathermap.org/data/2.5/weather'
    payload = {
        'lat': lat,
        'lon': lon,
        'appid': get_api_key()
    }
    resp = requests.get(url, params=payload)

    if resp.status_code == 200:
        return resp.json()
