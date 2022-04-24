import qrcode

data = 'https://www.berilcankutlu.com/post/python-i-le-qr-kod-olu%C5%9Fturma'

image = qrcode.make(data)

image.save('qr.png')
