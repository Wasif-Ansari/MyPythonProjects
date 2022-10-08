from captcha.audio import AudioCaptcha
#from captcha.image import ImageCaptcha

audio = AudioCaptcha()
#image = ImageCaptcha(fonts=['/path/A.ttf', '/path/B.ttf'])

data = audio.generate("123")
audio.write("123", 'out.mp3')

#data = image.generate('1234')
#image.write('1234', 'out.png')