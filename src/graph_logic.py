import networkx as nx
import matplotlib.pyplot as plt
import json
import os
from datetime import datetime

class TrailGraph:
    def __init__(self):
        self.graph = nx.DiGraph()

    def build_trail_graph(self, json_path):
        if not os.path.exists(json_path):
            raise FileNotFoundError(f"Błąd: Nie znaleziono pliku {json_path}")

        with open(json_path, 'r', encoding='utf-8') as f:
            data = json.load(f)

        for node in data['nodes']:
            self.graph.add_node(
                node['id'], 
                elevation=node['elevation'], 
                pos=(node['lon'], node['lat']), 
                type=node['type']
            )
            
        for link in data['links']:
            src = "Kuźnice" if link['source'] == "Kuznice" else link['source']
            tgt = link['target']
            
            self.graph.add_edge(
                src, tgt, 
                weight=link['time_forward'], 
                dist=link['distance_km'],
                diff=link['difficulty'],
                color=link['color'],
                winter=link['winter_closure']
            )
            self.graph.add_edge(
                tgt, src, 
                weight=link['time_backward'], 
                dist=link['distance_km'],
                diff=link['difficulty'],
                color=link['color'],
                winter=link['winter_closure']
            )

    def visualize(self, output_dir=None):
        if output_dir:
            os.makedirs(output_dir, exist_ok=True)

        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        full_path = os.path.join(output_dir, f"trail_full_{timestamp}.png") if output_dir else f"trail_{timestamp}.png"

        pos = nx.get_node_attributes(self.graph, 'pos')
        
        type_colors = {
            'summit': '#ff4d4d',   # Czerwony
            'shelter': '#4d79ff',  # Niebieski
            'parking': '#2eb82e',  # Zielony
            'pass': '#ffa31a',     # Pomarańczowy
            'junction': '#a6a6a6'  # Szary
        }
        node_colors = [type_colors.get(self.graph.nodes[n].get('type'), '#ffffff') for n in self.graph.nodes()]
        
        node_labels = {n: f"{n}\n({self.graph.nodes[n]['elevation']}m)" for n in self.graph.nodes()}
        
        edge_labels = {}
        for u, v, d in self.graph.edges(data=True):
            edge_labels[(u, v)] = f"{d['weight']}min | {d['dist']}km\nT:{d['diff']}"

        edge_colors = [self.graph[u][v]['color'] for u, v in self.graph.edges()]

        plt.figure(figsize=(15, 12))

        nx.draw_networkx_nodes(self.graph, pos, node_size=3000, node_color=node_colors, alpha=0.9)
        nx.draw_networkx_edges(self.graph, pos, edge_color=edge_colors, width=2.5, 
                               arrowsize=25, connectionstyle='arc3,rad=0.15')
        nx.draw_networkx_labels(self.graph, pos, labels=node_labels, font_size=9, font_weight='bold')
        
        nx.draw_networkx_edge_labels(self.graph, pos, edge_labels=edge_labels, font_size=7, label_pos=0.3)

        plt.title(f"Pełny Graf Szlaków Tatrzańskich\nEtykiety: Czas | Dystans | Trudność", pad=20, fontsize=15)
        
        from matplotlib.lines import Line2D
        legend_elements = [Line2D([0], [0], marker='o', color='w', label=k,
                          markerfacecolor=v, markersize=10) for k, v in type_colors.items()]
        plt.legend(handles=legend_elements, title="Typy punktów", loc='upper left')

        plt.savefig(full_path, bbox_inches='tight', dpi=300)
        print(f"Pełna wizualizacja zapisana w: {full_path}")
        plt.show()