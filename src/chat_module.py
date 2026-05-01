import streamlit as st # type: ignore
from src.graph_logic import GraphLogic
from src.gemini_client import GeminiClient
from src.sidebar_module import sidebar_init

def render_interface():
    """Generowanie czatu z asystentem"""
    st.set_page_config(page_title="Graph Scout", page_icon="🏔️", layout= "wide")
    st.title("🏔️ Graph Scout -  Asysten wycieczek górskich")
    graph = setup_trails_graph()
    gemini_client = GeminiClient()
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
                response = gemini_client.send_message(prompt, graph)
                full_response = response.text
                st.markdown(full_response)
            st.session_state.messages.append({"role": "ai", "content": full_response})
    
    sidebar_init(graph)

@st.cache_resource
def setup_trails_graph():
    return GraphLogic().build_trail_graph('data/trails/polish_tatra_mountains.json')