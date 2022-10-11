from pytube import YouTube

link = "https://youtu.be/LbOMrno3ByE"

youtube_1 = YouTube(link)

#print(youtube_1.title)
#print(youtube_1.thumbnail_url)

videos = youtube_1.streams.all() #get all stream options
#videos = youtube_1.streams.filter(only_audio=True) #for only audioṇ
vid = list(enumerate(videos)) #indexing

for i in vid:
    print(i)

stream = int(input("Enter Quality index: "))
videos[stream].download()
print("Successfully Downloaded ")