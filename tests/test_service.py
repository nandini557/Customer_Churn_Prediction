import pandas as pd

from src.services import ChurnAnalysisService


df = pd.read_csv("data/raw/Telco-Customer-Churn.csv")

service = ChurnAnalysisService()

result = service.analyze(df)

print(result["success"])

if result["success"]:
    print(result["data"].head())
    print(result["insights"])
else:
    print(result["missing_columns"])