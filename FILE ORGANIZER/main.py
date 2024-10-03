import tkinter as tk 
import os
from file_organizer import organize_files
root = tk.Tk()
root.title("My First GUI")
root.geometry("300x150")

def submit_function():
    address = entry.get()

    print("Address is :\t", address)
    if os.path.exists(address):
        organize_files(address)

def show_input():
    user_input = entry.get()
    print("User input:", user_input)
    label2 = tk.Label(root, text=user_input)
    label2.pack(pady=20)

label = tk.Label(root, text="Yogesh")
label.pack(pady=20)




entry = tk.Entry(root, width=30)
entry.pack(pady=5)

button = tk.Button(root, text="Submit", command=show_input)
button.pack(pady=10)

root.mainloop()
