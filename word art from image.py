from PIL import Image
Image.open("1.jpg")

import pywhatkit
pywhatkit.image_to_ascii_art("bear.jpg","MYART")
read_file = open("MYART.txt","r")
print(read_file)