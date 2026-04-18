import streamlit as st
from src.graph_logic import TrailGraph
from src.gemini_client import GeminiClient

@st.cache_resource
def init_resources():
    graf = TrailGraph()
    graf.build_trail_graph('data/trails/polish_tatra_mountains.json')
    #graf.save_visualization('data/visualizations')
    #graf.show_visualization()

    #try:
    #    gemini = GeminiClient()
    #    gemini.generate_chat()
    #    response = gemini.send_message("Powiedz mi jaką mamy godzinę i wylosuj losowy kolor.")
    #    print(response.text)
    #except Exception as ex:
    #    print(f"Wystąpił błąd:  {ex}")

    gemini_client = GeminiClient()
    gemini_client.generate_chat()
    return graf, gemini_client

def render_interface():
    st.set_page_config(page_title="Graph Scout", page_icon="🏔️", layout= "wide")
    st.title("🏔️ Graph Scout -  Asysten wycieczek górskich")
    graf, gemini_client = init_resources()
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