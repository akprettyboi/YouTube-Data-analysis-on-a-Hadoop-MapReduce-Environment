import os
import googleapiclient.discovery
import pandas as pd

# Replace 'YOUR_API_KEY' with your actual YouTube API key
API_KEY = 'AAIzaSyAI8lGaJiOUXNfTU4mP_1udpxyVwqiRZbg'

# Create a YouTube API client
youtube = googleapiclient.discovery.build('youtube', 'v3', developerKey=API_KEY)

def get_top_videos(api, part, max_results, region_code):
    video_list = []
    next_page_token = None

    while len(video_list) < max_results:
        request = api.videos().list(
            part=part,
            chart="mostPopular",
            maxResults=min(50, max_results - len(video_list)),  # Fetch up to 50 results per page
            pageToken=next_page_token,
            regionCode=region_code
        )

        response = request.execute()
        videos = response.get('items', [])
        video_list.extend(videos)

        # Check if there are more pages of results
        next_page_token = response.get('nextPageToken')
        if not next_page_token:
            break

    return video_list

def create_video_dataset(video_list, region_name, region_code):
    dataset = []
    video_ids_added = set()

    for video in video_list:
        video_id = video["id"]

        if video_id not in video_ids_added:
            video_data = {
                "region_name": region_name,
                "region_code": region_code,
                "video_id": video_id,
                "title": video["snippet"]["title"],
                "channel_name": video["snippet"]["channelTitle"],
                "date_uploaded": video["snippet"]["publishedAt"],
                "view_count": video["statistics"]["viewCount"],
                "like_count": video["statistics"]["likeCount"],
            }
            dataset.append(video_data)
            video_ids_added.add(video_id)

    return dataset

# Specify the regions and their codes
regions = {
    "USA": "US",
    "India": "IN",
    "Australia": "AU",
    "Canada": "CA",
    "Germany": "DE",
    "France": "FR",
}

total_entries = 0  # Total entries across all regions
desired_total_entries = 2000

for region_name, region_code in regions.items():
    max_results_per_region = desired_total_entries - total_entries
    if max_results_per_region <= 0:
        break  # Stop if we've reached the desired total entries
    max_results_per_region = min(200, max_results_per_region)  # Limit to 200 per region

    video_list = get_top_videos(youtube, "snippet,statistics", max_results_per_region, region_code)
    total_entries += len(video_list)

    # Create datasets for all the retrieved videos
    dataset = create_video_dataset(video_list, region_name, region_code)

    # Create a DataFrame for the dataset
    df = pd.DataFrame(dataset)

    # Append the data to the CSV file or create a new one if it doesn't exist
    file_name = f"top_viewed_videos_{region_code}.csv"
    if not os.path.isfile(file_name):
        df.to_csv(file_name, index=False)
    else:
        df.to_csv(file_name, mode='a', header=False, index=False)
    print(f"Saved data for {region_name} ({region_code})")

    if total_entries >= desired_total_entries:
        break  # Stop if we've reached the desired total entries
