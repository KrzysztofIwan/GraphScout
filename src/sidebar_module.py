import streamlit as st # type: ignore
from src.gemini_client import GeminiClient
from src.graph_logic import GraphLogic
from src.pathfinder.astar_pathfinder import AStarPathFinder

def sidebar_init(graph: GraphLogic):
    """Generowanie paska nawigacyjnego"""
    with st.sidebar:
        st.caption("Centrum akcji")
        st.button("Nowy chat", icon="💬", on_click = open_new_chat)
        st.button("Wyświetl zrzut szlaków - TODO", icon="📉", on_click= show_trails_visualization, args=[graph])
        st.button("Generuj zrzut szlaków", icon="📈", on_click = generate_trails_visualization, args=[graph])
        st.button("Testowanie A*", icon="🕸️", on_click= astar_test, args=[graph])
        st.caption("Czaty")

def open_new_chat():
    """Generowanie nowego chatu z asystentem"""
    st.session_state.messages = []
    if "gemini_client" in st.session_state:
        st.session_state.gemini_client.generate_chat()

    if "gemini_client" not in st.session_state:
        client = GeminiClient()
        st.session_state.gemini_client = client

def show_trails_visualization(graph: GraphLogic):
    """Metoda zwraca całą mape szlaków"""
    graph.show_visualization()

def generate_trails_visualization(graph: GraphLogic):
    """Metoda zapisuje całą mape jako zrzut w miejscu projektów"""    
    graph.save_visualization("data/visualizations")

def astar_test(graph: GraphLogic):
    """Testowanie działania algorytmu wyszukiwania najlepszej ścieżki"""
    pathfinder = AStarPathFinder(graph.graph)
    result_path = pathfinder.find_path("Kuznice", "Kasprowy_Wierch")
    print(result_path)

def show_trail_visualization():
    """Metoda zwraca vizualizację ścieżki wybranej przez asystenta"""
    pass