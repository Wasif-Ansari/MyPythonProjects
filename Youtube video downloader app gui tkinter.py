from multiprocessing.pool import IMapIterator
from pytube import YouTube
from tkinter import *
from tkinter import ttk
from PIL import ImageTk,Image

def data_get():
    link = entry.get()
    youtube_1 = YouTube(link)
    #print(youtube_1.title)
    #print(youtube_1.thumbnail_url)

    videos = youtube_1.streams.all() #get all stream options
    #videos = youtube_1.streams.filter(only_audio=True) #for only audioṇ
    vid = list(enumerate(videos)) #indexing
    ans=""
    for i in vid:
        mylist.insert(END,str(i))
        
def dstart():
    link = entry.get()
    youtube_1 = YouTube(link)
    videos = youtube_1.streams.all()
    q = mylist.get(ANCHOR)
    print(q[1])

    #stream = int(input("Enter Quality index: "))
    print("Downlaoding....")
    videos[int(q[1])].download()
    print("Successfully Downloaded ")


win = Tk()
win.title("Youtube downloader")
win.config(bg="green")
win.geometry("800x600") # width x height

my_img = ImageTk.PhotoImage(Image.open("download.png"))
name = Label(win,text=" YOUTUBE VIDEO DOWNLOADER ",font=("Time New Roman",30,"bold"))
name.place(x=25, y=50,height=50,width=750)

# link_input = Text(win, height = 10,
#                 width = 25,
#                 bg = "light yellow")
# link_input.place(x=25,y=140,height=50,width=450)

entry = Entry(win,font=("Times New Roman", 15, "bold"))
entry.place(x=25,y=140,height=50,width=600)

go_button = Button(win,text="GO>>",font=("Time New Roman",30,"bold"),command=data_get)
go_button.place(x=650,y=140,height=50,width=110)

# quality = Label(win,text="None",font=("Times New Roman",10,"bold" ),bg="white",fg="blue")
# quality.place(x=25,y=220,height=300,width=750)

mylist = Listbox(win)
mylist.place(x=25,y=220,height=300,width=750)

download_button = Button(win,text="DOWNLOAD",image=my_img,font=("Time New Roman",30,"bold"),command=dstart)
download_button.place(x=275,y=540,height=50,width=250)

win.mainloop()