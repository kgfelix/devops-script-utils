#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Module Name: fs-retention-cleanup-by-year.py
Description: Deletes files from a specific filesystem folder that are older than the configured year.
Author: Kleber Felix
Version: 1.0.0
Date: 2026-08-27
How to use: python3 fs-retention-cleanup.py <folder_path>
"""

import os
import sys
from datetime import datetime

MAX_INTERACTIONS = 10 # number of batches
MAX_ENTRIES = 10 # number of files per batch
NOT_REMOVE_THIS_YEAR = [2025, 2026]

if len(sys.argv) >= 2:
    file_path_arg = sys.argv[1]
    print(f'The file path is {file_path_arg}')
else:
    print('No file path provided.')
    sys.exit(1)

with os.scandir(file_path_arg) as entries:
    all_files = [entry for entry in entries if entry.is_file()]

count_interactions = 0
index = 0

while count_interactions < MAX_INTERACTIONS and index < len(all_files):
    count_entries = 0

    while count_entries < MAX_ENTRIES and index < len(all_files):
        entry = all_files[index]
        stats = entry.stat()
        mod_year = datetime.fromtimestamp(stats.st_mtime).year

        if mod_year not in NOT_REMOVE_THIS_YEAR:
            file_path = os.path.join(file_path_arg, entry.name)
            print(f"{entry.name} | Removing: {mod_year}")
            os.remove(file_path)
        else:
            print(f"{entry.name} | Keeping: {mod_year}")

        count_entries += 1
        index += 1

    print("-------------------")
    count_interactions += 1
