#!/usr/bin/env python

import sys

current_video_id = None

for line in sys.stdin:
    video_id, _ = line.strip().split('\t')

    # If the current video_id is different from the previous one, emit it
    if video_id != current_video_id:
        if current_video_id:
            print(current_video_id)
        current_video_id = video_id

# Emit the last video_id if it exists
if current_video_id:
    print(current_video_id)
