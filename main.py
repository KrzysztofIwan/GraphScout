from src.graph_logic import TrailGraph
from src.gemini_client import GeminiClient

def run_app():
    graf = TrailGraph()
    graf.build_trail_graph('data/trails/polish_tatra_mountains.json')
    #graf.save_visualization('data/visualizations')
    #graf.show_visualization()

    try:
        gemini = GeminiClient()
        gemini.generate_chat()
        response = gemini.send_message("Powiedz mi jaką mamy godzinę i wylosuj losowy kolor.")
        print(response.text)
    except Exception as ex:
        print(f"Wystąpił błąd:  {ex}")

if __name__ == "__main__":
    run_app()