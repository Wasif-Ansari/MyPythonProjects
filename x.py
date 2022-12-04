# with open("file.txt") as file:
#     count = 0
#     text = file.read()
#     for i in text:
#         if i.isupper():
#             count += 1
#     print(count)

#import speedtest
# wifi  = speedtest.Speedtest()
# print("Wifi Download Speed is ", wifi.download()/10**6)
# print("Wifi Upload Speed is ", wifi.upload()/10**6)


# import pywhatkit as kit
# import cv2

# kit.text_to_handwriting("Hope you are doing well", save_to="handwriting.png")
# img = cv2.imread("handwriting.png")
# cv2.imshow("Text to Handwriting", img)
# cv2.waitKey(0)
# cv2.destroyAllWindows()
# import re
# s="1.1.1.1"
# ds=""
# for i in s:
#     if(i=="."):
#         ds+="[.]"
#     else:
#         ds+=i

# print(ds)
# import re
# def Defanged_IP(Str):
#     x=re.sub("[.]","[.]",Str)
#     print(x)
# Str="1.1.1.2"
# Defanged_IP(Str)
# S = "255.100.50.0"
# Defanged_IP(S)

# from chatterbot import ChatBot
# import spacy
# import en_core_web_sm
# nlp = en_core_web_sm.load()
# ChatBot("hello")'

# from forex_python.converter import CurrencyRates
# c = CurrencyRates()
# amount = int(input("Enter the amount: "))
# from_currency = input("From Currency: ").upper()
# to_currency = input("To Currency: ").upper()
# print(amount, from_currency, " To ", to_currency)
# result = c.convert(from_currency, to_currency, amount)
# print(result)

# import colorama
# from colorama import Fore,Back,Style
# colorama.init(autoreset=True)

# print(Fore.RED + Back.YELLOW + "Hi My namw is wasif ansari"+Fore.RED+Back.BLACK+"I am your love")

# Height=float(input("Enter your height in centimeters: "))
# Weight=float(input("Enter your Weight in Kg: "))
# Height = Height/100
# BMI=Weight/(Height*Height)
# print("your Body Mass Index is: ",BMI)
# if(BMI>0):
# 	if(BMI<=16):
# 		print("you are severely underweight")
# 	elif(BMI<=18.5):
# 		print("you are underweight")
# 	elif(BMI<=25):
# 		print("you are Healthy")
# 	elif(BMI<=30):
# 		print("you are overweight")
# 	else: print("you are severely overweight")
# else:("enter valid details")

# def convert(s):
#     f = float(s)
#     c = (f - 32) * 5/9
#     return c
# temp = int(input("Enter temp : "))
# print(convert(temp))

# from imdb import IMDb
# movie = IMDb().get_movie("1000")
# print(movie)
# for i in movie["directors"]:
#     print(i)

# import turtle as t
# import random as rd #caterpillar game

# t.bgcolor('yellow')
# caterpillar = t.Turtle()
# caterpillar.shape('square')
# caterpillar.color('red')
# caterpillar.speed(0)
# caterpillar.penup()
# caterpillar.hideturtle()

# leaf = t.Turtle()
# leaf_shape = ((0,0),(14,2),(18,6),(20,20),(6,18),(2,14))
# t.register_shape('leaf',leaf_shape)
# leaf.shape('leaf')
# leaf.color('green')
# leaf.penup()
# leaf.hideturtle()
# leaf.speed()

# game_started = False
# text_turtle = t.Turtle()
# text_turtle.write('Press SPACE to start',align='center',font=('Arial',16,'bold'))
# text_turtle.hideturtle()

# score_turtle = t.Turtle()
# score_turtle.hideturtle()
# score_turtle.speed(0)

# def outside_window():
#     left_wall = -t.window_width()/2
#     right_wall = t.window_width()/2
#     top_wall = t.window_height()/2
#     bottom_wall = -t.window_height()/2
#     (x,y) = caterpillar.pos()
#     outside = x < left_wall or  x > right_wall or  y < bottom_wall or y > top_wall
#     return outside

# def game_over():
#     caterpillar.color('yellow')
#     leaf.color('yellow')
#     t.penup()
#     t.hideturtle()
#     t.write('GAME OVER!',align='center' , font=('Aerial',30,'normal'))

# def display_score(current_score):
#     score_turtle.clear()
#     score_turtle.penup()
#     x = (t.window_width() / 2)-50
#     y = (t.window_height() / 2)-50
#     score_turtle.setpos(x,y)
#     score_turtle.write(str(current_score) , align = 'right',font=('Arial',40,'bold'))

# def place_leaf():
#     leaf.hideturtle()
#     leaf.setx(rd.randint(-200,200))
#     leaf.sety(rd.randint(-200,200))
#     leaf.showturtle()

# def start_game():
#     global game_started
#     if game_started:
#         return
#     game_started = True

#     score = 0
#     text_turtle.clear()

#     caterpillar_speed = 2
#     caterpillar_length = 3
#     caterpillar.shapesize(1,caterpillar_length,1)
#     caterpillar.showturtle()
#     display_score(score)
#     place_leaf()

#     while True:
#         caterpillar.forward(caterpillar_speed)
#         if caterpillar.distance(leaf)<20:
#             place_leaf()
#             caterpillar_length = caterpillar_length + 1
#             caterpillar.shapesize(1,caterpillar_length,1)
#             caterpillar_speed = caterpillar_speed + 1
#             score = score + 10
#             display_score(score)
#         if outside_window():
#             game_over()
#             break

# def move_up():
#     if caterpillar.heading() == 0 or caterpillar.heading() == 180:
#         caterpillar.setheading(90)

# def move_down():
#     if caterpillar.heading() == 0 or caterpillar.heading() == 180:
#         caterpillar.setheading(270)

# def move_left():
#     if caterpillar.heading() == 90 or caterpillar.heading() == 270:
#         caterpillar.setheading(180)

# def move_right():
#     if caterpillar.heading() == 90 or caterpillar.heading() == 270:
#         caterpillar.setheading(0)

# t.onkey(start_game,'space')
# t.onkey(move_up,'Up')
# t.onkey(move_right,'Right')
# t.onkey(move_down,'Down')
# t.onkey(move_left,'Left')
# t.listen()
# t.mainloop()


# from bs4 import BeautifulSoup
# import requests
# headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'}

# def weather(city):
#     city=city.replace(" ","+")
#     res = requests.get(f'https://www.google.com/search?q={city}&oq={city}&aqs=chrome.0.35i39l2j0l4j46j69i60.6128j1j7&sourceid=chrome&ie=UTF-8',headers=headers)
#     print("Searching in google......\n")
#     soup = BeautifulSoup(res.text,'html.parser')   
#     location = soup.select('#wob_loc')[0].getText().strip()  
#     time = soup.select('#wob_dts')[0].getText().strip()       
#     info = soup.select('#wob_dc')[0].getText().strip() 
#     weather = soup.select('#wob_tm')[0].getText().strip()
#     print(location)
#     print(time)
#     print(info)
#     print(weather+"°C") 

# print("enter the city name")
# city=input()
# city=city+" weather"
# weather(city)

# from time import strftime
# from kivy.app import App
# from kivy.clock import Clock
# from kivy.core.text import LabelBase
# from kivy.core.window import Window
# from kivy.utils import get_color_from_hex

# class clockApp(App):
#     sw_started= False
#     sw_seconds = 0
#     def update_time(self, nap):
#         if self.sw_started:
#             self.sw_seconds += nap
#         minutes, seconds = divmod(self.sw_seconds, 60)
#         self.root.ids.stopwatch.text = (
#             '%02d:%02d.[size=40]%02d[/size]'%
#             (int(minutes), int(seconds),
#              int(seconds* 100 % 100))
#         )
#         self.root.ids.time.text = strftime('[b]%H[/b]:%M:%S')
#     def on_start(self):
#         Clock.schedule_interval(self.update_time, 0)
#     def start_stop(self):
#         self.root.ids.start_stop.text =(
#             'Start' if self.sw_started else 'Stop'
#         )
#         self.sw_started = not self.sw_started
#     def reset(self):
#         if self.sw_started:
#             self.root.ids.start_stop.text = 'Start'
#             self.sw_started = False
#         self.sw_seconds = 0

# if __name__ == '__main__':
#     Window.clearcolor = get_color_from_hex('#101216')
#     LabelBase.register(
#         name='Roboto',
#         fn_regular= 'Roboto-Thin.ttf',
#         fn_bold= 'Roboto-Medium.ttf'
#     )
#     clockApp().run()

from tkinter import Tk, Listbox, Button, Scrollbar

def get():
    userline=leftside.get('active')
    print(userline) 

def scale():
    global leftside
    thescale=Tk()
    scroll=Scrollbar(thescale)
    scroll.pack(side='right', fill='y')

    leftside = Listbox(thescale, yscrollcommand = scroll.set)
    for line in range(101):
        leftside.insert('end', "Scale "+str(line))

    leftside.pack(side='left', fill='both')
    scroll.config(command=leftside.yview)

    selectbutton=Button(thescale, text="Select", command=get)
    selectbutton.pack()

    thescale.mainloop()

scale()