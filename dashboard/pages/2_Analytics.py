import streamlit as st
import pandas as pd
import plotly.express as px

from src.session_manager import SessionManager

st.set_page_config(
    page_title="Analytics",
    layout="wide"
)

from src.ui import load_css

load_css()

SessionManager.initialize()

if not st.session_state.analysis_complete:

    st.warning("Please upload and analyze a dataset first.")

    st.stop()

insights = st.session_state.insights

df = st.session_state.prediction_df

st.title("📊 Business Analytics Dashboard")

# ===========================
# KPI CARDS
# ===========================

col1, col2, col3, col4 = st.columns(4)

col1.metric(
    "Total Customers",
    insights["Total Customers"]
)

col2.metric(
    "Likely to Churn",
    insights["Predicted Churn"]
)

col3.metric(
    "Retention",
    insights["Retention"]
)

col4.metric(
    "Churn Rate",
    f'{insights["Churn Rate"]}%'
)

st.divider()

# =====================================================
# ROW 1
# Prediction + Contract
# =====================================================

left, right = st.columns(2)

with left:

    st.subheader("Prediction Distribution")

    prediction_df = pd.DataFrame(
        {
            "Prediction": insights["Prediction Distribution"].keys(),
            "Count": insights["Prediction Distribution"].values()
        }
    )

    fig1 = px.pie(
        prediction_df,
        names="Prediction",
        values="Count",
        hole=0.4,
        title="Customer Churn Prediction"
    )

    st.plotly_chart(
        fig1,
        use_container_width=True
    )

with right:

    st.subheader("Contract Distribution")

    contract_df = pd.DataFrame(
        {
            "Contract": insights["Contract Distribution"].keys(),
            "Count": insights["Contract Distribution"].values()
        }
    )

    fig2 = px.bar(
        contract_df,
        x="Contract",
        y="Count",
        color="Contract",
        title="Customers by Contract Type"
    )

    st.plotly_chart(
        fig2,
        use_container_width=True
    )

# =====================================================
# ROW 2
# Internet + Payment
# =====================================================

left, right = st.columns(2)

with left:

    st.subheader("Internet Service Distribution")

    internet_df = pd.DataFrame(
        {
            "Service": insights["Internet Service Distribution"].keys(),
            "Count": insights["Internet Service Distribution"].values()
        }
    )

    fig3 = px.bar(
        internet_df,
        x="Service",
        y="Count",
        color="Service",
        title="Internet Service Distribution"
    )

    st.plotly_chart(
        fig3,
        use_container_width=True
    )

with right:

    st.subheader("Payment Method Distribution")

    payment_df = pd.DataFrame(
        {
            "Payment Method": insights["Payment Method Distribution"].keys(),
            "Count": insights["Payment Method Distribution"].values()
        }
    )

    fig4 = px.bar(
        payment_df,
        x="Payment Method",
        y="Count",
        color="Payment Method",
        title="Payment Methods"
    )

    st.plotly_chart(
        fig4,
        use_container_width=True
    )

# =====================================================
# ROW 3
# Monthly Charges + Tenure
# =====================================================

left, right = st.columns(2)

with left:

    st.subheader("Monthly Charges")

    fig5 = px.histogram(
        df,
        x="MonthlyCharges",
        nbins=30,
        title="Monthly Charges Distribution"
    )

    st.plotly_chart(
        fig5,
        use_container_width=True
    )

with right:

    st.subheader("Customer Tenure")

    fig6 = px.histogram(
        df,
        x="tenure",
        nbins=30,
        title="Customer Tenure"
    )

    st.plotly_chart(
        fig6,
        use_container_width=True
    )

st.divider()

# =====================================================
# HIGH RISK CUSTOMERS
# =====================================================

st.subheader("🔥 High Risk Customers")

high_risk = insights["High Risk Customers"]

st.dataframe(
    high_risk.head(20),
    use_container_width=True
)

st.divider()

# =====================================================
# DOWNLOAD
# =====================================================

csv = df.to_csv(index=False)

st.download_button(
    label="📥 Download Predictions",
    data=csv,
    file_name="customer_churn_predictions.csv",
    mime="text/csv"
)