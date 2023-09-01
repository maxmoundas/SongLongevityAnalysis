# SongLongevityAnalysis

An application designed to analyze and predict the longevity of songs in various top-ranking brackets (e.g., top 3, 5, 10, 20, 50).

## Introduction

Dataset

- The dataset for this project is conveniently stored as a zip file within this repository.
- To use the dataset, please extract the zip file to the datasets directory.
- Source: https://www.kaggle.com/datasets/edumucelli/spotifys-worldwide-daily-song-ranking?resource=download

## Cross-Validation Results

My approach involved 10-fold cross-validation, with the following accuracy scores:
- Fold-1: 0.9644
- Fold-2: 0.9468
- Fold-3: 0.9612
- Fold-4: 0.9584
- Fold-5: 0.9512
- Fold-6: 0.9536
- Fold-7: 0.9608
- Fold-8: 0.9539
- Fold-9: 0.9610
- Fold-10: 0.9554

**Average Accuracy**: 0.9567 with a standard deviation of +/- 0.0052.

## Model Performance

### Training Data Performance

**Validation Accuracy**:  0.9628631124890477

Classification Report on Validation Data:

|                   | precision | recall | f1-score | support |
|-------------------|-----------|--------|----------|---------|
| 1-2 weeks         | 0.70      | 0.34   | 0.46     | 398     |
| less than a week  | 0.74      | 0.73   | 0.73     | 596     |
| more than 2 weeks | 0.98      | 0.99   | 0.98     | 13843   |

### Test Data Performance

**Test Accuracy**: 0.9615151310911909

|                   | precision | recall | f1-score | support |
|-------------------|-----------|--------|----------|---------|
| 1-2 weeks         | 0.71      | 0.32   | 0.44     | 436     |
| less than a week  | 0.71      | 0.70   | 0.71     | 525     |
| more than 2 weeks | 0.97      | 0.99   | 0.98     | 13876   |

## Model Explanation

The model predominantly excels in predicting songs that will sustain "more than 2 weeks" in top rankings, evidenced by both precision and recall. On the contrary, predicting songs lasting "1-2 weeks" poses challenges, potentially due to factors such as class imbalances.

It's noteworthy that while accuracy metrics are impressive, potential class imbalances may somewhat distort this. Thus, precision, recall, and F1-score per class are pivotal in ascertaining model efficacy.

## Limitations

1. **Dataset Time Range**: The dataset comprises data collected between Jan 1, 2017, to Jan 1, 2018. This range presents certain biases:
    - Songs popular before or after these dates might be inaccurately represented.
    - Songs gaining popularity within or immediately after this period might be overrepresented.
2. **Class Imbalance**: The dataset appears to have a significant number of songs that stayed popular "more than 2 weeks," potentially leading to overfitting in predictions towards this category.

## Recommendations

For further studies or refinements, consider:
- Gathering data beyond the current date range to capture broader trends.
- Applying advanced techniques like SMOTE or ADASYN to counteract class imbalances.
- Experimenting with different machine learning models to enhance prediction capabilities.

## Conclusion

SongLongevityAnalysis offers insights into the longevity trends of songs in top-ranking brackets. While achieving commendable accuracy, refinements addressing its limitations can further elevate its predictive capabilities.
