import os

def file_exists(file) :
    if os.path.exists(file) :
        print(f"your file {file} exists")
        print(f"removing {file} now")
        os.remove(file)
    else :
        print(f"{file} not found on your computer")
    
file_1 = open("test.txt", "w")
file_1.close()

file_exists("test.txt")