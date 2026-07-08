import os
import joblib
import pandas as pd


class ChurnPredictor:
    """
    Loads the trained pipeline and performs predictions.
    """

    def __init__(self):

        project_root = os.path.dirname(
            os.path.dirname(os.path.abspath(__file__))
        )

        pipeline_path = os.path.join(
            project_root,
            "artifacts",
            "customer_churn_pipeline.pkl"
        )

        self.pipeline = joblib.load(pipeline_path)

    def predict(self, df):

        predictions = self.pipeline.predict(df)

        probabilities = self.pipeline.predict_proba(df)

        return predictions, probabilities[:, 1]