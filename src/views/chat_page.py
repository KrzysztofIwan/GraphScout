import streamlit as st
from src.gemini_client import GeminiClient

st.title("🏔️ Graph Scout")
st.caption("Asysten wycieczek górskich", width= "content")
st.info("Chatbot może generować nieprawdziwe informacje.", icon="⚠️")
graph = st.session_state['graph']

if "messages" not in st.session_state:
    st.session_state.messages = []

for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"], unsafe_allow_html=True)
        if "image" in message:
            st.image(message["image"])

if prompt := st.chat_input("Gdzie chcesz się wybrać?"):
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.markdown(prompt)

    with st.chat_message("ai"):
        with st.spinner("Przetwarzam twoje pytanie..."):
            gemini_client = GeminiClient()
            gemini_client.generate_chat()
            response = gemini_client.send_message(prompt, graph)
            full_response = response.text
            st.markdown(full_response)
            st.session_state.messages.append({"role": "ai", "content": full_response})