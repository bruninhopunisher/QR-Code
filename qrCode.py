import qrcode

qrCode = 'Aqui será a variável que ficara seu link, numero ou frase'

img = qrcode.make(qrCode)
img.show()


