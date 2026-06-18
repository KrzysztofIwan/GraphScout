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
    if result and result[0] != "Error":
        details = pathfinder.get_path_details(result)
    return result, details

def get_info_about_trail_color(trail_color:str):
    """Zwracanie informacji na temat koloru szlaku"""
    trail_difficulty = st.session_state['trail_difficulty']
    return trail_difficulty.get(delete_polish_chars(trail_color))

def get_info_about_point(point_name:str):
    """Pobieranie informacji na temat punktu na szlaku"""
    point_name = delete_polish_chars(point_name)
    graph = st.session_state['graph']
    pathfinder = AStarPathFinder(graph.graph)
    return pathfinder.get_point_info(point_name)

def get_info_about_alarm_phone():
    alarm_phones = st.session_state['alarm_phones']
    return alarm_phones

def get_parkings():
    """Pobiera najbliższe parkingi dla początkowych miejsc na szlaku integracja z Osm"""
    #TODO