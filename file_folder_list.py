import os
import csv
import tkinter as tk
from tkinter import filedialog, messagebox
from datetime import datetime

def timestamp_to_str(timestamp):
    return datetime.fromtimestamp(timestamp).strftime('%Y-%m-%d %H:%M:%S')

def get_all_file_paths_and_mac_times(directory):
    file_data = []
    for root, directories, files in os.walk(directory):
        for filename in files:
            filepath = os.path.join(root, filename)
            modified_time = timestamp_to_str(os.path.getmtime(filepath))
            accessed_time = timestamp_to_str(os.path.getatime(filepath))
            created_time = timestamp_to_str(os.path.getctime(filepath))
            file_data.append((filepath, "File", modified_time, accessed_time, created_time))
        
        for dirname in directories:
            dirpath = os.path.join(root, dirname)
            modified_time = timestamp_to_str(os.path.getmtime(dirpath))
            accessed_time = timestamp_to_str(os.path.getatime(dirpath))
            created_time = timestamp_to_str(os.path.getctime(dirpath))
            file_data.append((dirpath, "Directory", modified_time, accessed_time, created_time))
    return file_data

def save_to_csv(file_data, output_filename):
    with open(output_filename, 'w', newline='', encoding='cp949') as file:
        writer = csv.writer(file)
        writer.writerow(["Path", "Type", "Modified Time", "Accessed Time", "Created Time"])  # Writing header
        for data in file_data:
            writer.writerow(data)

def main():
    root = tk.Tk()
    root.withdraw()  # we don't want a full GUI, so keep the root window from appearing
    directory = filedialog.askdirectory()  # show an "Open" dialog box and return the path to the selected file
    if directory:  # if a directory is selected
        file_data = get_all_file_paths_and_mac_times(directory)
        save_to_csv(file_data, "output.csv")
        messagebox.showinfo("Success", "File paths and MAC times have been written to output.csv")

if __name__ == "__main__":
    main()
