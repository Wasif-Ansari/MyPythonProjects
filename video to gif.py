import moviepy.editor 
from tkinter.filedialog import *

vid = askopenfilename() #tkinter module to open a file

video = moviepy.editor.VideoFileClip(vid).subclip((3,17),(3,21))#.rotate(45)
#to enable edit on vid file
video.write_gif("NEW.gif")

