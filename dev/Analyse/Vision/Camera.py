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
	'''
	Paramètres : 	proxy : un videoProxy pour le nao
			moduleName : nom du module pour l'enregistrement des cameras
			camera : 0 pour la camera du haut et 1 pour la camera du bas
			resolution : kQQVGA : 160x120, kQVGA : 320x240, kVGA : 640x480
				     k4VGA : 1280x960
	'''
	def __init__(self,proxy,moduleName,camera=0,resolution=kQVGA):
		self.proxy = proxy
		self.moduleName = moduleName
		if camera < 0 or camera > 1:
			self.camera = 0 #Par defaut on prendra la camera du haut
		else:
			self.camera = camera
		self.resolution = resolution
		self.subscribe()

	'''
	La destruction de l'objet camera entrainera la désinscription du module au nao
	'''
	def __del__(self):
		self.unsubscribe()

	
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


	def switchCamera(self):
		self.unsubscribe()

		if self.camera == 0:
			self.camera = 1
		else:
			self.camera = 0

		self.subscribe()


	def setCameraHaut(self):
		self.unsubscribe()
		self.camera = 0
		self.subscribe()


	def setCameraBas(self):
		self.unsubscribe()
		self.camera = 1
		self.subscribe()

	def getActiveCamera(self):
		return self.camera

	def getResolution(self):
		if self.resolution == kQQVGA:
			return 160, 120 
		elif self.resolution == kQVGA:
			return 320, 240
		elif self.resolution == kVGA:
			return 640, 480
		else:
			return 1280, 960

	'''
	getNewImage: Prend une image de la caméra de nao puis retourne un Numpy array (Opencv)
	'''
	def getNewImage(self,cam=0):
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
		
	'''
	getMultipleImages: Prend "nbImages" images de la caméra de nao puis retourne une
	liste de Numpy array (OpenCV)
	'''
	def getMultipleImages(self,nbImages,pauseCapture):
		listeImages = []
		while nbImages > 0:
			listeImages.append(self.getNewImage())
			time.sleep(pauseCapture)
			nbImages -= 1
		return listeImages
