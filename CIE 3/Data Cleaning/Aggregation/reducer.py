#!/usr/bin/env python

import sys

current_channel = None
total_views = 0

for line in sys.stdin:
    channel, view_count = line.strip().split('\t')
    
    # If the current channel is different from the previous one, emit the total views
    if channel != current_channel:
        if current_channel:
            print(f"{current_channel}\t{total_views}")
        current_channel = channel
        total_views = 0

    total_views += int(view_count)

# Emit the last channel's total views if it exists
if current_channel:
    print(f"{current_channel}\t{total_views}")
