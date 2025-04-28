import tkinter as tk
from tkinter import filedialog, messagebox
import os

def process_m3u_files(directory, old_path, new_path):
    converted_dir = os.path.join(directory, "Converted")
    os.makedirs(converted_dir, exist_ok=True)  # Ensure "Converted" directory exists

    for file_name in os.listdir(directory):
        if file_name.endswith(".m3u"):
            file_path = os.path.join(directory, file_name)
            converted_file = os.path.join(converted_dir, file_name)  # Save modified file in "Converted"
            
            with open(file_path, "r", encoding="utf-8") as file:
                lines = file.readlines()

            updated_lines = []
            
            for line in lines:
                if old_path in line:  # Check if the old path appears in the line
                    line = line.replace(old_path, new_path, 1)  # Replace only the first occurrence in this line
                line = line.replace("\\","/")    
                updated_lines.append(line)
            
            with open(converted_file, "w", encoding="utf-8") as file:
                file.writelines(updated_lines)

    messagebox.showinfo("Success", f"First occurrence per line replaced!\nSaved in '{converted_dir}'.")

def select_directory():
    directory = filedialog.askdirectory()
    entry_dir.delete(0, tk.END)
    entry_dir.insert(0, directory)

def start_process():
    directory = entry_dir.get()
    old_path = entry_old_path.get()
    new_path = entry_new_path.get()

    if directory and old_path and new_path:
        process_m3u_files(directory, old_path, new_path)
    else:
        messagebox.showwarning("Warning", "Please fill all fields!")

# GUI Setup
root = tk.Tk()
root.title("M3U First Occurrence Modifier")

tk.Label(root, text="Directory:").grid(row=0, column=0)
entry_dir = tk.Entry(root, width=50)
entry_dir.grid(row=0, column=1)
tk.Button(root, text="Browse", command=select_directory).grid(row=0, column=2)

tk.Label(root, text="Old Path:").grid(row=1, column=0)
entry_old_path = tk.Entry(root, width=50)
entry_old_path.grid(row=1, column=1)

#Hint /storage/6234-3335/Music/
tk.Label(root, text="New Path:").grid(row=2, column=0)
entry_new_path = tk.Entry(root, width=50)
entry_new_path.grid(row=2, column=1)

tk.Button(root, text="Start", command=start_process).grid(row=3, column=1)

root.mainloop()