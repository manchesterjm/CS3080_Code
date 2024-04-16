import os
#import shutil
import tkinter as tk
from tkinter import Toplevel, Label, Button, messagebox
from PIL import Image, ImageTk
import imagehash
from tempfile import NamedTemporaryFile
import time

def find_duplicates(directory):
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

def create_temp_image(original_path):
    temp_file = NamedTemporaryFile(delete=False, suffix='.png')
    with Image.open(original_path) as img:
        img.save(temp_file.name)
    return temp_file.name

def delete_image(image_path):
    try:
        os.remove(image_path)
        messagebox.showinfo("Delete Duplicate", f"Deleted {image_path}")
    except Exception as e:
        messagebox.showerror("Error", f"Failed to delete file: {e}")

def get_file_info(file_path):
    stat = os.stat(file_path)
    creation_time = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(stat.st_ctime))
    with Image.open(file_path) as img:
        resolution = img.size
    return resolution, creation_time

def display_images(image_path1, image_path2):
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
        if res1 > res2 or (res1 == res2 and date1 < date2):
            delete_image(image_path2)
        else:
            delete_image(image_path1)
        window.destroy()

    btn_delete = Button(window, text="Delete Lower Resolution or Newer", command=handle_delete)
    btn_delete.pack(side="bottom", pady=10)

    # Button to keep both images
    btn_keep = Button(window, text="Keep Both", command=lambda: window.destroy())
    btn_keep.pack(side="bottom", pady=10)

    window.mainloop()


def main(directory):
    duplicates = find_duplicates(directory)
    for dup in duplicates:
        display_images(dup[0], dup[1])

# Directory containing images
images_directory = r'D:\Pictures\Scans\New folder'
main(images_directory)
