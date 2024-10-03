from file_downloader import download_file as download
import tkinter as tk

root = tk.Tk()
root.title("File Downloader")
root.geometry("500x200")


def buttonCall():
    url = urlInput.get()
    fname = filenameInput.get()
    print(f"Url:{url}\nFilename:{fname}")
    download(url,fname)
    

urlLabel = tk.Label(root, text="URL")
#url.pack(padx=10,pady=10)
urlLabel.grid(row=0,column=0)

urlInput = tk.Entry(root)
#urlInput.pack(padx=10,pady=10)
urlInput.grid(row=0,column=1)

filenameLabel = tk.Label(root,text="Filename")
filenameLabel.grid(row=1,column=0)

filenameInput =  tk.Entry(root)
filenameInput.grid(row=1,column=1)

downloadButton=tk.Button(root,text="Download",command=buttonCall)
downloadButton.grid(row=2,column=1)


root.mainloop()