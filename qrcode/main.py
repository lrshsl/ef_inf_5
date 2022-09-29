import qrcode

data = 'example'

img = qrcode.make(data)
img.save('output/qrcode_v1.png')