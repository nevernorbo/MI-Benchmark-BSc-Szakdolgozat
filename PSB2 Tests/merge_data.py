import pandas as pd
import glob

"""
    Script to merge together the CSV files stored in the statistics folder.
"""

statistics = glob.glob('./statistics/*.csv')

dataframes = []

for filename in statistics:
    df = pd.read_csv(filename, index_col=None, header=0)
    dataframes.append(df)

# Concatenate all data into one DataFrame
frame = pd.concat(dataframes, axis=0, ignore_index=True)

# Save the merged DataFrame to a new CSV file
frame.to_csv('./statistics/all_data.csv', index=False)
