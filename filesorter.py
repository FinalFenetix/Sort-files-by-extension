import tkinter as tk
from tkinter import filedialog as fd
import shutil
import os

directories = []
foldersToCreate = ['PDFs', 'PNGs', 'MP4s', 'MP3s', 'WAVs', 'ZIPs']

def create_folder(dir, name):
    try:
        newFolderPath = os.path.join(dir, name)

        os.makedirs(newFolderPath, exist_ok=True)
    
    except Exception as e:
        print(f"Yeah nahh I couldnt create a folder cuz {e}")

def file_in_directory(dir):
    try:
        files = [f for f in os.listdir(dir) if os.path.isfile(os.path.join(dir, f))]
        return files
    except Exception as e:
        print(f'Error accessing {dir}: {e}')

def open_file_dialog():
    folder = fd.askdirectory()
    if folder:
        print(f'Selected folder: {folder}')
    return folder

def organise_files():
    for f in allFiles:

        try:

            source_path = os.path.join(saveDir, f)
            if '.pdf' in f:
                shutil.move(source_path, directories[0])
            
            elif '.png' in f:
                shutil.move(source_path, directories[1])

            elif '.mp4' in f:
                shutil.move(source_path, directories[2])

            elif '.mp3' in f:
                shutil.move(source_path, directories[3])
            
            elif '.wav' in f:
                shutil.move(source_path, directories[4])
            
            elif '.zip' in f:
                shutil.move(source_path, directories[5])
            
            else:
                print(f'No valid directory for {f}')
            
        except Exception as e:
            print(f'An error occured when moving file {f} to {directories}')

if __name__ == "__main__":
    root = tk.Tk()
    root.withdraw()

    saveDir = open_file_dialog()

    count = 0
    for i in foldersToCreate:
        create_folder(saveDir, i)
        print(i)
        directories.append(os.path.join(saveDir, i))
        print(directories[count])
        count += 1
    
    allFiles = file_in_directory(saveDir)
    print(allFiles)
    organise_files()