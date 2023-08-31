# SongLongevityAnalysis
Analyze and predict how long songs stay in the top 3, 5, 10, 20, or 50 rankings.

The dataset used for this project is stored as a zip file in this repo. Extract the zip file to the datasets directory.

The dataset is sourced from: https://www.kaggle.com/datasets/edumucelli/spotifys-worldwide-daily-song-ranking?resource=download

## Limitations
The dataset only has data collected from Jan 1, 2017 to Jan 1, 2018. Thus, songs popular outside of the collection dates will 
likely be seen as less popular than they truly were, and songs popular in the middle of the collection date range (or released recently after 
Jan 1, 2017) will likely been seen as more popular than they truly were. This will impact the model, and will introduce bias.

### Training Data
Validation Accuracy:  0.9628631124890477

Classification Report on Validation Data:

|                   | precision | recall | f1-score | support |
|-------------------|-----------|--------|----------|---------|
| 1-2 weeks         | 0.70      | 0.34   | 0.46     | 398     |
| less than a week  | 0.74      | 0.73   | 0.73     | 596     |
| more than 2 weeks | 0.98      | 0.99   | 0.98     | 13843   |
| accuracy          |           |        | 0.96     | 14837   |
| macro avg         | 0.80      | 0.69   | 0.72     | 14837   |
| weighted avg      | 0.96      | 0.96   | 0.96     | 14837   |

Test Accuracy: 0.9615151310911909

### Classification Report on Test Data

|                   | precision | recall | f1-score | support |
|-------------------|-----------|--------|----------|---------|
| 1-2 weeks         | 0.71      | 0.32   | 0.44     | 436     |
| less than a week  | 0.71      | 0.70   | 0.71     | 525     |
| more than 2 weeks | 0.97      | 0.99   | 0.98     | 13876   |
| accuracy          |           |        | 0.96     | 14837   |
| macro avg         | 0.80      | 0.67   | 0.71     | 14837   |
| weighted avg      | 0.96      | 0.96   | 0.96     | 14837   |

Explained:

1. Validation Accuracy: 0.9628631124890477
This means that when the model made predictions on the validation set (which is a subset of the data it hasn't seen during training), it was correct about 96.29% of the time.

2. Classification Report on Validation Data:
The classification report gives detailed metrics on the performance of the classifier for each class:
Precision:
    1-2 weeks: 0.70 — Of all songs the model predicted to last 1-2 weeks on the charts, 70% actually did.
    less than a week: 0.74 — Of all songs the model predicted to last less than a week on the charts, 74% actually did.
    more than 2 weeks: 0.98 — Of all songs the model predicted to last more than 2 weeks on the charts, 98% actually did.
Recall:
    1-2 weeks: 0.34 — Of all songs that actually lasted 1-2 weeks on the charts, the model correctly predicted 34% of them.
    less than a week: 0.73 — Of all songs that actually lasted less than a week on the charts, the model correctly predicted 73% of them.
    more than 2 weeks: 0.99 — Of all songs that actually lasted more than 2 weeks on the charts, the model correctly predicted 99% of them.
F1-score:
The F1 score is the harmonic mean of precision and recall. It's a single metric that combines both precision and recall. An F1 score closer to 1 indicates better precision and recall balance, while an F1 score closer to 0 indicates poor balance.
    1-2 weeks: 0.46
    less than a week: 0.73
    more than 2 weeks: 0.98
The macro avg is the average of the metrics (precision, recall, F1-score) for each class without taking class distribution into account.
The weighted avg takes the class distribution into account when averaging the metrics. It's useful when there's a class imbalance.

3. Test Accuracy: 0.9615151310911909
This is the percentage of correct predictions the model made on the test set, another set of data it hasn't seen during training or validation. The model was correct about 96.15% of the time when predicting on the test set.

4. Classification Report on Test Data:
This report has the same structure as the report on the validation data, but it's evaluating the model's performance on the test set.

Summary:
The model is performing very well when predicting songs that will last "more than 2 weeks" on the charts, with both high precision and recall. However, it has a harder time predicting songs that will be on the charts for "1-2 weeks". This could be due to a variety of factors, such as class imbalance (which seems evident given the high count for "more than 2 weeks").
One thing to consider is that while accuracy is high, it might be misleading in the presence of class imbalance. This is because if most of the songs belong to the "more than 2 weeks" class, a model that simply predicts this class for every song would still achieve a high accuracy. Therefore, in such scenarios, precision, recall, and F1-score for each class become important metrics to evaluate model performance.
