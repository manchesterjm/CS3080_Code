import os
import shutil

def reorder_mp3_files(usb_path):
    """
    Attempts to reorder MP3 files on a USB drive in alphabetical order
    by physically rewriting directory entries. This sometimes helps
    older MP3 players that read track order from the FAT directory
    entry order rather than by filename.
    """
    # 1. Get all MP3 files (case-insensitive for .mp3)
    mp3_files = [f for f in os.listdir(usb_path) if f.lower().endswith('.mp3')]
    
    # 2. Sort them by name
    mp3_files.sort()
    
    # 3. Create a temporary folder to force new directory entries
    temp_folder = os.path.join(usb_path, "temp_reorder")
    if not os.path.exists(temp_folder):
        os.mkdir(temp_folder)
    
    # 4. Move the MP3s into the temp folder in alphabetical order
    #    WITHOUT changing the filenames:
    for filename in mp3_files:
        old_path = os.path.join(usb_path, filename)
        new_path = os.path.join(temp_folder, filename)
        shutil.move(old_path, new_path)
    
    # 5. Move the MP3s back to the root (usb_path) in alphabetical order
    #    so the final directory entries are re-created in sorted order
    reordered_files = sorted(os.listdir(temp_folder))
    for filename in reordered_files:
        old_path = os.path.join(temp_folder, filename)
        new_path = os.path.join(usb_path, filename)
        shutil.move(old_path, new_path)
    
    # 6. Remove the temp folder
    os.rmdir(temp_folder)

if __name__ == "__main__":
    # Replace this with your actual USB drive path
    # For Windows, something like: "E:\\"
    # For macOS/Linux, maybe: "/Volumes/USB_STICK"
    usb_drive_path = r"G:\\"
    
    reorder_mp3_files(usb_drive_path)
    print("Reordering complete. Safely eject the USB drive and test in your MP3 player.")
