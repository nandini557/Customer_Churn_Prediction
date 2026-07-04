import pandas as pd

from src.validator import DatasetValidator
from src.preprocess import DataPreprocessor
from src.predictor import ChurnPredictor
from src.insights import BusinessInsights


class ChurnAnalysisService:

    def __init__(self):

        self.validator = DatasetValidator()
        self.preprocessor = DataPreprocessor()
        self.predictor = ChurnPredictor()
        self.insights = BusinessInsights()

    def analyze(self, df: pd.DataFrame):

        # Validate dataset
        missing_columns = self.validator.validate(df)

        if missing_columns:
            return {
                "success": False,
                "missing_columns": missing_columns
            }

        # Preserve customer IDs (if available)

        customer_ids = None

        if "customerID" in df.columns:
            customer_ids = df["customerID"].copy()

        # Clean dataset
        clean_df = self.preprocessor.clean_data(df)

        # Predict
        predictions, probabilities = self.predictor.predict(clean_df)

        # Create result dataframe
        result_df = clean_df.copy()

        result_df["Prediction"] = predictions
        result_df["Churn Probability"] = (
            probabilities * 100
        ).round(2)

        def get_risk(probability):

            if probability >= 80:
                return "High"

            elif probability >= 50:
                return "Medium"

            return "Low"


        result_df["Risk Level"] = result_df[
            "Churn Probability"
        ].apply(get_risk)

        # Add customer IDs back
        if customer_ids is not None:
            result_df.insert(0, "customerID", customer_ids)


        # Business Insights
        insights = self.insights.generate(result_df)

        return {
            "success": True,
            "data": result_df,
            "insights": insights
        }