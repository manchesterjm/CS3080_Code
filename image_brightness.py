"""
Image brightness analyzer and organizer.

This module analyzes image brightness and moves images exceeding a threshold
to a target folder for organization purposes.
"""

import os
import shutil

import numpy as np
from PIL import Image


def calculate_brightness(image_path: str) -> float:
    """
    Calculate the average brightness of an image.

    Args:
        image_path: Path to the image file

    Returns:
        float: Average brightness value (0-255)

    Example:
        >>> brightness = calculate_brightness('photo.jpg')
        >>> print(f"Brightness: {brightness:.2f}")
    """
    # Open the image file
    img = Image.open(image_path).convert('L')  # Convert image to grayscale
    # Convert the image to a numpy array
    img_array = np.array(img)
    # Calculate the average brightness
    brightness = np.mean(img_array)
    return brightness


def process_folder(folder_path: str, target_folder: str, brightness_threshold: float) -> int:
    """
    Process images in folder and move bright images to target folder.

    Args:
        folder_path: Source folder containing images
        target_folder: Destination folder for bright images
        brightness_threshold: Minimum brightness value for moving images

    Returns:
        int: Status code (0 for success)

    Example:
        >>> status = process_folder(r'C:\\Images', r'C:\\BrightImages', 125)
    """
    if not os.path.exists(target_folder):
        os.makedirs(target_folder)  # Create the target folder if it doesn't exist

    for filename in os.listdir(folder_path):
        if filename.endswith(('.jpg', '.png', '.jpeg', '.bmp', '.gif')):
            image_path = os.path.join(folder_path, filename)
            brightness = calculate_brightness(image_path)

            if brightness > brightness_threshold:
                shutil.move(image_path, os.path.join(target_folder, filename))
                print(f'Moved {filename} to {target_folder} due to brightness {brightness}')
            else:
                print(f'{filename} brightness is {brightness}, not moved.')

    return 0


def main() -> None:
    """
    Execute image brightness processing.

    Returns:
        None
    """
    source_folder = r'D:\Pictures\Wallpapers'
    target_folder = r'D:\Pictures\Back Up Wallpapers'
    brightness_threshold = 125

    process_folder(source_folder, target_folder, brightness_threshold)


if __name__ == '__main__':
    main()
