from pytube import Playlist

py = Playlist("https://youtube.com/playlist?list=PLeo1K3hjS3uulqalNX4TTCNCHQjEa2PZf")

print(f'Downloading : {py.title}')

for video in py.videos:
    video.streams.first().download()

print("Successfully Downloaded whole playlist! ")