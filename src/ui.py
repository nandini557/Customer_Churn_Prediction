import os
import streamlit as st

def load_css():
    css_path = os.path.join(
        os.path.dirname(os.path.dirname(__file__)),
        "dashboard",
        "assets",
        "styles.css",
    )

    with open(css_path, "r") as css:
        st.markdown(
            f"<style>{css.read()}</style>",
            unsafe_allow_html=True,
        )
        