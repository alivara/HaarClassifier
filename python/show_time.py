import numpy as np
import cv2

# the train works better for the backs
back_cascade = cv2.CascadeClassifier('/Users/alivarastehranjbar/Nextcloud/HaarClassifier/xml_files/data_0/cascade.xml')
face_cascade = cv2.CascadeClassifier('/Users/alivarastehranjbar/Nextcloud/HaarClassifier/xml_files/data_1/cascade.xml')

# #this is the cascade we just made. Call what you want
# watch_cascade = cv2.CascadeClassifier('watchcascade10stage.xml')

cap = cv2.VideoCapture(0)

while 1:
    ret, img = cap.read()

    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    faces = face_cascade.detectMultiScale(gray, 20, 10)
    # image, reject levels level weights.
    backes = back_cascade.detectMultiScale(gray, 10, 6)

    # add this
    # for (x,y,w,h) in backes:
    #     cv2.rectangle(img,(x,y),(x+w,y+h),(255,255,0),2)

    for (x,y,w,h) in faces:
        cv2.rectangle(img,(x,y),(x+w,y+h),(255,0,0),2)

    cv2.imshow('img',img)
    k = cv2.waitKey(30) & 0xff
    if k == 27:
        break

cap.release()
cv2.destroyAllWindows()
