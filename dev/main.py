import sys

from naoqi import ALProxy
from Vision.Camera import Camera
from Vision.ColorObjects import FilterColor
import cv2

#videoProxy = ALProxy("ALVideoDevice", "192.168.1.3", 9559)

#camera = Camera(videoProxy,"toto")

#camera.subscribe()
'''
im = camera.getNewImage()
im2 = cv2.cvtColor(im,cv2.COLOR_BGR2HSV)
filter = FilterColor()
im3 = filter.filter(im,"Balle")
print camera
cv2.imshow("original",im)
cv2.imshow("Objet",im3)
'''

#Lim = camera.getMultipleImages(5,0.3)
filter = FilterColor()
filter.calibrage()
#cv2.waitKey(0)

camera.unsubscribe()
