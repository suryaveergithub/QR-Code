import qrcode as qr

img = qr.make("https://www.instagram.com/suryaveersingh__/")
img.save("Instagram Profile.png")
