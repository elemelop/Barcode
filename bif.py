#hello_world, Danish Abdullah here
#i hope you all are doing well
#this is the source code of simple Barcode Importing library
import qrcode

generate_image = qrcode.make("https://instagram.com/oldstoner18?utm_medium=copy_link")
generate_image.save('image.png')
