import qrcode
from pyzbar.pyzbar import decode
from PIL import Image

def make_qr(data, path, filename):
    qr = qrcode.QRCode(version=1, box_size=10, border=5)
    qr.add_data(data)
    qr.make(fit = True)
    img = qr.make_image(fill_color='blue', back_color='white')
    img.save('{path}/{filename}')
    
def read_qr(path):
    img = Image.open(path)
    result = decode(img)
    print(result)