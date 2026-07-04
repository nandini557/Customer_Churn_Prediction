import os
import joblib
import pandas as pd
import json

from sklearn.pipeline import Pipeline
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split

from sklearn.metrics import (
    accuracy_score,
    classification_report,
    confusion_matrix
)

from src.preprocess import DataPreprocessor


class ModelTrainer:
    def __init__(self):
        """Initialize project paths."""

        self.project_root = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

        self.data_path = os.path.join(
            self.project_root,
            "data",
            "raw",
            "Telco-Customer-Churn.csv"
        )

        self.artifacts_path = os.path.join(
            self.project_root,
            "artifacts"
        )

        os.makedirs(self.artifacts_path, exist_ok=True)

    def load_data(self):
        """Load dataset."""

        print("=" * 50)
        print("Loading Dataset...")
        print("=" * 50)

        df = pd.read_csv(self.data_path)

        print(f"Dataset Shape : {df.shape}")

        return df
    
    def inspect_data(self, df):
        """Inspect dataset."""

        print("\n" + "=" * 50)
        print("DATASET INSPECTION")
        print("=" * 50)

        print(f"\nRows: {df.shape[0]}")
        print(f"Columns: {df.shape[1]}")

        print("\nColumn Names:")
        print(df.columns.tolist())

        print("\nData Types:")
        print(df.dtypes)

        print("\nMissing Values:")
        print(df.isnull().sum())

        print("\nDuplicate Rows:", df.duplicated().sum())

    def train_model(self, df):
        """
        Train the churn prediction pipeline.
        """

        print("\n" + "=" * 50)
        print("MODEL TRAINING")
        print("=" * 50)

        X = df.drop("Churn", axis=1)
        y = df["Churn"]

        X_train, X_test, y_train, y_test = train_test_split(
            X,
            y,
            test_size=0.2,
            random_state=42,
            stratify=y
        )

        print(f"Training Samples : {len(X_train)}")
        print(f"Testing Samples  : {len(X_test)}")

        preprocessor = DataPreprocessor()

        transformer = preprocessor.create_preprocessor(X_train)

        pipeline = Pipeline(
            steps=[
                ("preprocessor", transformer),
                ("classifier", RandomForestClassifier(
                    n_estimators=200,
                    random_state=42
                ))
            ]
        )

        print("\nTraining Model...")

        pipeline.fit(X_train, y_train)

        print("Training Complete!")

        return pipeline, X_test, y_test
    
    def evaluate_model(self, pipeline, X_test, y_test):

        predictions = pipeline.predict(X_test)

        accuracy = accuracy_score(
            y_test,
            predictions
        )

        report = classification_report(
            y_test,
            predictions,
            output_dict=True
        )

        matrix = confusion_matrix(
            y_test,
            predictions
        )

        metrics = {

            "Accuracy": round(accuracy, 4),

            "Precision": round(
                report["weighted avg"]["precision"],
                4
            ),

            "Recall": round(
                report["weighted avg"]["recall"],
                4
            ),

            "F1 Score": round(
                report["weighted avg"]["f1-score"],
                4
            ),

            "Confusion Matrix": matrix.tolist()

        }

        reports_folder = os.path.join(
            self.project_root,
            "reports"
        )   

        os.makedirs(
            reports_folder,
            exist_ok=True
        )

        with open(

            os.path.join(
                reports_folder,
                "model_metrics.json"
            ),

        "w"

        ) as file:

            json.dump(
                metrics,
                file,
                indent=4
            )

        print("Model metrics saved.")

        return metrics

    def save_pipeline(self, pipeline):
        """
        Save trained pipeline.
        """

        save_path = os.path.join(
            self.artifacts_path,
            "customer_churn_pipeline.pkl"
        )

        joblib.dump(pipeline, save_path)

        print("\nPipeline Saved Successfully!")

        print(save_path)



def main():

    trainer = ModelTrainer()

    preprocessor = DataPreprocessor()

    df = trainer.load_data()

    trainer.inspect_data(df)

    df = preprocessor.clean_data(df)

    pipeline, X_test, y_test = trainer.train_model(df)

    metrics = trainer.evaluate_model(
        pipeline,
        X_test,
        y_test
    )

    trainer.save_pipeline(pipeline)


if __name__ == "__main__":
    main()