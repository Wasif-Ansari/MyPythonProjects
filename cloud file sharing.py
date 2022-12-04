import gofile as go
import tkinter as tk
from tkinter import filedialog

root = tk.Tk()
root.withdraw()
file_path = filedialog.askopenfilename()


def storefiles(file):
    cur_server = go.getServer()
    print(cur_server)
    url = go.uploadFile(file)
    print("Download Link : ", url["downloadPage"])

storefiles(file_path)