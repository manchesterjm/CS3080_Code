import os
import glob
import json

def replace_text_in_files(directory):
    # Get all .json files in the directory
    json_files = glob.glob(os.path.join(directory, '*.json'))
    
    # Loop through each file
    for file_path in json_files:
        # Read the JSON file
        with open(file_path, 'r', encoding='utf-8') as file:
            data = json.load(file)
        
        # Check if the "result" block contains "item" and replace it with "id"
        if 'result' in data and 'item' in data['result']:
            data['result']['id'] = data['result'].pop('item')
        
        # Write the modified content back to the file
        with open(file_path, 'w', encoding='utf-8') as file:
            json.dump(data, file, indent=4)
        print(f"Processed file: {file_path}")

# Specify the directory containing the .json files
directory = r'd:\Downloads\VanillaTweaks_c419099_MC1.20-1.20.4\data\slabs_stairs_to_block\recipes\stairs'

# Run the function
replace_text_in_files(directory)
