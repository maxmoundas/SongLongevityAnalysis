import pandas as pd
from sklearn.model_selection import train_test_split, cross_val_score
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import make_scorer, accuracy_score

# Load the data
input_file_path = r"datasets\data_cleaned_us_processed_labeled.csv"
df = pd.read_csv(input_file_path)

# Define features and target variable
X = df.drop(['LongevityLabel', 'Artist', 'TrackName', 'LabelGroup', 'Date', 'URL', 'Region'], axis=1)
y = df['LongevityLabel']

# Initialize a Random Forest classifier
# Here, we're assuming you want to use the RandomForest as the model for cross-validation. 
# This can be replaced or tuned as needed.
clf = RandomForestClassifier(random_state=42, n_estimators=100)

# Implement k-fold cross-validation
# The most commonly used k value is 10, but you can adjust it to your preference.
k = 10

# We use 'accuracy' as a performance metric. 
# You can include other metrics like precision, recall, f1-score as required.
# Here, we are using the `cross_val_score` method which provides the scores for each fold.
scores = cross_val_score(clf, X, y, cv=k, scoring=make_scorer(accuracy_score))

# Display the scores
print(f"Accuracy scores for the {k}-fold cross-validation:")
for i, score in enumerate(scores, 1):
    print(f"Fold-{i}: {score:.4f}")

# Display the average score
print(f"\nAverage Accuracy from {k}-fold cross-validation: {scores.mean():.4f} +/- {scores.std():.4f}")

