import os
import joblib
import sklearn

class ChurnPredictor:

    def __init__(self):

        print("=" * 60)
        print("Python executable:", os.sys.executable)
        print("scikit-learn version:", sklearn.__version__)
        print("=" * 60)

        project_root = os.path.dirname(
            os.path.dirname(os.path.abspath(__file__))
        )

        pipeline_path = os.path.join(
            project_root,
            "artifacts",
            "customer_churn_pipeline.pkl"
        )

        print("Pipeline exists:", os.path.exists(pipeline_path))
        print("Pipeline path:", pipeline_path)

        self.pipeline = joblib.load(pipeline_path)

    def predict(self, df):
        predictions = self.pipeline.predict(df)
        probabilities = self.pipeline.predict_proba(df)
        return predictions, probabilities[:, 1]