# -*- coding: utf-8 -*-

import cv2
import cv2.cv as cv
import numpy as np
import os
from Camera import Camera
from naoqi import ALProxy
from vision_definitions import *
import time

class FilterColor:
	
	def __init__(self):
		self.objets = []
		self.loadConfig()
		

	def loadConfig(self):
		fichier = open("./Data/colors.txt", "r")
		
		'''
		le fichier colors.txt devra contenir sur une ligne:
		nomObjet, H min, S min, V min, H max, S max, V max 
		pour les couleurs de cet objet
		'''

		#lecture du fichier
		for ligne in fichier:
			#On retire le \n de fin de ligne
			ligne = ligne.rstrip('\n')
			params = ligne.split(', ')
			self.objets.append(params)

		fichier.close()


	'''
	filtrer :
	Prend une image HSV et lui applique un filtre.
	Retourne l'image binaire après le filtre
	'''
	def filtrer(self, imageHSV, nomObjet):
		mini = None
		maxi = None
		for objet in self.objets:
			if objet[0] == nomObjet:
				mini = np.array([objet[1],objet[3],objet[5]],np.uint8)
				maxi = np.array([objet[2],objet[4],objet[6]],np.uint8)
				break

		if mini != None: #Si mini a été initialisé, maxi l'a aussi été
			#Filtre de l'image en fonction de la couleur
			imageHSV = cv2.medianBlur(imageHSV,15)
			thresh = cv2.inRange(imageHSV,mini,maxi) 

			#On va maintenant corriger quelques imperfection de l'image filtree
			thresh = cv2.medianBlur(thresh,15)
			kernel = cv2.getStructuringElement(cv2.MORPH_ELLIPSE,(10,10))
			thresh = cv2.morphologyEx(thresh, cv2.MORPH_OPEN, kernel)
			return thresh
		else:
			raise Exception('Filtre impossible [nomObjet incorrect]'+str(nomObjet))

	'''
	renvoie un filtre sur la couleur rouge
	'''
	def filtrerCoucheRouge(self, image):
		r = cv2.split(image)[2]
		mini = np.array([100], np.uint8)
		maxi = np.array([255], np.uint8)
		t = cv2.inRange(r, mini, maxi)
		return t

	'''
	multipleFilter:
	Applique le filtre demandé sur une liste d'image en HSV
	Retourne une liste d'image binaire filtrées 
	'''
	def multipleFilter(self, listeImagesHSV, nomObjet):
		imgsFiltre = []
		for img in listeImagesHSV :
			imgsFiltre.append(self.filtrer(img,nomObjet))
		return imgsFiltre
			
	'''
	multiHSVConvert :
	prend une liste d'images et retourne 
	une liste de celles ci convertis en HSV
	'''
	def multiHSVConvert(self,listImgs):
		imgsHSV = []
		for imgs in listImgs :
			imgsHSV.append(cv2.cvtColor(imgs, cv2.COLOR_BGR2HSV))
		return imgsHSV

	''' va afficher la fenetre pour calibrer les couleurs + interaction avec la console pour
	faire plusieurs enregistrements
	'''
	def calibrage(self):
		objets = ["Balle", "Poteau"]
		cameraCalibrage = 0
		tour = 0
		#Ouverture du fichier 
		fichier = open("./Data/colors.txt", "w+")
		
		videoProxy = ALProxy("ALVideoDevice", "192.168.1.3", 9559)
		cam = Camera(videoProxy, "Calibrage", camera=cameraCalibrage, resolution=kVGA)

		while cameraCalibrage < 2: #On va boucler sur les deux cameras

			boucle = True
		
		        # Nao
		
			print "Capture de quelques images pour le calibrage : Cam ", cameraCalibrage
			images = cam.getMultipleImages(10,0.05)
		
			imageCourante = 0

		        # Webcam du pc pour les moments sans nao
			'''
			cap = cv2.VideoCapture(0)
			images = []
			i = 0
			while i < 10:
			    images.append(cap.read()[1])
			    time.sleep(0.1)
			    i += 1
		        '''

		        #Callback pour les trackbar
			def callback(x):
				pass 

	                #print os.getcwd()
			print "===== Calibrage ====="
			for unobjet in objets:
				nom = str(unobjet)+str(cameraCalibrage)
				print "Calibrage de ", nom
				#definition des fenêtres
				cv2.namedWindow("Original",cv.CV_WINDOW_AUTOSIZE)
				cv2.namedWindow("Configuration",cv.CV_WINDOW_AUTOSIZE)
				cv2.namedWindow("Calibrage",cv.CV_WINDOW_AUTOSIZE)

				#Variables pour le calibrage
				# Teinte (Hue)
				h1=0
				h2=255
				# Saturation
				s1=0
				s2=255
				# Valeur (Value)
				v1=0
				v2=255

		        	#creation des trackbar
				cv.CreateTrackbar("H_MIN","Configuration",h1,255,callback)
				cv.CreateTrackbar("H_MAX","Configuration",h2,255,callback)
				cv.CreateTrackbar("S_MIN","Configuration",s1,255,callback)
				cv.CreateTrackbar("S_MAX","Configuration",s2,255,callback)
				cv.CreateTrackbar("V_MIN","Configuration",v1,255,callback)
				cv.CreateTrackbar("V_MAX","Configuration",v2,255,callback)

				while True:
					#On affiche la capture originale
					cv2.imshow("Original", images[imageCourante])


					#On convertis le colorspace de l'image en HSV
					imageHSV = cv2.cvtColor(images[imageCourante],cv2.COLOR_BGR2HSV)

				

					if imageCourante >= 9:
						imageCourante = 0
					else:
						imageCourante = imageCourante + 1

					#on recupère les valeurs des trackbars
					h1 = cv2.getTrackbarPos("H_MIN","Configuration")
					h2 = cv2.getTrackbarPos("H_MAX","Configuration")
					s1 = cv2.getTrackbarPos("S_MIN","Configuration")
					s2 = cv2.getTrackbarPos("S_MAX","Configuration")
					v1 = cv2.getTrackbarPos("V_MIN","Configuration")
					v2 = cv2.getTrackbarPos("V_MAX","Configuration")
					mini = np.array([h1,s1,v1],np.uint8)
					maxi = np.array([h2,s2,v2],np.uint8)
				

					#Filtre de l'image en fonction de la couleur
					imageHSV = cv2.medianBlur(imageHSV,15)
					thresh = cv2.inRange(imageHSV,mini,maxi) 
				
			        	#On va maintenant corriger quelques imperfection de l'image filtree
					thresh = cv2.medianBlur(thresh,15)
					kernel = cv2.getStructuringElement(cv2.MORPH_ELLIPSE,(10,10))
					thresh = cv2.morphologyEx(thresh,cv2.MORPH_OPEN,kernel)

					
					#Puis on affiche à l'écran l'image
				        cv2.imshow("Calibrage", thresh)

					key = cv2.waitKey(10)

				        ''' Bug connu avec ubuntu...
					Voir : http://stackoverflow.com/questions/9172170/python-opencv-cv-waitkey-spits-back-weird-output-on-ubuntu-modulo-256-maps-corre'''
					key -= 0x100000
					if key == 113: #on quitte avec la touche q
						break

				ligne = nom+ ", " + str(h1) + ", " + str(h2) + ", " + str(s1) + ", " + str(s2) + ", " + str(v1) + ", " + str(v2) + "\n" 

				fichier.write(ligne)
			

				cv2.destroyWindow("Calibrage")
				cv2.destroyWindow("Configuration")
				cv2.destroyWindow("Original")
				cv2.waitKey(1)

				
			cameraCalibrage += 1
			cam.switchCamera() #On passe a l'autre camera pour la calibrer

		#On recharge finalement les nouvelles configurations d'objets
		fichier.close()
		self.loadConfig()
	
