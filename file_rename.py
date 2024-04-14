import os
from datetime import datetime
import re

# Specify the directory containing the files
directory = r'D:\Pictures\Scans\New folder'

# Define a regular expression pattern that matches the datetime format in the filenames
pattern = re.compile(r'^\d{4}-\d{2}-\d{2}_\d{2}-\d{2}-\d{2}')

# Dictionary to count files by date
date_count = {}

# Total files count
total_files = 0

# Loop through all files in the directory
for filename in os.listdir(directory):
    total_files += 1  # Increment total files count

    # Get the full file path
    old_file = os.path.join(directory, filename)

    # Skip if it's a directory
    if os.path.isdir(old_file):
        continue

    # Get the last modified time of the file
    mod_time = os.path.getmtime(old_file)

    # Convert it to a datetime object
    date_time = datetime.fromtimestamp(mod_time)

    # Extract just the date part
    date_key = date_time.strftime('%Y-%m-%d')

    # Increment the count for this date
    if date_key in date_count:
        date_count[date_key] += 1
    else:
        date_count[date_key] = 1

    # Check if the filename already matches the datetime pattern
    if pattern.match(filename):
        # print(f'Skipped renaming "{filename}" as it is already in the correct format.')
        continue

    # Format the datetime object as a string in the desired format
    new_filename = date_time.strftime('%Y-%m-%d_%H-%M-%S')

    # Generate new file path with the same extension as the original file
    file_extension = os.path.splitext(filename)[1]
    new_file = os.path.join(directory, new_filename + file_extension)

    # Rename the file
    os.rename(old_file, new_file)
    print(f'Renamed "{old_file}" to "{new_file}"')

# Output the results
print(f'Total number of files in the directory: {total_files}')
print("Files downloaded per day:")
for date, count in sorted(date_count.items()):
    print(f"{date}: {count} files")
