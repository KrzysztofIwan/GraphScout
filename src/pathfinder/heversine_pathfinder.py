import math
import networkx as nx # type: ignore

def haversine_distance(lat1, lon1, lat2, lon2):
    #Wykorzystanie algorytmu Haversine’a w celu obliczenia odpległości w lini prostej
    earth_radius = 6371
    phi1, phi2 = math.radians(lat1), math.radians(lat2)
    d_phi = math.radians(lat2 - lat1)
    d_lambda = math.radians(lon2 - lon1)

    a = (math.sin(d_phi / 2)**2 + math.cos(phi1) * math.cos(phi2) * math.sin(d_lambda / 2)**2)
    c =  2 * math.atan2(math.sqrt(a), math.sqrt(1-a))
    return earth_radius * c

def get_heuristic(current_node, end_node, Graph):
    #Obliczanie h(n) - optymistyczne dotarcie do celu
    n1 = Graph.nodes[current_node]
    n2 = Graph.nodes[end_node]

    dist_km = haversine_distance(n1['lat'], n1['lon'], n2['lat'], n2['lon'])
    
    #Zakładam że pokonanie 1km zajmuje 10min (szybkie tempo marszu)
    return dist_km *10