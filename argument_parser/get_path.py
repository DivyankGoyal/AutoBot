import tkinter as tk
from tkinter import filedialog

def get_folder_path():
    root = tk.Tk()
    root.withdraw()

    folder_path = filedialog.askdirectory()
    return folder_path

def get_file_path():
    root = tk.Tk()
    root.withdraw()

    folder_path = filedialog.askopenfilename()
    return folder_path

if __name__ == "__main__":
    selected_folder = get_folder_path()
    print("Selected folder path:", selected_folder)
