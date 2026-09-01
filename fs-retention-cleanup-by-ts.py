import os
import sys
from datetime import datetime

MAX_INTERACTIONS = 100
MAX_ENTRIES = 100

CUTOFF_TIMESTAMP = datetime(2025, 1, 1).timestamp()

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
count_deleted_files = 0

while count_interactions < MAX_INTERACTIONS and index < len(all_files):
    count_entries = 0

    while count_entries < MAX_ENTRIES and index < len(all_files):
        entry = all_files[index]
        stats = entry.stat()
        file_mtime = stats.st_mtime
        readable_time = datetime.fromtimestamp(file_mtime).strftime('%Y-%m-%d %H:%M:%S')

        if file_mtime < CUTOFF_TIMESTAMP:
            file_path = os.path.join(file_path_arg, entry.name)
            print(f"{entry.name} | Removing (Modified: {readable_time})")
            os.remove(file_path)
            count_deleted_files +- 1
        else:
            print(f"{entry.name} | Keeping (Modified: {readable_time})")

        count_entries += 1
        index += 1

    print("-------------------")
    count_interactions += 1

print(f"{count_deleted_files} files were deleted")
