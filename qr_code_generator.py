# run cmd : pip install qrcode
import qrcode

# data to encode
data = "QR code using make() function"

#  Encoding data
img = qrcode.make(data)

img.save("MyQRCode.png")