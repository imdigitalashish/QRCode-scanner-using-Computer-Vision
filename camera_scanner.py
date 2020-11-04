from cv2 import cv2
from pyzbar import pyzbar
vid = cv2.VideoCapture(0)

while True:
    ret, frame = vid.read()

    barcodes = pyzbar.decode(frame)
    for barcode in barcodes:
        barcodeData = barcode.data.decode("utf-8")
        barcodeType = barcode.type
        text = "{} {}".format(barcodeData, barcodeType)
        (x,y,w,h) = barcode.rect
        cv2.rectangle(frame, (x,y), (x+w, y+h), (0, 0, 255), 3)
        cv2.putText(frame, text, (x, y-10), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0,255,0), 2)


    cv2.imshow('frame', frame)

    if cv2.waitKey(1) & 0xFF == ord("q"):
        break
    

vid.release()
cv2.destroyAllWindows()