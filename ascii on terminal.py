import pywhatkit as kit
import ascii_magic

#kit.image_to_ascii_art("download.jpg","ascii.txt")

output = ascii_magic.from_image_file("1.jpeg",columns=50,char = "#")

ascii_magic.to_terminal(output)