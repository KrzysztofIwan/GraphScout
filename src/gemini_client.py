import json
import os
import time
import networkx as nx # type: ignore
from src.function_calling import get_weather, get_the_best_path, get_info_about_point, get_info_about_trail_color, get_info_about_alarm_phone
from google import genai
from google.genai import errors
from src.dynamic_prompt_manager import DynamicPromptManager

class GeminiClient:
    def __init__(self):
        config = self._load_config('config/gemini_api.json')
        self.model = config.get('gemini_model').strip()
        self.api_key = config.get('api_key').strip()
        self.base_instruction = config.get('base_instruction').strip()
        self.client = genai.Client(api_key = self.api_key)
        self.chat = None
        
    def _load_config(self, json_path):
        if not os.path.exists(json_path):
            raise FileNotFoundError(f"Błąd: Nie znaleziono pliku {json_path}")
        with open(json_path, 'r', encoding='utf-8') as f:
            return json.load(f)

    def generate_chat(self):
        self.chat = self.client.chats.create(model = self.model)

    def send_message(self, message: str, graph: nx.DiGraph):
        time.sleep(1) # Dodanie przestoju z uwagi na limitowaną liczbę zapytań
        if not self.chat:
            self.generate_chat() # Jeżeli chat nie istnieje tworzymy go na nowo

        bulder = DynamicPromptManager(self.base_instruction)
        current_instruction = bulder.build_prompt()
        
        trial = 3
        wait = 2

        for t in range(trial):
            try:
                result = self.client.models.generate_content(
                    model = self.model,
                    contents= message,
                    config={
                        "tools" : [get_the_best_path, get_weather, get_info_about_trail_color, get_info_about_alarm_phone, get_info_about_point],
                        "system_instruction" : current_instruction
                    }
                )
                return result
            
            except errors.ServerError as ex:
                if ex.code == 503 and t < trial - 1:
                    print(f"Błąd 503 (Przeciążenie). Próba {t + 1}/{trial}. Ponowna próba za {wait}s...")
                    time.sleep(wait)
                    wait *= 2 # Wykładnicze wydłużanie czasu oczekiwania
                else:
                    raise ex
            
            except Exception as ex:
                raise ex