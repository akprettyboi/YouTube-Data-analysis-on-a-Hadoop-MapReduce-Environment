#!/usr/bin/env python

import sys

for line in sys.stdin:
    # Split the input line into columns
    columns = line.strip().split(',')

    # Check if the line has the expected number of columns
    if len(columns) == 10:
        channel_name = columns[6]  
        view_count = int(columns[4])  

        # Emit the channel_name as the key and the view_count as the value
        print(f"{channel_name}\t{view_count}")
