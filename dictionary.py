from PyDictionary import PyDictionary
from tkinter import *

root = Tk()
root.geometry('420x500')


def find_meaning():
    word = entry.get()
    dictionary = PyDictionary(word)
    x = dictionary.meaning(word)
    
    for i in x:
        n = len(x[i])
        print(n)
        ans=""
        for m in range(n):
            ans += str(x[i][m]) + "\n"
        means.config(text=ans)
            

entry = Entry(root,font=("Times New Roman", 15, "bold"))
entry.grid(row=1,column=2)
entry.place(x=10,y=10,width=400)
buttons = Button(root , text="FIND MEANING",command=find_meaning)
buttons.grid(row=4 , column=2)
buttons.place(x=160,y=45,width=100)
means = Label(root,text="None",font=("Times New Roman",10,"bold" ),bg="white",fg="blue")
means.place(x=10,y=100,height=100,width=400)


root.mainloop()