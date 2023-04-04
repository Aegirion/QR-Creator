import qrcode as qr

img=qr.make("https://github.com/Aegirion?tab=repositories")
type(img)
img.save("qr.png")