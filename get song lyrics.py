import lyricsgenius

apikey = "00rJ5_f0nPAe8q2X4wZg4Zr60oDBkU4K6PD1hVnKwPqM3oZfd3BaG-xoZcTvr6IJ"
genius = lyricsgenius.Genius(apikey)
name = input("Enter Artist name : ")
artist = genius.search_artist(name)
song = input("Enter song name : ")
song=artist.song(song)
print(song.lyrics)