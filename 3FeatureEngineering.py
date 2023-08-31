import pandas as pd
from sklearn.preprocessing import MinMaxScaler

# Load the Data
input_file_path = r"datasets\us_data.csv"
output_file_path = r"datasets\ranking_processed.csv"
df = pd.read_csv(input_file_path)

# Sort the dataset by Date and then by Position to ensure it's in chronological order
df.sort_values(by=['Date', 'Position'], inplace=True)
# Group the dataset by TrackName and Artist. This allows us to compute features specific to each song
grouped = df.groupby(['TrackName', 'Artist'])

# Feature Engineering

# 1. Artist Popularity
# Calculate how many songs by the same artist are in the top 200 on a given day
df['ArtistSongCount'] = df.groupby(['Date', 'Artist']).transform('count')['TrackName']
# Compute the average position of all songs by an artist over the past week
df['ArtistAvgPositionLastWeek'] = df.groupby(['Artist']).rolling(window=7)['Position'].mean().reset_index(0, drop=True)

# 2. Song Momentum
# Calculate the change in position from the previous day
df['ChangeInPosition'] = grouped['Position'].diff().fillna(0)
# Calculate the change in position from the previous day
df['AvgChangeInPositionLastWeek'] = grouped['Position'].diff().rolling(window=7).mean().reset_index(0, drop=True)
# Determine the number of days since the song first appeared in the top 200
df['DaysSinceEntry'] = grouped.cumcount() + 1

# 3. Historical Song Performance
# Define a custom function to compute the average song position over the last 7 days
# This function will be applied to each song's 'Position' series within its group
def song_avg_position_last_week(series):
    return series.rolling(window=7).mean()
# Define a custom function to compute the highest (smallest numerical value) position so far for a song
# This function will be applied to each song's 'Position' series within its group
def highest_position_so_far(series):
    return series.cummin()
# Using the `transform` method on the grouped 'Position' series, 
# apply the `song_avg_position_last_week` function to calculate the average position over the last 7 days
# The result retains the original DataFrame's index, ensuring there's no mismatch when creating a new column
df['SongAvgPositionLastWeek'] = grouped['Position'].transform(song_avg_position_last_week)
# Similarly, using the `transform` method on the grouped 'Position' series, 
# apply the `highest_position_so_far` function to determine the best position a song has achieved to date
# As with the previous step, the result retains the original DataFrame's index
df['HighestPositionSoFar'] = grouped['Position'].transform(highest_position_so_far)

# 4. Streaming Patterns
# Calculates the difference in streams from the previous day for each song.
# The first entry will have no previous data to compare with, so we fill it with 0 using fillna.
df['ChangeInStreams'] = grouped['Streams'].transform(lambda x: x.diff().fillna(0))
# Calculates the average streams for each song over the past 7 days. 
# Using the transform method ensures the output retains the same index as the original DataFrame.
df['AvgStreamsLastWeek'] = grouped['Streams'].transform(lambda x: x.rolling(window=7).mean())
# Calculates the ratio between the number of streams a song has and its position on the chart.
# A higher ratio might indicate a song's popularity in comparison to its chart position.
df['StreamsToPositionRatio'] = df['Streams'] / df['Position']

# 5. Temporal Features
# Convert the 'Date' column to a datetime dtype
df['Date'] = pd.to_datetime(df['Date'])
# Extract the day of the week from the 'Date' column. Monday is 0 and Sunday is 6.
df['DayOfWeek'] = df['Date'].dt.dayofweek
# Create a new binary column indicating if the day is a weekend (Saturday or Sunday).
df['IsWeekend'] = df['DayOfWeek'].isin([5, 6]).astype(int)

# Handle Missing Data
# Some of the derived features might have missing values, especially for songs that 
# just entered the chart. This step replaces any missing values (NaNs) with 0
df.fillna(0, inplace=True)

# Normalization
# Normalizing certain columns ensures that they are on a similar scale
# MinMaxScaler scales the values between 0 and 1. In this case, we're 
# scaling the Streams and StreamsToPositionRatio columns.
# The Streams column could have a wide range due to viral songs getting many more 
# streams than less popular ones. By normalizing this data, we help ensure that 
# models don't unduly prioritize the absolute number of streams in their 
# calculations.
# While the ratio may already bring Streams and Position to a more comparable 
# scale, the resultant ratio can still vary widely across songs and days. 
# Normalizing ensures that this feature's scale is consistent with other features 
# in the dataset.
# scaler = MinMaxScaler()
# df[['Streams', 'StreamsToPositionRatio']] = scaler.fit_transform(df[['Streams', 'StreamsToPositionRatio']])

# Save the processed dataset
df.to_csv(output_file_path, index=False)

print("Feature Engineering Completed!")
