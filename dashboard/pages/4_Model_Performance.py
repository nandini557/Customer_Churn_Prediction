import json
import os

import pandas as pd
import plotly.express as px
import streamlit as st

st.set_page_config(
    page_title="Model Performance",
    page_icon="📈",
    layout="wide"
)

from src.ui import load_css

load_css()

st.title("📈 Model Performance")

project_root = os.path.dirname(
    os.path.dirname(
        os.path.dirname(
            os.path.abspath(__file__)
        )
    )
)

metrics_path = os.path.join(
    project_root,
    "reports",
    "model_metrics.json"
)

if not os.path.exists(metrics_path):

    st.warning(
        "Please train the model first."
    )

    st.stop()

with open(metrics_path) as file:

    metrics = json.load(file)

col1, col2, col3, col4 = st.columns(4)

col1.metric(
    "Accuracy",
    metrics["Accuracy"]
)

col2.metric(
    "Precision",
    metrics["Precision"]
)

col3.metric(
    "Recall",
    metrics["Recall"]
)

col4.metric(
    "F1 Score",
    metrics["F1 Score"]
)

st.subheader("Confusion Matrix")

cm = pd.DataFrame(

    metrics["Confusion Matrix"],

    index=["Actual No", "Actual Yes"],

    columns=["Predicted No", "Predicted Yes"]

)

fig = px.imshow(

    cm,

    text_auto=True,

    aspect="auto",

    title="Confusion Matrix"

)

st.plotly_chart(
    fig,
    use_container_width=True
)