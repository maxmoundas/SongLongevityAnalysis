# This script removes all lines out of a cleaned csv except for the lines 
# representing one region

import pandas as pd

# Load the dataset
input_file_path = "datasets\cleaned_data.csv"
output_file_path = r"datasets\us_data.csv"
data = pd.read_csv(input_file_path)

# Filter rows where 'Region' is 'us'
filtered_data = data[data['Region'] == 'us']

# Save the filtered data back to a CSV or another desired format (optional)
filtered_data.to_csv(output_file_path, index=False)

print(f"Filtered data saved to {output_file_path}")
