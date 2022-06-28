import qrcode 

data = 'Hello World'

img = qrcode.make(data)

img.save('C:/Users/Dhrumil.Panchal/Documents/Python Projects/QR1.png')