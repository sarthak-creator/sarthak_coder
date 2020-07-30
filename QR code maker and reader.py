import pyqrcode
import cv2
import pyzbar.pyzbar as pyzbar
from PIL import Image
print("To read QR code type R:")
a=input("To generate QR code type G:\n")
a=a.upper()
if a=="G":
    print("********************************************************************QR Code Generator****************************************************************************")
    sa=input("Enter data to be encoded in QR code:\n")
    ent=input("Enter name of QR code file:\n")
    print("Generating QR code......")
    qr = pyqrcode.create(sa)
    qr.png(f"{ent}.png", scale=8)
    print("QR code generated an saved")

elif a=="R":
    print("*******************************************************************QR Code Reader*****************************************************************************")
    print("To scan live QR code type S:")
    print("To scan  QR code from directory type D")
    a=input()
    a=a.upper()
    if a=="D":
        a=input("Enter the name of file\n")
        if ".png" in a:
            b=len(a)
            if ".png" in a:
                a=a[:(b-4)]
                d=pyzbar.decode(Image.open(f"{a}.png"))
                print("The qr code contains", d[0].data.decode("ascii"))
        else:
            d=pyzbar.decode(Image.open(f"{a}.png"))
                
            print("The qr code contains", d[0].data.decode("ascii"))
    if a=="S":
        print("You selected live QR code scan")
        cap= cv2.VideoCapture(0)

        while True:
            _, frame = cap.read()
            decodedObjects = pyzbar.decode(frame)
            for obj in decodedObjects:
                print(obj.data)
                
                
                        
                   

            cv2.imshow("Frame", frame)

            key=cv2.waitKey(1)
            if key == "9":
                break

  
