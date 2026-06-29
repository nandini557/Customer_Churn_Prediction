import streamlit as st

st.title("🏠 Home")

st.write("Welcome to the Customer Churn Prediction System.")

st.markdown("---")

st.subheader("What is Customer Churn?")

st.write("""
Customer churn refers to customers leaving a company's services.

Using Machine Learning, we can predict which customers are at high risk of leaving.
""")

st.subheader("Features")

st.markdown("""
- 🔍 Single Customer Prediction
- 📂 Batch Prediction
- 📊 Interactive Dashboard
- 🤖 Model Information
- 📥 Download Results
""")

st.markdown("---")

st.info("Select a page from the sidebar to begin.")