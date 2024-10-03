import os
import tkinter as tk
import itertools

# Function to organize files based on their types
def organize_files(directory):
    assert os.path.exists(directory), "Path does not exist"
    
    # Define file categories
    file_types = {
        'Videos': ['.mp4', '.mkv', '.avi', '.mov'],
        'Audios': ['.mp3', '.wav', '.aac', '.flac'],
        'Images': ['.jpg', '.jpeg', '.png', '.gif', '.bmp'],
        'Documents': ['.pdf', '.doc', '.docx', '.xls', '.xlsx', '.ppt', '.pptx', '.txt'],
        'Misc': []
    }
    
    # Create folders for categories if they don't exist
    for folder in file_types.keys():
        folder_path = os.path.join(directory, folder)
        if not os.path.exists(folder_path):
            os.makedirs(folder_path)
    
    # Organize files into the respective folders
    for file_name in os.listdir(directory):
        file_path = os.path.join(directory, file_name)
        if os.path.isdir(file_path):
            continue  # Skip directories

        file_extension = os.path.splitext(file_name)[1].lower()

        moved = False
        for folder, extensions in file_types.items():
            if file_extension in extensions:
                destination = os.path.join(directory, folder, file_name)
                if not os.path.exists(destination):
                    os.rename(file_path, destination)
                moved = True
                break
        
        # If no matching category is found, move to 'Misc'
        if not moved:
            misc_destination = os.path.join(directory, 'Misc', file_name)
            if not os.path.exists(misc_destination):
                os.rename(file_path, misc_destination)

    print("Files have been organized!")

# Function to handle user input and organize files
def show_input():
    user_input = entry.get()
    if os.path.exists(user_input):
        organize_files(user_input)
        label2.config(text="Files have been organized!")
    else:
        label2.config(text="Invalid directory path!")

# Function to change background color every second
def change_background_color():
    color = next(color_cycle)
    root.configure(bg=color)
    root.after(1000, change_background_color)  # Schedule color change every 1000 ms (1 second)

# Create main window
root = tk.Tk()
root.title("File Organizer")
root.geometry("300x200")

# Create label, entry, button, and result label
label = tk.Label(root, text="File Organizer", font=("Helvetica", 16), bg="white")
label.pack(pady=10)
entry = tk.Entry(root, width=30)
entry.pack(pady=5)
button = tk.Button(root, text="Organize", command=show_input)
button.pack(pady=10)
label2 = tk.Label(root, text="")
label2.pack(pady=10)

# Define a list of background colors and an iterator to cycle through them
colors = ['lightblue', 'lightgreen', 'lightyellow', 'lightpink', 'lightgray']
color_cycle = itertools.cycle(colors)

# Start changing the background color
change_background_color()

# Run the Tkinter event loop
root.mainloop()
