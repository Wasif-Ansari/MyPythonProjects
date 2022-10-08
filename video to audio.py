import moviepy.editor
from tkinter.filedialog import *

vid = askopenfilename() #tkinter module to open a file

video = moviepy.editor.VideoFileClip(vid) #to enable edit on vid file

aud = video.audio
aud.write_audiofile("demo.mp3")

print(" ---END--- ")