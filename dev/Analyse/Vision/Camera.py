# -*- coding: utf-8 -*-
'''
	Fichier capteur caméra
'''

import sys
from vision_definitions import *
import cv2
import cv2.cv as cv
import numpy as np
import time

class Camera:

	def __init__(self,proxy,moduleName,camera=0,resolution=kQVGA):
		self.proxy = proxy
		self.moduleName = moduleName
		self.camera = camera
		self.resolution = resolution

	def subscribe(self):
		self.proxy.subscribeCamera(self.moduleName, 
					   self.camera, 
					   self.resolution, 
					   kBGRColorSpace, 30)

	def unsubscribe(self):
		try:
			while(True):
				self.proxy.unsubscribe(self.moduleName)
		except:
			pass


	def getResolution(self):
		if self.resolution == kQVGA:
			return 320, 240
		elif self.resolution == kVGA:
			return 640, 480
		else:
			return 1280, 960

	'''
	getNewImage: Prend une image de la caméra de nao puis retourne un Numpy array (Opencv)
	'''
	def getNewImage(self):
		#Demande une image au proxy
		ImageNAO = self.proxy.getImageRemote(self.moduleName)
		
		#Lecture des paramètres
		largeur = ImageNAO[0] 
		hauteur = ImageNAO[1] 
		canaux = ImageNAO[2] 
		imageBrute = ImageNAO[6]

		#Conversion de l'image obtenue en Numpy array
		imageNumpy = np.fromstring(imageBrute, dtype="uint8").reshape(hauteur, largeur, canaux)

		return imageNumpy
		

	def getMultipleImages(self,nbImages,pauseCapture):
		listeImages = []
		while nbImages > 0:
			listeImages.append(self.getNewImage())
			time.sleep(pauseCapture)
			nbImages -= 1
		return listeImages
