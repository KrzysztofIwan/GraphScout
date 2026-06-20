import streamlit as st
import json
from src.helpers.user_helper import set_user_data

st.title("👤 Profil Użytkownika")
user_data = st.session_state['user_data']

tab_profile, tab_settings = st.tabs([
        "Główne informacje",
        "Ustawienia"
    ])

with tab_profile:
    col1, col2 = st.columns(2)
    USER_NAME = user_data.get("user_name")
    CLIMBING_TITLE = user_data.get("climbing_title")
    DATE_OF_BIRTH = user_data.get("date_of_birth")
    LANGUAGE = user_data.get("language")
    MODEL_INSTRUCTION = user_data.get("model_instruction")
    MODEL_PREFERENCE = user_data.get("model_preference")
    CLIMBING_TITLE = user_data.get("climbing_level")

    with col1:
        st.text_input("Nazwa użytkownika", value=USER_NAME, disabled=True)
        st.text_input("Data urodzenia", value=DATE_OF_BIRTH, disabled=True)
        
    with col2:
        st.text_input("Tytuł wspinacza", value=CLIMBING_TITLE, disabled=True)
        st.text_input("Język", value=LANGUAGE, disabled=True)

with tab_settings:
    st.subheader("Konfiguracja Promptów")
    user_prompts = st.text_area(
        label = "Wprowadź własne warunki i instrukcje dla systemu:",
        value = MODEL_INSTRUCTION,
        placeholder="np. Omijaj szlaki o ekspozycji powyżej 2000m n.p.m...",
        height=150)
    
    st.subheader("Preferencje Szlaków")
    trail_preferences = st.text_area(
        label = "Opisz swoje preferencje dotyczące charakterystyki szlaków:",
        value = MODEL_PREFERENCE,
        placeholder="np. Preferuję szlaki techniczne, z dużą ilością łańcuchów, najlepiej w Tatrach Wysokich.",
        height=150)

    #st.subheader("Wybrany model do odpowiedzi")
    #Dodanie zwracania modeli które są używane
    #st.selectbox("Model)
    #st.selectbox(
    #        "Preferowany poziom trudności",
    #        ["Łatwy", "Średni", "Trudny", "Zaawansowany"]
    #    )

    st.divider()
    if st.button("Zapisz zmiany"):
        set_user_data(user_data, "model_instruction", user_prompts)
        set_user_data(user_data, "model_preference", trail_preferences)
        st.success("Zaktualizowałem ustawienia dla modelu")