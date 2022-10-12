import pyshorteners

long_url = input("Enter URL to be shortened: ")

short_url = pyshorteners.Shortener().tinyurl.short(long_url)
print("Shortened URL is : " + short_url)