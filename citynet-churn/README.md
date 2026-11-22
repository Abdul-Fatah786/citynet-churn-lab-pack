# CityNet Churn Baseline

## User story

As the retention manager, I want a weekly list of the 100 customers most likely to cancel next month, so my team can call them first.

## How to run

```bash
pip install -r requirements.txt

python src/lab7_save.py
python src/predict.py data/new_customers.csv
```

The prediction script writes the ranked results to `reports/predictions.csv`.

## Results (validation, then test once)

| Metric | Baseline | Our model |
|---|---:|---:|
| PR-AUC (validation) | 0.179 | 0.909 |
| Churners in top 100 (validation) | 18 | 49 |

**Test performance:** PR-AUC = 0.361 (recorded during the final evaluation).

## Intended use

- Help the customer retention team prioritize customers who may cancel their subscriptions.
- Generate a ranked list of the 100 highest-risk customers.
- Support proactive customer outreach and retention campaigns.
- Assist human decision-making by identifying customers who may need attention.

## Not for

- Automatically cancelling or modifying customer subscriptions.
- Making financial, contractual, or service decisions without human review.
- Treating predictions as guaranteed customer behaviour.
- Using predictions as the sole basis for denying services or changing customer benefits.

## Assumptions

- Historical customer data is representative of future customer behaviour.
- Input CSV files contain the required customer features.
- The target variable `churned` represents whether a customer actually cancelled.
- The model is retrained when new labelled customer data becomes available.
- Customer features are available before the prediction period begins.

## Risks and limitations

- Model performance may change as customer behaviour and business conditions change.
- The validation PR-AUC and final test PR-AUC differ significantly, indicating that further investigation is needed.
- Data leakage may inflate validation performance if features contain information recorded after a customer decides to cancel.
- Predictions may be inaccurate for customers whose behaviour differs from the training data.
- Regional or customer-group performance may vary.
- Human review is required before taking retention actions.
- Customer data must be handled securely and in accordance with applicable privacy requirements.
