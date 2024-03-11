import qrcode
import image
qr = qrcode.QRCode(
    version = 15, #15 means the version of the qr code high the number bigger than the code image and complicated picture
    box_size = 10, # size of the box where qr code will be displayed
    border = 5, # it is the white part of image -- border in all 4 sides with the white colour
)

# Enter the web link of the site you want to generate QR Code for
data = input("Enter the Web Link: ")

qr.add_data(data)
qr.make(fit = True)
img = qr.make_image(fill="black", back_color="white")
img.save("test.png")