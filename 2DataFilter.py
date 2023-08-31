# This script removes all lines out of a cleaned csv except for the lines 
# representing one region

import pandas as pd

# Load the dataset
input_file_path = "datasets\data_cleaned.csv"
output_file_path = r"datasets\data_cleaned_us.csv"
data = pd.read_csv(input_file_path)

# Filter rows where 'Region' is 'us'
filtered_data = data[data['Region'] == 'us']

# Save the filtered data back to a CSV or another desired format (optional)
filtered_data.to_csv(output_file_path, index=False)

print(f"\nData filtering completed. Saved to: '{output_file_path}'")
