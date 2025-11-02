"""
Duplicate image finder and manager with GUI.

This module finds duplicate images using perceptual hashing and provides
a GUI for viewing and managing duplicates based on resolution and creation date.
"""

import os
import time
from tempfile import NamedTemporaryFile
from tkinter import Button, Label, Toplevel, messagebox
import tkinter as tk

import imagehash
from PIL import Image, ImageTk


def find_duplicates(directory: str) -> list[tuple[str, str]]:
    """
    Find duplicate images in a directory using average hashing.

    Args:
        directory: Path to directory containing images

    Returns:
        list: List of tuples containing (duplicate_path, original_path)

    Example:
        >>> duplicates = find_duplicates(r'C:\\\\Pictures')
        >>> print(f"Found {len(duplicates)} duplicates")
    """
    hashes = {}
    duplicates = []
    # Scan all files in the directory
    for filename in os.listdir(directory):
        file_path = os.path.join(directory, filename)
        if os.path.isfile(file_path) and filename.lower().endswith(('.png', '.jpg', '.jpeg')):
            with Image.open(file_path) as img:
                img_hash = imagehash.average_hash(img.convert('L'))
                if img_hash in hashes:
                    duplicates.append((file_path, hashes[img_hash]))
                else:
                    hashes[img_hash] = file_path
    return duplicates


def create_temp_image(original_path: str) -> str:
    """
    Create a temporary copy of an image.

    Args:
        original_path: Path to original image file

    Returns:
        str: Path to temporary image file

    Example:
        >>> temp_path = create_temp_image('original.jpg')
    """
    with NamedTemporaryFile(delete=False, suffix='.png') as temp_file:
        with Image.open(original_path) as img:
            img.save(temp_file.name)
        return temp_file.name


def delete_image(image_path: str) -> None:
    """
    Delete an image file with error handling.

    Args:
        image_path: Path to image file to delete

    Returns:
        None
    """
    try:
        os.remove(image_path)
        messagebox.showinfo("Delete Duplicate", f"Deleted {image_path}")
    except (OSError, PermissionError) as e:
        messagebox.showerror("Error", f"Failed to delete file: {e}")


def get_file_info(file_path: str) -> tuple[tuple[int, int], str]:
    """
    Get image resolution and creation time.

    Args:
        file_path: Path to image file

    Returns:
        tuple: ((width, height), creation_time_string)

    Example:
        >>> resolution, created = get_file_info('image.jpg')
        >>> print(f"Resolution: {resolution}, Created: {created}")
    """
    stat = os.stat(file_path)
    creation_time = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(stat.st_ctime))
    with Image.open(file_path) as img:
        resolution = img.size
    return resolution, creation_time


def display_images(image_path1: str, image_path2: str) -> None:  # pylint: disable=too-many-locals
    """
    Display two images side-by-side with options to manage duplicates.

    Args:
        image_path1: Path to first image
        image_path2: Path to second image

    Returns:
        None
    """
    # Create temporary images for display
    temp_image_path1 = create_temp_image(image_path1)
    temp_image_path2 = create_temp_image(image_path2)

    # Get image info
    res1, date1 = get_file_info(image_path1)
    res2, date2 = get_file_info(image_path2)

    # Create a new window
    window = Toplevel()
    window.title("Duplicate Images")

    # Load the two images
    img1 = Image.open(temp_image_path1)
    img2 = Image.open(temp_image_path2)

    # Resize for display if needed
    img1 = img1.resize((250, 250), Image.Resampling.LANCZOS)
    img2 = img2.resize((250, 250), Image.Resampling.LANCZOS)

    # Convert to PhotoImage
    img1 = ImageTk.PhotoImage(img1)
    img2 = ImageTk.PhotoImage(img2)

    # Frame for first image and its info
    frame1 = tk.Frame(window)
    frame1.pack(side="left", padx=10, pady=10)
    label1 = Label(frame1, image=img1)
    label1.image = img1  # keep a reference
    label1.pack()
    info1 = Label(frame1, text=f"Resolution: {res1}, Created: {date1}")
    info1.pack()

    # Frame for second image and its info
    frame2 = tk.Frame(window)
    frame2.pack(side="right", padx=10, pady=10)
    label2 = Label(frame2, image=img2)
    label2.image = img2  # keep a reference
    label2.pack()
    info2 = Label(frame2, text=f"Resolution: {res2}, Created: {date2}")
    info2.pack()

    # Button to delete the lower-resolution image or newer if same resolution
    def handle_delete():
        """Handle deletion of lower quality or newer duplicate."""
        if res1 > res2 or (res1 == res2 and date1 < date2):
            delete_image(image_path2)
        else:
            delete_image(image_path1)
        window.destroy()

    btn_delete = Button(window, text="Delete Lower Resolution or Newer", command=handle_delete)
    btn_delete.pack(side="bottom", pady=10)

    # Button to keep both images
    def handle_keep():
        """Handle keeping both images (no deletion)."""
        window.destroy()

    btn_keep = Button(window, text="Keep Both", command=handle_keep)
    btn_keep.pack(side="bottom", pady=10)

    window.mainloop()


def main(directory: str) -> None:
    """
    Find and display duplicate images for user review.

    Args:
        directory: Path to directory to scan for duplicates

    Returns:
        None
    """
    duplicates = find_duplicates(directory)
    for dup in duplicates:
        display_images(dup[0], dup[1])


if __name__ == '__main__':
    # Directory containing images
    IMAGES_DIRECTORY = r'D:\Pictures\Scans\New folder'
    main(IMAGES_DIRECTORY)
