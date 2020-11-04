from pyzbar import pyzbar
import cv2

name = input("Image Path: ")

image = cv2.imread(name)

barcodes = pyzbar.decode(image)

for barcode in barcodes:
	barcodeData = barcode.data.decode("utf-8")
	barcodeType = barcode.type
	text = "{} {}".format(barcodeData, barcodeType)
	(x,y,w,h) = barcode.rect
	cv2.rectangle(image, (x,y), (x+w, y+h), (0, 0, 255), 3)
	cv2.putText(image, text, (x, y-10), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0,255,0), 2)

cv2.imshow("Image", image)
cv2.waitKey(0)