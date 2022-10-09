from tkinter import *
import datetime

def date_time():
    time = datetime.datetime.now()
    hr = time.strftime("%I") #gives us hours
    mn = time.strftime("%M") #minutes
    sc = time.strftime("%S")
    am = time.strftime("%p")

    date = time.strftime("%d")
    month = time.strftime("%m")
    year = time.strftime("%y")
    day = time.strftime("%a")

    hour.config(text=hr)
    minute.config(text=mn)
    secs.config(text=sc)
    ampm.config(text=am)
    datelab.config(text=date)
    monthlab.config(text=month)
    yearlab.config(text=year)
    daylab.config(text=day)

    hour.after(200,date_time) #recalling to change every second
    

clock = Tk()
clock.title("     **** Digital Clock ****")
clock.geometry("1000x500")
clock.config(bg="Blue")

hour = Label(clock, text="00", font=("Times New Roman",40,"bold"),
bg='white', fg='black')
hour.place(x=120,y=50,height=110,width=100)

hour_txt = Label(clock, text="HOURS", font=("Times New Roman",20,"bold"),
bg='white', fg='black')
hour_txt.place(x=120,y=190,height=30,width=100)

minute = Label(clock, text="00", font=("Times New Roman",40,"bold"),
bg='white', fg='black')
minute.place(x=340,y=45,height=110,width=100)

minute_txt = Label(clock, text="MIN", font=("Times New Roman",20,"bold"),
bg='white', fg='black')
minute_txt.place(x=340,y=190,height=30,width=100)

secs = Label(clock, text="00", font=("Times New Roman",40,"bold"),
bg='white', fg='black')
secs.place(x=560,y=45,height=110,width=100)

secs_txt = Label(clock, text="SECS", font=("Times New Roman",20,"bold"),
bg='white', fg='black')
secs_txt.place(x=560,y=190,height=30,width=100)

ampm = Label(clock, text="00", font=("Times New Roman",40,"bold"),
bg='white', fg='black')
ampm.place(x=780,y=45,height=110,width=100)

ampm_txt = Label(clock, text="AM/PM", font=("Times New Roman",20,"bold"),
bg='white', fg='black')
ampm_txt.place(x=780,y=190,height=30,width=100)

# for date

datelab = Label(clock, text="00", font=("Times New Roman",40,"bold"),
bg='white', fg='black')
datelab.place(x=120,y=270,height=110,width=100)

datelab_txt = Label(clock, text="DATE", font=("Times New Roman",20,"bold"),
bg='white', fg='black')
datelab_txt.place(x=120,y=410,height=30,width=100)

monthlab = Label(clock, text="00", font=("Times New Roman",40,"bold"),
bg='white', fg='black')
monthlab.place(x=340,y=270,height=110,width=100)

monthlab_txt = Label(clock, text="MONTH", font=("Times New Roman",20,"bold"),
bg='white', fg='black')
monthlab_txt.place(x=340,y=410,height=30,width=110)

yearlab = Label(clock, text="00", font=("Times New Roman",40,"bold"),
bg='white', fg='black')
yearlab.place(x=560,y=270,height=110,width=100)

yearlab_txt = Label(clock, text="YEAR", font=("Times New Roman",20,"bold"),
bg='white', fg='black')
yearlab_txt.place(x=560,y=410,height=30,width=100)

daylab = Label(clock, text="00", font=("Times New Roman",40,"bold"),
bg='white', fg='black')
daylab.place(x=780,y=270,height=110,width=100)

daylab_txt = Label(clock, text="DAY", font=("Times New Roman",20,"bold"),
bg='white', fg='black')
daylab_txt.place(x=780,y=410,height=30,width=100)


date_time()

clock.mainloop()