from google import genai
import json
import os
import time

class GeminiClient:
    def __init__(self):
        config = self._load_config('config/gemini_api.json')
        self.model = config.get('gemini_model').strip()
        self.api_key = config.get('api_key').strip()
        self.client = genai.Client(api_key = self.api_key)
        self.chat = None
        
    def _load_config(self, json_path):
        if not os.path.exists(json_path):
            raise FileNotFoundError(f"Błąd: Nie znaleziono pliku {json_path}")
        with open(json_path, 'r', encoding='utf-8') as f:
            return json.load(f)

    def generate_chat(self):
        self.chat = self.client.chats.create(model = self.model)

    def send_message(self, message):
        time.sleep(1) # Dodanie przestoju z uwagi na limitowaną liczbę zapytań
        if not self.chat:
            self.generate_chat() # Jeżeli chat nie istnieje tworzymy go na nowo
        return self.chat.send_message(message)