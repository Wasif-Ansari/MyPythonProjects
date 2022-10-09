from pyzbar.pyzbar import decode
from PIL import Image

decodeQR = decode(Image.open('YOUTUBE CHANNEL LINK.png'))
print(decodeQR[0].data.decode())
#print(decodeQR[0].data.decode('ascii'))