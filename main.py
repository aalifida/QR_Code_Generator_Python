import qrcode as qr

website = input("Please Paste Your Website's URL: ")
QR_type = int(input("For Simple QR Code Press 1:\nFor Customizable QR Code Press 2:\n"))

if QR_type == 1:
    code = qr.make(website)
    print(type(code))
    code.save("QR_sample1.png")
else:
    qr_version = int(input("Enter Version of QR Code (1-40): "))
    qr_boxsize = int(input("Enter Box Size of QR Code: "))
    qr_border = int(input("Enter Border Size of QR Code: "))
    qr_bgColor = input("Enter Background Color of QR Code: ").lower()
    qr_Color = input("Enter Color of QR Code: ").lower()
    
    code = qr.QRCode(
        version=qr_version,
        error_correction=qr.constants.ERROR_CORRECT_H,
        box_size=qr_boxsize,
        border=qr_border,
    )
    code.add_data(website)
    code.make(fit=True)
    
    image = code.make_image(fill_color=qr_Color, back_color=qr_bgColor)
    image.save("QR_sample2.png")
