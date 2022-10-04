from tkinter import *
import os

def Restart():
    os.system("Shutdown /r /t 1")

def Restart_time():
    os.system("Shutdown /r /t 20")

def logout():
    os.system("shutdown -l")

def shutdown():
    os.system("Shutdown /s /t 1")

st = Tk()
st.title("SHUT-DOWN APP")
st.geometry("500x500")
st.config(bg="blue")


r_button = Button(st,text = "Restart", font=("Time New Roman",25,"bold"),
relief = RAISED,cursor = "plus",command=Restart)
r_button.place(x=150,y=60,height = 50,width=200)

rt_button = Button(st,text = "Restart Time", font=("Time New Roman",25,"bold"),
relief = RAISED,cursor = "plus",command=Restart_time)
rt_button.place(x=150,y=170,height = 50,width=200)

lg_button = Button(st,text = "Log-Out", font=("Time New Roman",25,"bold"),
relief = RAISED,cursor = "plus",command=logout)
lg_button.place(x=150,y=270,height = 50,width=200)
 
st_button = Button(st,text = "Shut-Down", font=("Time New Roman",25,"bold"),
relief = RAISED,cursor = "plus",command=shutdown)
st_button.place(x=150,y=370,height = 50,width=200)





st.mainloop()