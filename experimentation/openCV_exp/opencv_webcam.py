import cv2
import cv2.cv as cv
import numpy as np


cap = cv2.VideoCapture(0)

cv2.namedWindow("cnt",cv.CV_WINDOW_AUTOSIZE)
cv2.namedWindow("thresh",cv.CV_WINDOW_AUTOSIZE)



#variables pour le trackbar
h1=0
s1=0
v1=0
h2=0
s2=0
v2=0
thresh = None #image apres le traitement 
def rien(x):
	pass
	

#creation des trackbar
cv.CreateTrackbar("H1","cnt",h1,255,rien)
cv.CreateTrackbar("H2","cnt",h2,255,rien)
cv.CreateTrackbar("S1","cnt",s1,255,rien)
cv.CreateTrackbar("S2","cnt",s2,255,rien)
cv.CreateTrackbar("V1","cnt",v1,255,rien)
cv.CreateTrackbar("V2","cnt",v2,255,rien)


while True:
	ret,im = cap.read()
	im2 = cv2.cvtColor(im,cv2.COLOR_BGR2HSV)
	h1 = cv2.getTrackbarPos('H1','cnt')
	h2 = cv2.getTrackbarPos('H2','cnt')
	s1 = cv2.getTrackbarPos('S1','cnt')
	s2 = cv2.getTrackbarPos('S2','cnt')
	v1 = cv2.getTrackbarPos('V1','cnt')
	v2 = cv2.getTrackbarPos('V2','cnt')
	mini = np.array([h1,s1,v1],np.uint8)
	maxi = np.array([h2,s2,v2],np.uint8)
    	cv2.imshow('video test',im)
	thresh = cv2.inRange(im2,mini,maxi)
	cv2.imshow('thresh',thresh)
	key = cv2.waitKey(10)

cv2.waitKey(0)
cv2.destroyAllWindows()
