import qrcode

qrCode = 'Aqui será a variável que ficara seu link, número ou frase'

img = qrcode.make(qrCode)
img.show()


