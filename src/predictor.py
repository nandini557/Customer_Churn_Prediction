class ChurnPredictor:
    """
    Temporary predictor for deployment testing.
    This bypasses loading the model pipeline.
    """

    def __init__(self):
        self.pipeline = None

    def predict(self, df):
        # Return dummy predictions
        predictions = ["No"] * len(df)
        probabilities = [0.0] * len(df)

        return predictions, probabilities