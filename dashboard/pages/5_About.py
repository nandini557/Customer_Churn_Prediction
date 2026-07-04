import streamlit as st

st.set_page_config(
    page_title="About",
    page_icon="ℹ️",
    layout="wide"
)

from src.ui import load_css

load_css()

st.title("ℹ️ About AI Customer Churn Analyzer")

st.markdown("---")

st.header("📌 Project Overview")

st.write(
    """
The **AI Customer Churn Analyzer** is a machine learning application
that predicts whether telecom customers are likely to churn.

The application allows companies to upload their customer datasets,
generate churn predictions, visualize business insights, and download
prediction results through an interactive dashboard.
"""
)

st.markdown("---")

st.header("🎯 Objectives")

st.markdown("""
- Predict customer churn using Machine Learning
- Analyze customer behavior
- Identify high-risk customers
- Provide business insights through interactive dashboards
- Support bulk dataset analysis
""")

st.markdown("---")

st.header("🛠 Technology Stack")

col1, col2 = st.columns(2)

with col1:

    st.markdown("""
### Backend

- Python
- Pandas
- NumPy
- Scikit-learn
- Joblib
    """)

with col2:

    st.markdown("""
### Frontend

- Streamlit
- Plotly
- Git
- GitHub
    """)

st.markdown("---")

st.header("⚙ Machine Learning Pipeline")

st.code("""
Customer Dataset
        │
        ▼
Data Validation
        │
        ▼
Preprocessing
        │
        ▼
Random Forest Pipeline
        │
        ▼
Prediction
        │
        ▼
Business Insights
        │
        ▼
Interactive Dashboard
""")

st.markdown("---")

st.header("✨ Key Features")

st.markdown("""
✅ Bulk CSV Upload

✅ Customer Churn Prediction

✅ Business Analytics Dashboard

✅ Interactive Visualizations

✅ Risk Classification

✅ Download Predictions

✅ Model Performance Dashboard
""")

st.markdown("---")

st.header("🚀 Future Enhancements")

st.markdown("""
- SHAP Explainability
- PDF Report Generation
- Database Integration
- REST API (FastAPI)
- Docker Deployment
- Cloud Deployment
- Authentication System
""")

st.markdown("---")

st.success("Developed using Python, Scikit-learn and Streamlit.")