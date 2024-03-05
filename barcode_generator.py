# pip install python_barcode

# create a barcode image with given code

import barcode
from barcode.writer import ImageWriter

text = "Python Programming Code"
text1 = str(text)

code = barcode.get_barcode_class("code128")
image = code(text,writer=ImageWriter())

save_img = image.save('my final barcode')