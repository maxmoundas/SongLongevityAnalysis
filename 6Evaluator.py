import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import os
from sklearn.metrics import confusion_matrix, accuracy_score, precision_score, recall_score, f1_score, classification_report
from sklearn.model_selection import train_test_split
import joblib
from sklearn.ensemble import RandomForestClassifier

# Load the saved model
model_path = r'models\trained_model.pkl'
clf = joblib.load(model_path)

# Load the test data (if not loaded yet)
# If you saved the test set separately in step 5, you can load it here.
# Otherwise, you'd need to reproduce the test split exactly as before.
input_file_path = r"datasets\data_cleaned_us_processed_labeled.csv"
df = pd.read_csv(input_file_path)
X = df.drop(['LongevityLabel', 'Artist', 'TrackName', 'LabelGroup', 'Date', 'URL', 'Region'], axis=1)
y = df['LongevityLabel']

# Split the data to reproduce the test set
from sklearn.model_selection import train_test_split
_, X_test, _, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Make predictions on the test set
y_pred = clf.predict(X_test)

# Evaluate performance using various metrics
print("Test Accuracy: ", accuracy_score(y_test, y_pred))
print("Precision: ", precision_score(y_test, y_pred, average='weighted'))
print("Recall: ", recall_score(y_test, y_pred, average='weighted'))
print("F1 Score: ", f1_score(y_test, y_pred, average='weighted'))

# Classification report
print("\nClassification Report on Test Data:")
print(classification_report(y_test, y_pred))

# Confusion Matrix
import itertools
cm = confusion_matrix(y_test, y_pred)

# Ensure the visualizations directory exists
visualization_dir = 'visualizations'
if not os.path.exists(visualization_dir):
    os.makedirs(visualization_dir)

# Function to plot confusion matrix
def plot_confusion_matrix(cm, classes, normalize=False, title='Confusion matrix', cmap=plt.cm.Blues):
    """
    This function prints and plots the confusion matrix.
    Normalization can be applied by setting `normalize=True`.
    """
    if normalize:
        cm = cm.astype('float') / cm.sum(axis=1)[:, np.newaxis]
        print("Normalized confusion matrix")
    else:
        print('Confusion matrix, without normalization')

    plt.imshow(cm, interpolation='nearest', cmap=cmap)
    plt.title(title)
    plt.colorbar()
    tick_marks = np.arange(len(classes))
    plt.xticks(tick_marks, classes, rotation=45)
    plt.yticks(tick_marks, classes)

    fmt = '.2f' if normalize else 'd'
    thresh = cm.max() / 2.
    for i, j in itertools.product(range(cm.shape[0]), range(cm.shape[1])):
        plt.text(j, i, format(cm[i, j], fmt),
                 horizontalalignment="center",
                 color="white" if cm[i, j] > thresh else "black")

    plt.ylabel('True label')
    plt.xlabel('Predicted label')
    plt.tight_layout()

    # Save the figure
    plt.savefig(os.path.join(visualization_dir, 'confusion_matrix.png'))

# Plot non-normalized confusion matrix
class_names = y.unique()
plot_confusion_matrix(cm, classes=class_names, title='Confusion matrix, without normalization')
