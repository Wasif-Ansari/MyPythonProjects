from email.mime import image
import cv2
import pyautogui
from win32api import GetSystemMetrics
import numpy as np
import time

width = GetSystemMetrics(0)
height = GetSystemMetrics(1)
t = int(input("Enter time to record screen for.. "))
dim = (width,height)

f = cv2.VideoWriter_fourcc(*"XVID")

output = cv2.VideoWriter("E:/CODING/MyPythonProjects/test.mp4",f,30.0,dim)

now_start_time = time.time()
lag = 5
dur = t+lag
end_time = now_start_time + dur

while 1:
    image = pyautogui.screenshot() #take screen shot
    frame_1 = np.array(image) #make array of all images
    frame = cv2.cvtColor(frame_1,cv2.COLOR_BGR2RGB) #make color original

    output.write(frame)
    
    c_time = time.time()
    if c_time>end_time:
        break
output.release()

print("---END---")
