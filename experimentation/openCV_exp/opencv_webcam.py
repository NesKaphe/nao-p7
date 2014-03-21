import cv2
import cv2.cv as cv
import numpy as np


cap = cv2.VideoCapture(0)

cv2.namedWindow("cnt",cv.CV_WINDOW_AUTOSIZE)
cv2.namedWindow("thresh",cv.CV_WINDOW_AUTOSIZE)



#variables pour le trackbar r
h1=133
s1=128
v1=83
h2=184
s2=175
v2=254
minDist=20
floue = 5
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
cv.CreateTrackbar("Floue","cnt",floue,20,rien)

i=0
while True:
	ret,im = cap.read()
	im = cv2.blur(im,(floue,floue))
	im2 = cv2.cvtColor(im,cv2.COLOR_BGR2HSV)
	h1 = cv2.getTrackbarPos('H_MIN','cnt')
	h2 = cv2.getTrackbarPos('H_MAX','cnt')
	s1 = cv2.getTrackbarPos('S_MIN','cnt')
	s2 = cv2.getTrackbarPos('S_MAX','cnt')
	v1 = cv2.getTrackbarPos('V_MIN','cnt')
	v2 = cv2.getTrackbarPos('V_MAX','cnt')
	minDist = cv2.getTrackbarPos('minDistCircle','cnt')
	floue = cv2.getTrackbarPos('Floue','cnt')
	mini = np.array([h1,s1,v1],np.uint8)
	maxi = np.array([h2,s2,v2],np.uint8)
    	
	thresh = cv2.inRange(im2,mini,maxi)

	
	thresh = cv2.medianBlur(thresh,5)
	circles = cv2.HoughCircles(thresh,cv.CV_HOUGH_GRADIENT,2,minDist,param1=50,param2=30,minRadius=0,maxRadius=0)
	if circles != None:
		circles = np.uint16(np.around(circles))
		#print "owi        circle", circles
		#i+=1
		circles = np.uint16(np.around(circles))
		for i in circles[0,:]:
		    # draw the outer circle
		    cv2.circle(im,(i[0],i[1]),i[2],(0,255,0),2)
		    # draw the center of the circle
		    cv2.circle(im,(i[0],i[1]),2,(0,0,255),3)
	
	cv2.imshow('thresh',thresh)
	cv2.imshow('video test',im)
	print "im type = ",type(im)
	key = cv2.waitKey(10)

cv2.waitKey(0)
cv2.destroyAllWindows()
