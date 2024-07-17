import qrcode


qr = qrcode.QRCode(
    version=5,
    error_correction=qrcode.constants.ERROR_CORRECT_L,
    box_size=10,
    border=40000,
)


qr=qrcode.make("https//www.google.com")


qr.save("goog.png")