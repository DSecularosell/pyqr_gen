import pyqrcode
import png
from pyqrcode import QRCode

def create_qr():
   link = input('What link should be converted to QR?: ')
   qr_code = pyqrcode.create(link)
   qr_code.png(input('Name the file: ') + '.png', scale=8)
   return qr_code

create_qr()

   

