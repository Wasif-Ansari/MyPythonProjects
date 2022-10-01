# for grphics need tkinter
#need speed test module

from tkinter import *
import speedtest

sp = Tk() #tkinter module creates
sp.title(" INTERNET SPEED TEST ") #name
sp.geometry("500x650") #size
sp.config(bg = "blue") #background using config

lab = Label(sp,text = "Internet Speed Test", font = ("Time New Roman",30,"bold","italic"),bg = "blue",fg = "White")
lab.place(x = 60 , y=40 , height=50 ,width=380)

lab = Label(sp,text = "Downloading Speed", font = ("Time New Roman",28,"bold","italic"))
lab.place(x = 60 , y=130, height=50 ,width=380)

lab = Label(sp,text = "00", font = ("Time New Roman",28,"bold","italic"))
lab.place(x = 60 , y=200, height=50 ,width=380)

lab = Label(sp,text = "Uploading Speed", font = ("Time New Roman",28,"bold","italic"))
lab.place(x = 60 , y=290, height=50 ,width=380)

lab = Label(sp,text = "00", font = ("Time New Roman",28,"bold","italic"))
lab.place(x = 60 , y=360, height=50 ,width=380)

button = Button(sp,text = "Run Test" , font = ("Time New Roman",28,"bold","italic") , relief=RAISED, bg = "red") 
#RAISED TO LOOK IN 3D
button.place(x = 60 , y=460, height=50 ,width=380)

sp.mainloop() #create window

