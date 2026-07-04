import streamlit as st


class SessionManager:
    """
    Handles Streamlit session state.
    """

    @staticmethod
    def initialize():

        defaults = {
            "uploaded_df": None,
            "prediction_df": None,
            "insights": None,
            "analysis_complete": False
        }

        for key, value in defaults.items():
            if key not in st.session_state:
                st.session_state[key] = value

    @staticmethod
    def save_results(df, insights):

        st.session_state.prediction_df = df
        st.session_state.insights = insights
        st.session_state.analysis_complete = True

    @staticmethod
    def save_uploaded_dataset(df):

        st.session_state.uploaded_df = df

    @staticmethod
    def clear():

        for key in [
            "uploaded_df",
            "prediction_df",
            "insights",
            "analysis_complete"
        ]:
            st.session_state[key] = None if key != "analysis_complete" else False