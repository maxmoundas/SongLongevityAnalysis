import pandas as pd

# Load the dataset
input_file_path = "datasets\data.csv"
output_file_path = "datasets\data_cleaned.csv"
data = pd.read_csv(input_file_path)

# Display the first few rows
# print(data.head())

# Get an overview of the data types and non-null counts
# print(data.info())

# Get basic statistics for numerical columns
# print(data.describe())

# Check for missing values
# print("\nMissing values count per column:")
# print(data.isnull().sum())

# Drop rows with missing values
data.dropna(inplace=True)

# Count unique values for a given categorical column
# print(data['Region'].value_counts())

# Check for duplicates
# print(f"\nNumber of duplicate rows: {data.duplicated().sum()}")

# Drop duplicates
data.drop_duplicates(inplace=True)

# Convert the 'Date' column to datetime format
data['Date'] = pd.to_datetime(data['Date'])

# Save the cleaned dataset
data.to_csv(output_file_path, index=False)

print(f"\nData cleaning completed. Saved to: '{output_file_path}'")
