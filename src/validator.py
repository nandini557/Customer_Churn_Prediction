class DatasetValidator:

    REQUIRED_COLUMNS = [

        "gender",
        "SeniorCitizen",
        "Partner",
        "Dependents",
        "tenure",
        "PhoneService",
        "MultipleLines",
        "InternetService",
        "OnlineSecurity",
        "OnlineBackup",
        "DeviceProtection",
        "TechSupport",
        "StreamingTV",
        "StreamingMovies",
        "Contract",
        "PaperlessBilling",
        "PaymentMethod",
        "MonthlyCharges",
        "TotalCharges"

    ]

    def validate(self, df):

        missing = []

        for column in self.REQUIRED_COLUMNS:

            if column not in df.columns:
                missing.append(column)

        return missing