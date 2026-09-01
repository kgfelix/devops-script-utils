#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Module Name: fs-retention-cleanup-by-ts.py
Description: Delete files from a file system that were modified before a specific date.
Author: Kleber Felix
Version: 1.0.0
Date: 2026-09-o1
How to use: python3 fs-retention-cleanup-by-ts.py <folder_path>
"""

import os
import sys
from datetime import datetime

# Files modified before April 1, 2026 will be deleted
CUTOFF_TIMESTAMP = datetime(2026, 4, 1).timestamp()

if len(sys.argv) >= 2:
    file_path_arg = sys.argv[1]
    print(f'The file path is {file_path_arg}')
else:
    print('No file path provided.')
    sys.exit(1)

with os.scandir(file_path_arg) as entries:
    all_files = [entry for entry in entries if entry.is_file()]

count_deleted_files = 0

for entry in all_files:
    stats = entry.stat()
    file_mtime = stats.st_mtime
    readable_time = datetime.fromtimestamp(file_mtime).strftime('%Y-%m-%d %H:%M:%S')

    if file_mtime < CUTOFF_TIMESTAMP:
        file_path = os.path.join(file_path_arg, entry.name)
        print(f"{entry.name} | Removing (Modified: {readable_time})")
        os.remove(file_path)
        count_deleted_files += 1
    else:
        print(f"{entry.name} | Keeping (Modified: {readable_time})")

print(f"{count_deleted_files} files were deleted")
