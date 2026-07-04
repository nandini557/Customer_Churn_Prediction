import pandas as pd

from sklearn.compose import ColumnTransformer
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import OneHotEncoder, StandardScaler


class DataPreprocessor:

    def clean_data(self, df):

        df = df.copy()

        if "customerID" in df.columns:
            df.drop(columns=["customerID"], inplace=True)

        if "TotalCharges" in df.columns:
            df["TotalCharges"] = pd.to_numeric(
                df["TotalCharges"],
                errors="coerce"
            )

            df["TotalCharges"] = df["TotalCharges"].fillna(
                df["TotalCharges"].median()
            )

        return df


    def create_preprocessor(self, X):

        categorical_columns = X.select_dtypes(
            include=["object"]
        ).columns.tolist()

        numerical_columns = X.select_dtypes(
            exclude=["object"]
        ).columns.tolist()

        preprocessor = ColumnTransformer(

            transformers=[

                (
                    "num",
                    StandardScaler(),
                    numerical_columns
                ),

                (
                    "cat",
                    OneHotEncoder(
                        handle_unknown="ignore"
                    ),
                    categorical_columns
                )

            ]

        )

        return preprocessor