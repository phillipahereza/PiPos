import barcode
from barcode.writer import ImageWriter

from generate_ean import getnumber

ean = getnumber()
bar = barcode.get('ean13', ean, writer=ImageWriter())
filename = bar.save('ean13')
