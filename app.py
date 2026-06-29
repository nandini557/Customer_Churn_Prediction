import streamlit as st
from utils.constants import APP_NAME, APP_ICON

st.set_page_config(
    page_title=APP_NAME,
    page_icon=APP_ICON,
    layout="wide",
    initial_sidebar_state="expanded"
)

st.sidebar.success("Select a page above.")

st.title(APP_NAME)

st.markdown("""
## Welcome 👋

This application predicts whether a telecom customer is likely to churn.

Use the navigation panel on the left to explore the application.
""")