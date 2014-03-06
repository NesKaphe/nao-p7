import cv2
 
cap = cv2.VideoCapture(0)
 
while True:
    ret,im = cap.read()
    cv2.imshow('video test',im)
    key = cv2.waitKey(10)
