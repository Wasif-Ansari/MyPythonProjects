from moviepy.editor import *

clip_1 = VideoFileClip("1.mp4").subclip(0,20)
clip_2 = VideoFileClip("2.mp4").subclip(10,30)
clip_3 = VideoFileClip("3.mp4").subclip(0,20)
clip_4 = VideoFileClip("4.mp4").subclip(0,20)

comb = clips_array([[clip_1,clip_2],
                    [clip_3,clip_4]])

comb.write_videofile("test.mp4")
 