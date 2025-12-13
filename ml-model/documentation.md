<h4>Using the suggested Isolation Forest model, I conclude the following:</h4>

1. Hard to get proper data in order to train AI-Model.
2. According to the data file, we have in total 10000 cases, out of which we tested 4000 (3804 normal users, 196 anomalies).
3. The current AI-Model has very low accuracy!

Reason:

- Only 95.5% of normal users were predicted correctly as normal activity!
- 4.5% of normal users were predicted wrongly as anomalies!!!
- Only 5.6% of anomalies were predicted correctly as anomalies!
- 94.4% of anomalies were very wrongly predicted as normal!!!

Result:
- Most of anomalies were not predicted!

What to do: 
- Model not suitable in our case
- Solution given in features_plan.md