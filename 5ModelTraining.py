import pandas as pd
from sklearn.model_selection import train_test_split, GridSearchCV
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, classification_report
import joblib  # For saving and loading the model
import os

# Load your data
input_file_path = r"datasets\data_cleaned_us_processed_labeled.csv"
df = pd.read_csv(input_file_path)

# Define features and target variable
X = df.drop(['LongevityLabel', 'Artist', 'TrackName', 'LabelGroup', 'Date', 'URL', 'Region'], axis=1)  # Removing non-numeric columns and the target
y = df['LongevityLabel']

# Split the data into training, validation, and test sets
# First, split into training + validation (80%) and test (20%)
X_train_val, X_test, y_train_val, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Further split training + validation into separate training (60%) and validation (20%) sets
X_train, X_val, y_train, y_val = train_test_split(X_train_val, y_train_val, test_size=0.25, random_state=42)

# Initialize a Random Forest classifier
clf = RandomForestClassifier(random_state=42)

# Define hyperparameters grid for tuning
param_grid = {
    'n_estimators': [50, 100, 150],
    'max_depth': [None, 10, 20, 30],
    'min_samples_split': [2, 5, 10],
    'min_samples_leaf': [1, 2, 4]
}

# Use GridSearchCV to find the best hyperparameters using the validation set
grid_search = GridSearchCV(clf, param_grid, cv=3, n_jobs=-1, verbose=2)

# Train the model using the training set
grid_search.fit(X_train, y_train)

# Use the model with the best hyperparameters found in the grid search
best_clf = grid_search.best_estimator_

# Save the trained model to the 'models' directory
if not os.path.exists('models'):  # Check if 'models' directory doesn't exist
    os.makedirs('models')         # If not, create it

model_save_path = 'models/trained_model.pkl'
joblib.dump(best_clf, model_save_path)
print(f"Model saved to {model_save_path}")

# Validate the model's performance on the validation set
y_val_pred = best_clf.predict(X_val)
print("Validation Accuracy: ", accuracy_score(y_val, y_val_pred))
print("Classification Report on Validation Data:")
print(classification_report(y_val, y_val_pred))

# At this point, we can further tune our model if needed, based on the validation performance.
# Once satisfied, the final step would be to evaluate the model on the test set.

y_test_pred = best_clf.predict(X_test)
print("Test Accuracy: ", accuracy_score(y_test, y_test_pred))
print("Classification Report on Test Data:")
print(classification_report(y_test, y_test_pred))
