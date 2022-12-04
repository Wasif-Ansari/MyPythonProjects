import os
import random
import smtplib


def automatic_email():
    user = input("Enter your name: ")
    email = input("Enter Your Email: ")
    message = (f"Dear{user}, Welcome to Thecleverprogrammer")
    s=smtplib.SMTP('smtp.gmail.com', 587)
    s=startls()
    s.login("Your Gmail Account", "Your App Password")
    s.sendmail("SSSSSSSSSSSS", email,message)
    print("Email Sent!")

automatic_email()