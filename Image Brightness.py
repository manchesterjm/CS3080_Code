from PIL import Image
import numpy as np
import os
import shutil

def calculate_brightness(image_path):
    # Open the image file
    img = Image.open(image_path).convert('L')  # Convert image to grayscale
    # Convert the image to a numpy array
    img_array = np.array(img)
    # Calculate the average brightness
    brightness = np.mean(img_array)
    return brightness

def process_folder(folder_path, target_folder, brightness_threshold):
    if not os.path.exists(target_folder):
        os.makedirs(target_folder)  # Create the target folder if it doesn't exist

    for filename in os.listdir(folder_path):
        if filename.endswith(('.jpg', '.png', '.jpeg', '.bmp', '.gif')):  # Add more extensions if needed
            image_path = os.path.join(folder_path, filename)
            brightness = calculate_brightness(image_path)
            
            if brightness > brightness_threshold:
                shutil.move(image_path, os.path.join(target_folder, filename))
                print(f'Moved {filename} to {target_folder} due to brightness {brightness}')
            else:
                print(f'{filename} brightness is {brightness}, not moved.')

    return 0

# Example usage
source_folder = r'D:\Pictures\Wallpapers'
target_folder = r'D:\Pictures\Back Up Wallpapers'
brightness_threshold = 125

process_folder(source_folder, target_folder, brightness_threshold)
