import requests
import json
import os

class OpenMeteoClient:
    def __init__(self):
        config = self._load_config('config/open_meteo_api.json')
        url = config.get('url').strip()
        timezone = config.get('timezone').strip()
        hourly = config.get('hourly').strip()

    def _load_config(self, json_path):
        if not os.path.exists(json_path):
            raise FileNotFoundError(f"Błąd: Nie znaleziono pliku {json_path}")
        with open(json_path, 'r', encoding='utf-8') as f:
            return json.load(f)
        
    def get_date(self, latitude, longitude, forecast_days):
        params = {
            "latitude": latitude,
            "longitude": longitude,
            "hourly": self.hourly,
            "timezone": self.timezone,
            "forecast_days": forecast_days
        }

        try:
            response = requests.get(self.url, params)
            response.raise_for_status()
            data = response.json()
            print(data);
        
        except requests.exceptions.RequestException as e:
            print(f"Błąd połączenia: {e}")