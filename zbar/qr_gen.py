# pip install qrcode pillow
import qrcode

text = 'Hello World!'
img = qrcode.make(text)

img.save('img/'+text+'.png')