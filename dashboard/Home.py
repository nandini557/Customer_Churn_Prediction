import os
import sys

PROJECT_ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

if PROJECT_ROOT not in sys.path:
    sys.path.insert(0, PROJECT_ROOT)

import streamlit as st
from src.ui import load_css

st.set_page_config(
    page_title="AI Customer Churn Analyzer",
    page_icon="📊",
    layout="wide"
)

load_css()

# ----------------------------
# Header
# ----------------------------

st.title("📊 AI Customer Churn Analyzer")

st.caption(
    "Machine Learning Powered Customer Retention Dashboard"
)

st.divider()

# ----------------------------
# Feature Cards - Row 1
# ----------------------------

col1, col2 = st.columns(2)

with col1:
    st.info("""
📤 **Upload Dataset**

Analyze telecom customer data in seconds.
""")

with col2:
    st.success("""
🤖 **Predict Churn**

Identify customers likely to leave.
""")

# ----------------------------
# Feature Cards - Row 2
# ----------------------------

col3, col4 = st.columns(2)

with col3:
    st.warning("""
📈 **Business Insights**

Interactive analytics dashboard.
""")

with col4:
    st.error("""
📥 **Download Results**

Export predictions instantly.
""")

st.divider()

# ----------------------------
# About the App
# ----------------------------

st.subheader("🚀 What can this application do?")

st.markdown("""
- Upload telecom customer datasets
- Predict customer churn using a trained Machine Learning model
- Explore interactive business analytics
- Identify high-risk customers
- Download prediction results as CSV
- Evaluate model performance
""")

st.divider()

st.info("👈 Use the sidebar to navigate through the application.")