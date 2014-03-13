import cv2
import cv2.cv as cv
import numpy as np


cap = cv2.VideoCapture(0)

cv2.namedWindow("cnt",cv.CV_WINDOW_AUTOSIZE)
cv2.namedWindow("thresh",cv.CV_WINDOW_AUTOSIZE)



#variables pour le trackbar
h1=0
s1=117
v1=124
h2=31
s2=189
v2=255
minDist=20
thresh = None #image apres le traitement 
def rien(x):
	pass
	

#creation des trackbar
cv.CreateTrackbar("H_MIN","cnt",h1,255,rien)
cv.CreateTrackbar("H_MAX","cnt",h2,255,rien)
cv.CreateTrackbar("S_MIN","cnt",s1,255,rien)
cv.CreateTrackbar("S_MAX","cnt",s2,255,rien)
cv.CreateTrackbar("V_MIN","cnt",v1,255,rien)
cv.CreateTrackbar("V_MAX","cnt",v2,255,rien)
cv.CreateTrackbar("minDistCircle","cnt",minDist,20,rien)

while True:
	ret,im = cap.read()
	im2 = cv2.cvtColor(im,cv2.COLOR_BGR2HSV)
	h1 = cv2.getTrackbarPos('H_MIN','cnt')
	h2 = cv2.getTrackbarPos('H_MAX','cnt')
	s1 = cv2.getTrackbarPos('S_MIN','cnt')
	s2 = cv2.getTrackbarPos('S_MAX','cnt')
	v1 = cv2.getTrackbarPos('V_MIN','cnt')
	v2 = cv2.getTrackbarPos('V_MAX','cnt')
	minDist = cv2.getTrackbarPos('minDistCircle','cnt')
	mini = np.array([h1,s1,v1],np.uint8)
	maxi = np.array([h2,s2,v2],np.uint8)
	im = cv2.medianBlur(im,15)
    	cv2.imshow('video test',im)
	thresh = cv2.inRange(im2,mini,maxi)
	thresh = cv2.medianBlur(thresh,5)
	circles = cv2.HoughCircles(thresh,cv.CV_HOUGH_GRADIENT,1,minDist,param1=50,param2=30,minRadius=0,maxRadius=0)
	if circles != None:
		circles = np.uint16(np.around(circles))
		print "owi"
	
	cv2.imshow('thresh',thresh)
	key = cv2.waitKey(10)

cv2.waitKey(0)
cv2.destroyAllWindows()
