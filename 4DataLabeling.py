# This script first determines the days since the last appearance for each song. If the song disappears from the top 
# 200 and reappears later, we only consider the first sequence of consecutive appearances for labeling. It then calculates 
# the longevity label based on this sequence.

import pandas as pd

# Read the dataset
input_file_path = r"datasets\ranking_processed.csv"
output_file_path = r"datasets\labeled.csv"
df = pd.read_csv(input_file_path)

# Convert the 'Date' column to datetime format
df['Date'] = pd.to_datetime(df['Date'])

# Sort the dataframe by 'Artist', 'TrackName', and 'Date'
df = df.sort_values(by=['Artist', 'TrackName', 'Date'])

# Group by 'Artist' and 'TrackName' and then find the difference in days for each song's appearance
df['DaysSinceLastAppearance'] = df.groupby(['Artist', 'TrackName'])['Date'].diff().dt.days.fillna(0)

# For each song, if it disappears from the top 200 and then reappears, 
# we consider the first sequence of appearances for labeling
df['IsConsecutive'] = (df['DaysSinceLastAppearance'] <= 1).astype(int)
df['BreakPoint'] = ((df['DaysSinceLastAppearance'] > 1) & (df['IsConsecutive'].shift(fill_value=0) == 1)).astype(int)
df['LabelGroup'] = df.groupby(['Artist', 'TrackName'])['BreakPoint'].cumsum()

# Now, we'll compute the label for each song based on its longest sequence of consecutive appearances
# 1. Retain the DataFrame structure after using cumcount():
df['CumCount'] = df.groupby(['Artist', 'TrackName', 'LabelGroup']).cumcount()

# 2. Use groupby with the desired columns and extract the max values:
longevity_max = df.groupby(['Artist', 'TrackName'])['CumCount'].max()

# 3. Merge the extracted labels back with the original DataFrame:
df = df.merge(longevity_max, on=['Artist', 'TrackName'], suffixes=('', '_Max'))

# Assigning multi-class labels as before:
def assign_label(days):
    if days < 7:
        return "less than a week"
    elif 7 <= days < 14:
        return "1-2 weeks"
    else:
        return "more than 2 weeks"

df['LongevityLabel'] = df['CumCount_Max'].apply(assign_label)

# Remove auxiliary columns
df.drop(['CumCount', 'CumCount_Max'], axis=1, inplace=True)

# Saving the labeled dataset
df.to_csv(output_file_path, index=False)
