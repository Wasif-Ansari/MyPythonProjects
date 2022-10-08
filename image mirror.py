from PIL import Image

img = Image.open("WhatsApp Image 2022-03-27 at 5.20.59 AM.jpeg")
mirror_img = img.transpose(Image.FLIP_LEFT_RIGHT)
mirror_img.save("output.png")
