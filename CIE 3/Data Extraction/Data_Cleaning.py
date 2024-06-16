import pandas as pd

# Load your dataset
data = pd.read_csv(r"D:\Study\Sem V\Lab\Big-Data-Analytics\CIE 3\Dataset\Uncleaned\merged_data.csv")

# Define a function to clean the 'video_id' column
def clean_video_id(video_id):
    # Use regular expressions to remove symbols and operators in front of the ID
    import re
    match = re.search(r'[^a-zA-Z0-9]*([\w-]+)$', video_id)
    if match:
        return match.group(1)
    return video_id  # Return the original value if no match is found

# Apply the cleaning function to the 'video_id' column
data['video_id'] = data['video_id'].apply(clean_video_id)

# Save the cleaned dataset
data.to_csv('cleaned_dataset.csv', index=False)  # Save to a new CSV file

print("Cleaning completed. Cleaned dataset saved as 'cleaned_dataset.csv'")
