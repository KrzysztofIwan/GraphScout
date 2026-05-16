import requests
import json
import os
from datetime import datetime, timedelta
import pandas as pd

class OpenMeteoClient:
    def __init__(self):
        config = self._load_config('config/open_meteo_api.json')
        self.weather_codes = self._load_config('config/weather_code.json')
        self.url = config.get('url').strip()
        self.timezone = config.get('timezone').strip()
         
    def _load_config(self, json_path):
        if not os.path.exists(json_path):
            raise FileNotFoundError(f"Błąd: Nie znaleziono pliku {json_path}")
        with open(json_path, 'r', encoding='utf-8') as f:
            return json.load(f)       
        
    #def get_date(self, latitude:float, longitude:float, forecast_days:int = 7):
    def get_date(self, latitude:float, longitude:float, start_dt:datetime = None):
        if start_dt is None:
            start_dt = datetime.now()
        end_dt = start_dt + timedelta(hours=8)
        params = {
            "latitude": latitude,
            "longitude": longitude,
            "hourly": ["temperature_2m", "weather_code"],
            "timezone": self.timezone,
            #"forecast_days": forecast_days
            "start_hour": start_dt.strftime("%Y-%m-%dT%H:%M"),
            "end_hour": end_dt.strftime("%Y-%m-%dT%H:%M")
        }

        try:
            response = requests.get(self.url, params)
            response.raise_for_status()
            return response.json()
        
        except requests.exceptions.RequestException as e:
            print(f"Błąd połączenia: {e}")
        
    def process_weather(self, data):
        df = pd.DataFrame(data['hourly'])
        report_date = pd.to_datetime(df['time']).dt.date.iloc[0]
        df['time'] = pd.to_datetime(df['time']).dt.strftime('%H:%M')
        df['weather_code'] = df['weather_code'].astype(str).map(self.weather_codes)
        
        df.rename(columns={
        'time': 'Godzina',
        'temperature_2m': 'Temperatura w celcjuszach',
        'weather_code': 'Pogoda'
        }, inplace=True)

        return report_date.strftime("%m/%d/%Y"), df;