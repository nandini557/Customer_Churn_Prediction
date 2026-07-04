import pandas as pd


class BusinessInsights:

    def generate(self, df):

        insights = {}

        # Basic KPIs
        insights["Total Customers"] = len(df)

        insights["Predicted Churn"] = (
            df["Prediction"] == "Yes"
        ).sum()

        insights["Retention"] = (
            df["Prediction"] == "No"
        ).sum()

        insights["Churn Rate"] = round(
            insights["Predicted Churn"] /
            insights["Total Customers"] * 100,
            2
        )

        # Additional Metrics
        insights["Average Monthly Charges"] = round(
            df["MonthlyCharges"].mean(),
            2
        )

        insights["Average Tenure"] = round(
            df["tenure"].mean(),
            2
        )

        # Data for charts
        insights["Contract Distribution"] = (
            df["Contract"]
            .value_counts()
            .to_dict()
        )

        insights["Internet Service Distribution"] = (
            df["InternetService"]
            .value_counts()
            .to_dict()
        )

        insights["Payment Method Distribution"] = (
            df["PaymentMethod"]
            .value_counts()
            .to_dict()
        )

        insights["Prediction Distribution"] = (
            df["Prediction"]
            .value_counts()
            .to_dict()
        )

        # High Risk Customers (> 80% probability)

        if "Churn Probability" in df.columns:

            insights["High Risk Customers"] = (
                df[df["Churn Probability"] >= 80]
                .sort_values(
                    by="Churn Probability",
                    ascending=False
                )
            )

        # Average Probability

        if "Churn Probability" in df.columns:

            insights["Average Risk"] = round(
                df["Churn Probability"].mean() * 100,
                2
            )

        return insights