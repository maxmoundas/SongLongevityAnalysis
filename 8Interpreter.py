import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import joblib
import warnings

# Suppress warnings
warnings.simplefilter(action='ignore', category=FutureWarning)

# Load the trained model from the 'models' directory
model_path = r"models\trained_model.pkl"
clf = joblib.load(model_path)

# Load your data for reference
input_file_path = r"datasets\data_cleaned_us_processed_labeled.csv"
df = pd.read_csv(input_file_path)

# 1. Analyze Feature Importance

# Fetching the feature importance from the model
feature_importances = clf.feature_importances_

# Create a dataframe for feature importance
feature_df = pd.DataFrame({
    'Feature': df.drop(['LongevityLabel', 'Artist', 'TrackName', 'LabelGroup', 'Date', 'URL', 'Region'], axis=1).columns,
    'Importance': feature_importances
})

# Sort the dataframe based on importance
feature_df = feature_df.sort_values(by='Importance', ascending=False)

# Plotting the features based on their importance
plt.figure(figsize=(12, 8))
sns.barplot(x='Importance', y='Feature', data=feature_df, palette="viridis")
plt.title('Feature Importance')
plt.tight_layout()
plt.savefig(r'visualizations\feature_importance.png')
plt.close()

# Here, instead of 'SongLength', choose an actual numeric column from your DataFrame.
# Example: If you have a column named 'SongDuration', replace 'SongLength' with 'SongDuration'.
feature_to_analyze = 'DaysSinceEntry' 

long_duration_songs = df[df['LongevityLabel'] == 'more than 2 weeks']

plt.figure(figsize=(10, 6))
sns.kdeplot(df[feature_to_analyze], label='All Songs', shade=True)
sns.kdeplot(long_duration_songs[feature_to_analyze], label='Long Duration Songs', shade=True)
plt.title(f'Distribution of {feature_to_analyze} for All Songs vs. Long Duration Songs')
plt.tight_layout()
plt.savefig(r'visualizations\specific_feature_distribution.png')
plt.close()

print("Visualizations saved in 'visualizations' directory.")
