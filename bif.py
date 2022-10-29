#abdullahpvt09
#this is the source code of simple Barcode Importing library
import qrcode

generate_image = qrcode.make("https://www.instagram.com/abdullahpvt09/")
generate_image.save('image.png')
