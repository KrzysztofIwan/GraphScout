import math
import networkx as nx # type: ignore
import heapq
from typing import List, Dict, Tuple
from .heversine_pathfinder import get_heuristic
from ..helpers.string_helper import delete_polish_chars

class AStarPathFinder:
    def __init__(self, graph: nx.DiGraph):
        self.graph = graph

    #Zmienne są stringami ponieważ wierzchołki w grafie mają swoje nazwy
    def find_path(self, start_node: str, goal_node: str) -> List[str]:
        """Wyszukiwanie najlepszej ścieżki w grafie"""

        #Pozbywanie się polskich znaków
        start_node = delete_polish_chars(start_node)
        goal_node = delete_polish_chars(goal_node)

        #Sprawdzenie czy wierzchołki istnieją w grafie
        if start_node not in self.graph:
            print(f"Błąd: Wierzołek ({start_node}) nie istnieje w grafie.")
            return []
        
        if goal_node not in self.graph:
            print(f"Błąd: Wierzchołek ({goal_node}) nie istnieje w grafie.")
            return []

        # Kolejka priorytetowa przechowująca krotki (f_score, node_id)
        # heapq zawsze wypycha najmniejszy pierwszy element
        open_set: List[Tuple[float, str]] = []
        heapq.heappush(open_set, (0.0, start_node))

        # Słownik przechowujący najlepszego 'rodzica' dla każdego węzła
        came_from: Dict[str, str] = {}

        # g_score: rzeczywisty koszt dotarcia ze startu do danego węzła
        g_score: Dict[str, float] = {node: float('inf') for node in self.graph.nodes}
        g_score[start_node] = 0.0

        # f_score: g_score + h_score (heurystyka)
        f_score: Dict[str, float] = {node: float('inf') for node in self.graph.nodes}
        f_score[start_node] = get_heuristic(start_node, goal_node, self.graph)

        while open_set:
            # Pobieramy węzeł z najniższym f_score
            _, current = heapq.heappop(open_set)

            if current == goal_node:
                return self._reconstruct_path(came_from, current)

            for neighbor in self.graph.neighbors(current):
                # Pobieramy wagę krawędzi (czas przejścia)
                # Zakładamy, że krawędź w DiGraph ma już przypisany poprawny kierunek wag
                weight = self.graph[current][neighbor].get('time_forward', 0)
                
                # Obliczamy tymczasowy g_score dla sąsiada
                tentative_g_score = g_score[current] + weight

                if tentative_g_score < g_score[neighbor]:
                    # Znaleźliśmy lepszą drogę do tego sąsiada
                    came_from[neighbor] = current
                    g_score[neighbor] = tentative_g_score
                    f_score[neighbor] = tentative_g_score + get_heuristic(neighbor, goal_node, self.graph)
                    
                    # Jeśli sąsiada nie ma w kolejce, dodajemy go (heapq nie wspiera update'u)
                    # Duplikaty w open_set zostaną obsłużone przez wyższy f_score i zignorowane
                    heapq.heappush(open_set, (f_score[neighbor], neighbor))

        return []  # Ścieżka nie istnieje

    def _reconstruct_path(self, came_from: Dict[str, str], current: str) -> List[str]:
        """Odtwarza trasę cofając się po rodzicach."""
        total_path = [current]
        while current in came_from:
            current = came_from[current]
            total_path.append(current.replace("_"," "))
        return total_path[::-1] # Odwrócenie listy na [Start -> Cel]