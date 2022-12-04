import pyttsx3
import speech_recognition as sr
import webbrowser
import datetime
import pyjokes
import os
import time

def sptext(): #speech to text
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        print("Speak Now...")
        recognizer.adjust_for_ambient_noise(source)
        audio = recognizer.listen(source)
        try:
            print("recognizing...")
            data = recognizer.recognize_google(audio)
            print(data)
            return data   
        except sr.UnknownValueError:
            print("Not Understood")

def speechtx(x): # text to speech
    engine = pyttsx3.init()
    voices = engine.getProperty("voices")
    engine.setProperty("voice", voices[0].id) #male 0 & female 1 2
    rate = engine.getProperty("rate")
    engine.setProperty("rate" , 130)
    engine.say(x)
    engine.runAndWait()


if __name__ == "__main__":
    
    #if "wasif" in sptext().lower():
    if sptext().lower() == "hello":
        while 1:
            try:
                data1 = sptext().lower()
            except AttributeError:
                print("Pardon i could'nt get it")
                continue
            if "your name" in data1:
                name = "my name is wasif"
                speechtx(name)
            elif ("old are you") in data1:
                age = "i am two years old"
                speechtx(age)
            elif ("your age") in data1:
                age = "i am two years old"
                speechtx(age)
            elif 'time' in data1:
                time = datetime.datetime.now().strftime("%I%M%p") #give time
                speechtx(time)
            elif "youtube" in data1:
                webbrowser.open("https://www.youtube.com/")
            elif "google" in data1:
                webbrowser.open("https://www.google.com/")
            elif "joke" in data1:
                joke_1 = pyjokes.get_joke(language="en", category="neutral")
                print(joke_1)
                speechtx(joke_1)
            elif 'play song' in data1:
                add = "E:\CODING\songs"
                listsongs = os.listdir(add)
                print(listsongs)
                os.startfile(os.path.join(add,listsongs[1]))
            elif "exit" in data1:
                speechtx("thank you ")
                break
            #time.sleep(3)
