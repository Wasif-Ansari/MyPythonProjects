from pytube import Playlist

py = Playlist("https://youtube.com/playlist?list=PLS46nnSnLF7pIeWVzSBRuHSPSa2bzSgtX")

print(f'Downloading : {py.title}')

for video in py.videos:
    videos = video.streams.all() #for only video
    vid = list(enumerate(videos)) #indexing
    for i in vid:
        print(i)
    stream = int(input("Enter Quality index: "))
    videos[stream].download()
print("Successfully Downloaded whole playlist! ")