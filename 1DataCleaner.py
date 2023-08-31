import pandas as pd

# Load the dataset
dirty_data_file_path = "datasets\data.csv"
clean_data_file_path = "datasets\cleaned_data.csv"
data = pd.read_csv(dirty_data_file_path)

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
print("\nRemoving rows with missing values")
data.dropna(inplace=True)

# Count unique values for a given categorical column
print(data['Region'].value_counts())

# Check for duplicates
# print(f"\nNumber of duplicate rows: {data.duplicated().sum()}")

# Drop duplicates
print("\nRemoving duplicate rows")
data.drop_duplicates(inplace=True)

# Convert the 'Date' column to datetime format
print("\nConverting values in 'Date' column to a datetime data type")
data['Date'] = pd.to_datetime(data['Date'])

# Save the cleaned dataset
print("\nSaving cleaned dataset")
data.to_csv(clean_data_file_path, index=False)

print(f"\nData cleaning completed and saved to '{clean_data_file_path}'")
