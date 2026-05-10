import time
import streamlit as st # type: ignore
from src.gemini_client import GeminiClient
from src.graph_logic import GraphLogic
from src.pathfinder.astar_pathfinder import AStarPathFinder
from src.open_meteo_client import OpenMeteoClient

def sidebar_init(graph: GraphLogic):
    """Generowanie paska nawigacyjnego"""
    with st.sidebar:
        st.caption("Centrum akcji")
        st.button("Nowy chat", icon="💬", on_click = open_new_chat)
        st.button("Wyświetl zrzut szlaków", icon="📉", on_click = show_trails_visualization)
        st.button("Generuj zrzut szlaków", icon="📈", on_click = generate_trails_visualization, args=[graph])
        st.button("Testowanie A*", icon="🕸️", on_click = astar_test, args=[graph])
        st.button("Sprawdź pogodę", icon="⛅️", on_click=get_weather)
        st.caption("Czaty")
        #TODO dodanie obsługi histori czatów

def open_new_chat():
    """Generowanie nowego chatu z asystentem"""
    st.session_state.messages = []
    if "gemini_client" in st.session_state:
        st.session_state.gemini_client.generate_chat()

    if "gemini_client" not in st.session_state:
        client = GeminiClient()
        st.session_state.gemini_client = client

def show_trails_visualization():
    """Metoda zwraca vizualizację ścieżki wybranej przez asystenta"""
    #with st.spinner("Spwadzam czy posiadam zrzut..."):
    time.sleep(2)
    st.session_state.messages.append({"role": "ai", "content": "Oto wizualizacja wszystkich szlaków!", 
                                      "image": "data/visualizations/trail_map_20260509_092300.png"})         

def generate_trails_visualization(graph: GraphLogic):
    """Metoda zapisuje całą mape jako zrzut w miejscu projektów"""    
    graph.save_visualization("data/visualizations")
    st.toast("Zrobiłem wizualizacje - sprawdź folder", icon="👍")

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

def show_trail_visualization():
   """Tworzenie oraz wyświetlanie obrazka szlaku który wybraliśmy"""
   pass