# Importing libraries
import cv2 
import webbrowser
import mysql.connector

# Declaring a variable and passing an instance to start the camera 
cap = cv2.VideoCapture(0) 
# initialize the cv2 QRCode detector 
detector = cv2.QRCodeDetector()
a = ''
def scanner():
# Continuously reading the webcam screen until the loop breaks
    while True: 
        _, img = cap.read()

        # detect and decode 
        data, bbox, _ = detector.detectAndDecode(img)

        # check if there is a QRCode in the image 
        if data: 
            a=data.split() 
            b = a[0]
            print(b)
            return b
            break

        cv2.imshow("QRCODEscanner", img)     
        if cv2.waitKey(1) == ord("q"): 
            break
  
roll_num = scanner()
b=webbrowser.open(str(a)) 
cap.release() 
cv2.destroyAllWindows()