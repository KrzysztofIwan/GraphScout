import streamlit as st

st.title("👤 Profil Użytkownika")

tab_profile, tab_settings = st.tabs([
        "Główne informacje",
        "Ustawienia"
    ])

with tab_profile:
    col1, col2 = st.columns(2)
    USER_NAME = "Krzysiek2137"
    CLIMBING_TITLE = "Górol"
    DATE_OF_BIRTH = "18.11.2001"
    LANGUAGE = "Polski"

    with col1:
        st.text_input("Nazwa użytkownika", value=USER_NAME, disabled=True)
        st.text_input("Data urodzenia", value=DATE_OF_BIRTH, disabled=True)
        
    with col2:
        st.text_input("Tytuł wspinacza", value=CLIMBING_TITLE, disabled=True)
        st.text_input("Język", value=LANGUAGE, disabled=True)

with tab_settings:
    st.subheader("Konfiguracja Promptów")
    user_prompts = st.text_area(
        "Wprowadź własne warunki i instrukcje dla systemu:",
        placeholder="np. Omijaj szlaki o ekspozycji powyżej 2000m n.p.m...",
        height=150)
    
    st.subheader("Preferencje Szlakowe")
    trail_preferences = st.text_area(
        "Opisz swoje preferencje dotyczące charakterystyki szlaków:",
        placeholder="np. Preferuję szlaki techniczne, z dużą ilością łańcuchów, najlepiej w Tatrach Wysokich.",
        height=150)

    st.selectbox(
            "Preferowany poziom trudności",
            ["Łatwy", "Średni", "Trudny", "Zaawansowany"]
        )

    st.divider()
    if st.button("Zapisz zmiany"):
        st.session_state['custom_prompts'] = user_prompts
        st.session_state['trail_prefs'] = trail_preferences
        st.success("Preferencje zostały zaktualizowane w bieżącej sesji.")    