import streamlit as st

class DynamicPromptManager:
    def __init__(self, base:str ):
        self.instruction = "BEZWZGLEDNE OGRANICZENIA I INSTRUKCJE\n" + base

    def build_prompt(self):
        user_data = st.session_state['user_data']
        user_instruction = user_data.get("model_instruction")
        user_preference = user_data.get("model_preference")

        if user_instruction:
            self.instruction += f"\n{user_instruction}"

        if user_preference:
            self.instruction += f"\n{user_preference}"

        return self.instruction