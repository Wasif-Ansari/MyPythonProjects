from captcha.image import ImageCaptcha

image = ImageCaptcha(width=300,height=100)
captcha_text = input("Enter text: ")
data = image.generate(captcha_text)
image.write(captcha_text,'output.png')

#from PIL import Image
#Image.open('output.png')