import os
import re

def rename_files(directory):
  """
  Renames files in a given directory if their names start with 
  "nnn - " where 'nnn' is an integer.

  Args:
    directory: The directory path to process.
  """
  for filename in os.listdir(directory):
    filepath = os.path.join(directory, filename)
    if os.path.isfile(filepath):
      if re.match(r"^\d{3} - ", filename): 
        new_filename = filename[6:]  # Remove first 5 characters
        new_filepath = os.path.join(directory, new_filename)
        os.rename(filepath, new_filepath)
        # print(f"Renamed: {filename} to {new_filename}")

# Example usage:
directory_path = r"G:\\"  # Replace with the actual directory path
rename_files(directory_path)