from naoqi import *
from vision_definitions import *
import cv2
import cv2.cv as cv
import numpy as np
import math
#from cv2 import * 
#from numpy import *


naoIP = "192.168.1.3"
moduleName = "OpenCVDemo"
camera = 0 # 1 = Bas/ 0 = Haut
# creer un proxy vers le module ALVideoDevice 
videoProxy = ALProxy("ALVideoDevice", naoIP, 9559)

try:
	while(True):
		videoProxy.unsubscribe(moduleName)
except:
	pass

# specifier au module le type dimage requis 
moduleName = videoProxy.subscribeCamera(moduleName, camera, kQVGA, kBGRColorSpace, 30) 
key=0

cv2.namedWindow("cnt",cv.CV_WINDOW_AUTOSIZE)
cv2.namedWindow("thresh",cv.CV_WINDOW_AUTOSIZE)



#variables pour le trackbar
'''
h1=0
s1=0
v1=0
h2=255
s2=255
v2=255
'''
#SVH lumiere
'''
h1=51
s1=50
v1=180
h2=111
s2=109
v2=255
'''

#SVH ombre
'''
h1=0
s1=125
v1=105
h2=204
s2=170
v2=255
'''

#Autre SVH
'''
h1=0
s1=108
v1=178
h2=11
s2=202
v2=255
'''
#Autre SVH 2
h1=128
h2=255
s1=150
s2=255
v1=0
v2=255

minDist=20
pourcent=80
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
cv.CreateTrackbar("pourcentage_detection","cnt",pourcent,100,rien)


def getPercentage(radius,contour):
	aire_objet = cv2.contourArea(contour)
	aire_cercle = math.pi*radius*radius
	return (aire_objet/aire_cercle)*100


while(key !=10):
	

	# obtenir une image 
	ImageNAO = videoProxy.getImageRemote(moduleName) 
	# lire les parametres 
	largeur = ImageNAO[0] 
	hauteur = ImageNAO[1] 
	canaux = ImageNAO[2] 
	imageBrute = ImageNAO[6] 

	# Conversion magique vers OpenCV
	im = np.fromstring(imageBrute, dtype="uint8").reshape(hauteur, largeur, canaux)
	im = cv2.blur(im,(5,5))	

	im2 = cv2.cvtColor(im,cv2.COLOR_BGR2HSV)
	h1 = cv2.getTrackbarPos('H_MIN','cnt')
	h2 = cv2.getTrackbarPos('H_MAX','cnt')
	s1 = cv2.getTrackbarPos('S_MIN','cnt')
	s2 = cv2.getTrackbarPos('S_MAX','cnt')
	v1 = cv2.getTrackbarPos('V_MIN','cnt')
	v2 = cv2.getTrackbarPos('V_MAX','cnt')
	minDist = cv2.getTrackbarPos('minDistCircle','cnt')
	pourcent = cv2.getTrackbarPos('pourcentage_detection','cnt')
	mini = np.array([h1,s1,v1],np.uint8)
	maxi = np.array([h2,s2,v2],np.uint8)
	#im = cv2.medianBlur(im,15)
	#im2 = cv2.blur(im,(5,5))
	thresh = cv2.inRange(im2,mini,maxi)
	#thresh = cv2.blur(thresh,(10,10))
	thresh = cv2.medianBlur(thresh,5)

	kernel = cv2.getStructuringElement(cv2.MORPH_ELLIPSE,(5,5))
	thresh = cv2.dilate(thresh,kernel,iterations=2)
	thresh = cv2.erode(thresh,kernel,iterations=1)

	contours = cv2.findContours(thresh.copy(),cv.CV_RETR_EXTERNAL ,cv.CV_CHAIN_APPROX_NONE)[0]
	if contours != None:
		for i in contours:
			approx = cv2.approxPolyDP(i,0.05*cv2.arcLength(i,True),True)
			#x,y,w,h = cv2.boundingRect(approx)
			(x,y),radius = cv2.minEnclosingCircle(approx)
			#cv2.rectangle(im,(x,y),(x+w,y+h),(0,255,0),2)
			center = (int(x),int(y))
			radius = int(radius)
			if getPercentage(radius,i) > pourcent:
				cv2.circle(im,center,radius,(0,255,255),2)
	cv2.drawContours(im,contours,-1,cv.CV_RGB(0,255,0))

	"""
	#version qui ne marche pas pour l'instant
	circles = cv2.HoughCircles(thresh,cv.CV_HOUGH_GRADIENT,1,minDist,param1=50,param2=30,minRadius=0,maxRadius=0)
	if circles != None:
		circles = np.uint16(np.around(circles))
		print "cercle !!"
		compteur = 0
		for i in circles[0,:]:
		    # draw the outer circle
		    cv2.circle(im,(i[0],i[1]),i[2],(255,255,0),2)
		    # draw the center of the circle
		    cv2.circle(im,(i[0],i[1]),2,(0,0,255),3)
		    if compteur > 20:
			break
		    compteur += 1
	"""
	
	cv2.imshow('thresh',thresh)

	# affichage de l'image originale 
	cv2.imshow("Camera", im)
	 
	key=cv2.waitKey(1)	#attente
# Cleanup
destroyAllWindows()
videoProxy.unsubscribe(moduleName)
