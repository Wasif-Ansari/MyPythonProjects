from re import T
import qrcode
from PIL import Image

qr = qrcode.QRCode(
version=1, 
error_correction=qrcode.constants.ERROR_CORRECT_H,
box_size=20,border=10,)
qr.add_data("https://www.youtube.com/channel/UCQ8_eumCHbZMhNeMupaTiLw")
qr.make(fit=True)
img = qr.make_image(fill_color = "red",back_color="white")
img.save("YOUTUBE CHANNEL LINK.png")
