import pandas as pd

df = pd.read_csv("data/citynet_churn.csv")

print(f"data frame shape : " , df.shape)
print(df.dtypes.value_counts().to_dict())
missing = df.isna().sum()
print(missing[missing > 0].to_dict())
print(f"churned values count: ",df["churned"].value_counts(normalize=True).round(3).to_dict())
print(f"",df[["tenure_months", "support_calls_90d", "outage_hours_90d"]].describe().loc[["mean", "min", "max"]].round(1))
print(df.groupby("support_calls_90d")["churned"].mean().round(2).head(6).to_dict())
print(df.groupby("cancel_request_logged")["churned"].mean().round(3).to_dict())

# TODO 1 ANSWER:
# payment_method has 149 missing values.
# age has 411 missing values.

# TODO 2 ANSWER:
# 17.9% of customers churned and 82.1% did not churn.
# The dataset is imbalanced because the classes are not equally distributed.

# TODO 3 ANSWER:
# cancel_request_logged predicts churn almost perfectly.
# We must exclude it because it causes data leakage.
# It contains information about cancellation that may not be available
# when we want to predict future churn.
