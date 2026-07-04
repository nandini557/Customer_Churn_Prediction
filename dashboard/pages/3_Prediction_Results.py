import streamlit as st

from src.session_manager import SessionManager

st.set_page_config(
    page_title="Prediction Results",
    page_icon="📋",
    layout="wide"
)

from src.ui import load_css

load_css()

SessionManager.initialize()

if not st.session_state.analysis_complete:
    st.warning("Please upload and analyze a dataset first.")
    st.stop()

df = st.session_state.prediction_df.copy()

st.title("📋 Prediction Results")

col1, col2, col3, col4 = st.columns(4)

col1.metric(
    "Total Customers",
    len(df)
)

col2.metric(
    "Likely to Churn",
    (df["Prediction"] == "Yes").sum()
)

col3.metric(
    "Retention",
    (df["Prediction"] == "No").sum()
)

col4.metric(
    "Average Risk",
    f"{df['Churn Probability'].mean():.2f}%"
)

st.divider()

col1, col2, col3 = st.columns(3)

search = col1.text_input(
    "🔍 Search Customer ID"
)

risk = col2.selectbox(
    "Risk Level",
    [
        "All",
        "High",
        "Medium",
        "Low"
    ]
)

prediction = col3.selectbox(
    "Prediction",
    [
        "All",
        "Yes",
        "No"
    ]
)

filtered_df = df.copy()

if search:

    filtered_df = filtered_df[
        filtered_df["customerID"]
        .astype(str)
        .str.contains(search, case=False)
    ]

if risk != "All":

    filtered_df = filtered_df[
        filtered_df["Risk Level"] == risk
    ]

if prediction != "All":

    filtered_df = filtered_df[
        filtered_df["Prediction"] == prediction
    ]

filtered_df = df.copy()

if search:

    filtered_df = filtered_df[
        filtered_df["customerID"]
        .astype(str)
        .str.contains(search, case=False)
    ]

if risk != "All":

    filtered_df = filtered_df[
        filtered_df["Risk Level"] == risk
    ]

if prediction != "All":

    filtered_df = filtered_df[
        filtered_df["Prediction"] == prediction
    ]

filtered_df = filtered_df.sort_values(
    by="Churn Probability",
    ascending=False
)

st.subheader("Prediction Results")

display_columns = [
    "customerID",
    "Prediction",
    "Churn Probability",
    "Risk Level"
]

st.dataframe(
    filtered_df[display_columns],
    use_container_width=True,
    hide_index=True
)

csv = filtered_df.to_csv(index=False)

st.download_button(
    label="📥 Download Predictions",
    data=csv,
    file_name="customer_churn_predictions.csv",
    mime="text/csv"
)