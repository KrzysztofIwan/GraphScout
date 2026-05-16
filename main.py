import streamlit as st
import time
from src.graph_logic import GraphLogic
from src.helpers.chat_helper import open_new_chat, show_trails_visualization, generate_trails_visualization, astar_test, get_weather

st.set_page_config(page_title="Graph Scout", page_icon="🏔️", layout = "wide")

st.session_state['graph'] = GraphLogic().build_trail_graph('data/trails/polish_tatra_mountains.json')

page_1 = st.Page("src/views/chat_page.py", title="Chatbot")
page_2 = st.Page("src/views/user_page.py", title="Profil")

pg = st.navigation([page_1, page_2])

st.sidebar.title("Centrum akcji")
if pg == page_1:
    graph = st.session_state['graph']
    with st.sidebar:
        st.button("Nowy chat", icon="💬", on_click = open_new_chat, use_container_width=True)
        st.button("Wyświetl zrzut szlaków", icon="📉", on_click = show_trails_visualization, use_container_width=True)
        st.button("Generuj zrzut szlaków", icon="📈", on_click = generate_trails_visualization, use_container_width=True, args=[graph])
        st.button("Testowanie A*", icon="🕸️", on_click = astar_test, use_container_width=True, args=[graph])
        st.button("Sprawdź pogodę", icon="⛅️", on_click=get_weather, use_container_width=True)
        st.title("Czaty")
elif pg == page_2:
    with st.sidebar:
        st.button("Edytuj profil", icon="⚡", use_container_width=True)
    
pg.run()