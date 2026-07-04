import streamlit as st
import pandas as pd

from src.services import ChurnAnalysisService
from src.session_manager import SessionManager

st.set_page_config(page_title="Upload Dataset", layout="wide")

from src.ui import load_css

load_css()

SessionManager.initialize()

st.title("📤 Upload Customer Dataset")

uploaded_file = st.file_uploader(
    "Upload a CSV file",
    type=["csv"]
)

if uploaded_file is not None:

    df = pd.read_csv(uploaded_file)

    SessionManager.save_uploaded_dataset(df)

    st.success("Dataset uploaded successfully!")

    st.subheader("Dataset Preview")

    st.dataframe(df.head())

    st.write(f"Rows: {df.shape[0]}")
    st.write(f"Columns: {df.shape[1]}")

    if st.button("Run Analysis"):

        with st.spinner("Analyzing dataset..."):

            service = ChurnAnalysisService()

            result = service.analyze(df)

            if result["success"]:

                SessionManager.save_results(
                    result["data"],
                    result["insights"]
                )

                st.success("Analysis completed successfully!")

            else:

                st.error("Dataset validation failed!")

                st.write(result["missing_columns"])