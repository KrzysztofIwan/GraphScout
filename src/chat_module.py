import streamlit as st # type: ignore
import networkx as nx # type: ignore
from src.graph_logic import TrailGraph
from src.gemini_client import GeminiClient
from src.pathfinder.astar_pathfinder import AStarPathFinder

@st.cache_resource
def get_trail_graph():
    graf = TrailGraph()
    graf.build_trail_graph('data/trails/polish_tatra_mountains.json')
    #graf.save_visualization('data/visualizations')
    #graf.show_visualization()
    return graf;

def init_resources():
    gemini_client = GeminiClient()
    gemini_client.generate_chat()
    return gemini_client

def render_interface():
    st.set_page_config(page_title="Graph Scout", page_icon="🏔️", layout= "wide")
    st.title("🏔️ Graph Scout -  Asysten wycieczek górskich")
    graf = get_trail_graph()
    gemini_client = init_resources()
    gemini_client.generate_chat()

    if "messages" not in st.session_state:
        st.session_state.messages = []

    for message in st.session_state.messages:
        with st.chat_message(message["role"]):
            st.markdown(message["content"])

    if prompt := st.chat_input("Gdzie chcesz się wybrać?"):
        st.session_state.messages.append({"role": "user", "content": prompt})
        with st.chat_message("user"):
            st.markdown(prompt)

        with st.chat_message("ai"):
            with st.spinner("Przetwarzam twoje pytanie..."):
                response = gemini_client.send_message(prompt)
                full_response = response.text
                st.markdown(full_response)
            st.session_state.messages.append({"role": "ai", "content": full_response})

    with st.sidebar:
        st.button("Nowy chat", icon="💬", on_click = open_new_chat)
        st.button("Wygeneruj zrzut grafu", icon="📈", on_click = show_trails_visualization)
        st.button("Testowanie A*", icon="🕸️", on_click=astar_test, args=[graf])

def open_new_chat():
    st.session_state.messages = []
    if "gemini_client" in st.session_state:
        st.session_state.gemini_client.generate_chat()

    if "gemini_client" not in st.session_state:
        graf, client = init_resources()
        st.session_state.gemini_client = client

def show_trail_visualization():
    pass

def show_trails_visualization():
    pass

def astar_test(graf):
    pathfinder = AStarPathFinder(graf.graph)
    result_path = pathfinder.find_path("Kuznice", "Kasprowy_Wierch")
    print(result_path)