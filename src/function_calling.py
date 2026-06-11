from src.open_meteo_client import OpenMeteoClient
from src.pathfinder.astar_pathfinder import AStarPathFinder
from src.helpers.string_helper import delete_polish_chars
import streamlit as st

def get_weather(latitude:float, longitude:float):
    """Pobiera i zwraca pogodę dla wybranej lokalizacji 8h do przodu"""
    openmeteo_api = OpenMeteoClient()
    result = openmeteo_api.get_date(latitude, longitude)
    date, table = openmeteo_api.process_weather(result)
    return date, table.to_html(index=False)

def get_the_best_path(start_point:str, end_point:str):
    """Wylicza i zwraca najlesze połączenie pomiędzy punktami"""
    graph = st.session_state['graph']
    pathfinder = AStarPathFinder(graph.graph)
    result = pathfinder.find_path(start_point, end_point)
    details = []
    if result:
        details = pathfinder.get_path_details(result)
    return result, details

def get_into_about_trail_color(trail_color:str):
    """Zwracanie informacji na temat koloru szlaku"""
    trail_difficulty = st.session_state['trail_difficulty']
    return trail_difficulty.get(delete_polish_chars(trail_color))

def get_info_about_point():
    """Pobieranie informacji na temat punktu na szlaku"""
    #TODO

def get_durations(start_point:str, end_point:str):
    """Zwraca czas przejcia pomiędzy punktem startowym a docelowym"""
    #TODO

def get_parkings():
    """Pobiera najbliższe parkingi dla początkowych miejsc na szlaku integracja z Osm"""
    #TODO