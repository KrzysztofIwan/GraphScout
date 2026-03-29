from src.graph_logic import TrailGraph

def run_app():
    graf = TrailGraph()
    graf.build_trail_graph('data/trails/polish_tatra_mountains.json')
    #graf.save_visualization('data/visualizations')
    graf.show_visualization()

if __name__ == "__main__":
    run_app()