import streamlit as st
import time
from src.gemini_client import GeminiClient
from src.graph_logic import GraphLogic
from src.pathfinder.astar_pathfinder import AStarPathFinder
from src.open_meteo_client import OpenMeteoClient
from src.helpers.image_helper import get_latest_file

def open_new_chat():
    """Generowanie nowego chatu z asystentem"""
    st.session_state.messages = []
    
    # Inicjalizacja klienta tylko wtedy, gdy go nie ma
    if "gemini_client" not in st.session_state:
        st.session_state.gemini_client = GeminiClient()
        
    # Uruchomienie metody dla asystenta (wykona się zawsze)
    st.session_state.gemini_client.generate_chat()

def show_trails_visualization():
    """Metoda zwraca wizualizację ścieżki wybranej przez asystenta"""
    time.sleep(2)
    
    # Inicjalizacja klucza messages (zabezpieczenie przed KeyError)
    #if "messages" not in st.session_state:
     #   st.session_state.messages = []
        
    st.session_state.messages.append({
        "role": "ai", 
        "content": "Oto wizualizacja wszystkich szlaków!", 
        "image": get_latest_file("data/visualizations/")
    })         

def generate_trails_visualization(graph: GraphLogic):
    """Metoda zapisuje całą mape jako zrzut w miejscu projektów"""    
    graph.save_visualization("data/visualizations")
    st.toast("Zrobiłem wizualizacje - sprawdź folder", icon="👍")
    show_trails_visualization()

def astar_test(graph: GraphLogic):
    """Testowanie działania algorytmu wyszukiwania najlepszej ścieżki"""
    pathfinder = AStarPathFinder(graph.graph)
    result_path = pathfinder.find_path("Kuznice", "Kasprowy_Wierch")
    print(result_path)
    st.toast("Wypisałem ścieżke - sprawdź konsole", icon="👍")

def get_weather():
    """Pobieranie danych z API pogodowego dla konkretnej lokalizacji"""
    openmeteo_api = OpenMeteoClient()
    result = openmeteo_api.get_date(49.2787, 19.9818)
    print(result)
    st.toast("Wypisałem pogodę dla lokalizacji Szlak_na_Nosal - sprawdź konsole", icon="👍")