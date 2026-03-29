import networkx as nx
import matplotlib.pyplot as plt
from matplotlib.lines import Line2D
import json
import os
import numpy as np
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
            src, tgt = link['source'], link['target']
            
            common_attrs = {
                'dist': link['distance_km'],
                'diff': link['difficulty'],
                'color': link['color'],
                'winter': link['winter_closure']
            }
            
            self.graph.add_edge(src, tgt, weight=link['time_forward'], **common_attrs)
            self.graph.add_edge(tgt, src, weight=link['time_backward'], **common_attrs)

    def _setup_plot(self):
        pos = nx.get_node_attributes(self.graph, 'pos')
        
        type_colors = {
            'summit': '#ff4d4d', 'shelter': '#4d79ff',
            'parking': '#2eb82e', 'pass': '#ffa31a', 'junction': '#a6a6a6'
        }
        
        node_colors = [type_colors.get(self.graph.nodes[n].get('type'), '#ffffff') for n in self.graph.nodes()]
        node_labels = {n: f"{n}\n({self.graph.nodes[n].get('elevation', '?')}m)" for n in self.graph.nodes()}

        fig, ax = plt.subplots(figsize=(18, 12))
        
        # 1. Rysowanie węzłów
        nx.draw_networkx_nodes(self.graph, pos, node_size=3800, node_color=node_colors, 
                               alpha=1.0, edgecolors='black', linewidths=1.5, ax=ax)
        
        # 2. Rysowanie krawędzi z wyraźnymi strzałkami i łukami
        for u, v, d in self.graph.edges(data=True):
            rad = 0.15 # Stały łuk dla każdej krawędzi skierowanej
            nx.draw_networkx_edges(
                self.graph, pos, edgelist=[(u, v)],
                edge_color=d['color'], width=2.5,
                arrowstyle='-|>', arrowsize=25,
                connectionstyle=f'arc3,rad={rad}',
                min_source_margin=20, min_target_margin=20, ax=ax
            )

        # 3. Rysowanie etykiet węzłów
        nx.draw_networkx_labels(self.graph, pos, labels=node_labels, font_size=8, 
                                font_weight='bold', ax=ax)

        # 4. Ręczne rysowanie etykiet krawędzi (obsługa łuków)
        for u, v, d in self.graph.edges(data=True):
            # Obliczanie punktu środkowego łuku dla etykiety
            p1 = np.array(pos[u])
            p2 = np.array(pos[v])
            
            # Środek odcinka
            mid = (p1 + p2) / 2
            # Wektor prostopadły dla przesunięcia etykiety na zewnątrz łuku
            diff = p2 - p1
            norm = np.linalg.norm(diff)
            if norm == 0: continue
            
            perp = np.array([-diff[1], diff[0]]) / norm
            # Przesunięcie etykiety (rad * dystans / 2)
            label_pos = mid + perp * (norm * 0.1) 
            
            label_text = f"{d['weight']}min\n{d['dist']}km | T:{d['diff']}"
            
            ax.text(label_pos[0], label_pos[1], label_text, 
                    fontsize=7, ha='center', va='center',
                    bbox=dict(facecolor='white', edgecolor='none', alpha=0.8, pad=0.2),
                    zorder=10)

        plt.title("Graf Szlaków Tatrzańskich - Poprawiona Czytelność", pad=20, fontsize=15)
        
        legend_elements = [Line2D([0], [0], marker='o', color='w', label=k,
                          markerfacecolor=v, markersize=12, markeredgecolor='black') 
                          for k, v in type_colors.items()]
        ax.legend(handles=legend_elements, title="Typy punktów", loc='upper left', frameon=True)
        
        plt.axis('off')
        return fig

    def save_visualization(self, output_dir="output"):
        os.makedirs(output_dir, exist_ok=True)
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        full_path = os.path.join(output_dir, f"trail_map_{timestamp}.png")
        
        fig = self._setup_plot()
        plt.savefig(full_path, bbox_inches='tight', dpi=300)
        plt.close(fig)
        print(f"Wizualizacja zapisana: {full_path}")

    def show_visualization(self):
        self._setup_plot()
        plt.show()