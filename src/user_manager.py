import streamlit as st  # type: ignore
from datetime import datetime
import json

class UserManager:
    """Manages user profile and preferences"""

    DEFAULT_USER = {
        "username": "Turysta",
        "email": "user@example.com",
        "join_date": datetime.now().strftime("%Y-%m-%d"),
        "difficulty_level": "Średni",
        "favorite_regions": ["Tatry"],
        "preferred_language": "Polski",
        "notifications_enabled": True,
    }

    @staticmethod
    def get_user():
        """Get current user from session state"""
        if "user" not in st.session_state:
            st.session_state.user = UserManager.DEFAULT_USER.copy()
        return st.session_state.user

    @staticmethod
    def update_user(user_data: dict):
        """Update user information"""
        st.session_state.user = user_data
