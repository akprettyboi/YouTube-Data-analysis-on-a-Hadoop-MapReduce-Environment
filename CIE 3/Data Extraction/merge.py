import pandas as pd

# List of file names to merge
file_names = ["CIE 3/Dataset/Uncleaned/top_viewed_videos_AU.csv", 
              "CIE 3/Dataset/Uncleaned/top_viewed_videos_CA.csv", 
              "CIE 3/Dataset/Uncleaned/top_viewed_videos_DE.csv", 
              "CIE 3/Dataset/Uncleaned/top_viewed_videos_FR.csv", 
              "CIE 3/Dataset/Uncleaned/top_viewed_videos_IN.csv",
              "CIE 3/Dataset/Uncleaned/top_viewed_videos_US.csv"]

# Initialize an empty list to store DataFrames
data_frames = []

# Loop through the file names and read the data into DataFrames
for file_name in file_names:
    df = pd.read_csv(file_name)
    data_frames.append(df)

# Concatenate the DataFrames into a single DataFrame
merged_data = pd.concat(data_frames, ignore_index=True)

# Save the merged data to a new CSV file
merged_data.to_csv("merged_data.csv", index=False)

print("Merged data saved to 'merged_data.csv'")