# -*- coding: utf-8 -*-

import cv2
import cv2.cv as cv
import numpy as np
import os
import Camera

class FilterColor:
	
	def __init__(self):
		self.objets = []
		

	def loadConfig(self):
		#Peut etre changer ca en mettant le path dans un fichier de config
		fichier = open("./Data/colors.txt", "r")
		
		'''
		Je met ici mais on trouvera un autre endroit pour l'expliquer:
		le fichier colors.txt devra contenir sur une ligne H min, 
		S min, V min, H max, S max, V max 
		pour les couleurs de cet objet
		'''

		#lecture du fichier
		for ligne in fichier:
			#On retire le \n de fin de ligne
			ligne = ligne.rstrip('\n')
			params = ligne.split(', ')
			self.objets.append(params)

		fichier.close()


	def filter(self, imageHSV, nomObjet):
		mini = None
		maxi = None
		for objet in self.objets:
			if objet[0] == nomObjet:
				mini = np.array([objet[1],objet[3],objet[5]],np.uint8)
				maxi = np.array([objet[2],objet[4],objet[6]],np.uint8)
				break

		if mini != None:
			#Filtre de l'image en fonction de la couleur
			thresh = cv2.inRange(imageHSV,mini,maxi) 

			#On va maintenant corriger quelques imperfection de l'image filtree
			thresh = cv2.medianBlur(thresh,5)
			kernel = cv2.getStructuringElement(cv2.MORPH_ELLIPSE,(5,5))
			thresh = cv2.dilate(thresh,kernel,iterations=2)
			thresh = cv2.erode(thresh,kernel,iterations=1)
			
			return thresh
		else:
			raise Exception('Filtre impossible [nomObjet incorrect]')

	''' Peut etre inutile
	'''
	def multipleFilter(self, listeImagesHSV, nomObjet):
		pass

	''' va afficher la fenetre pour calibrer les couleurs + interaction avec la console pour
	faire plusieurs enregistrements [TODO : Vendredi 28 mars !!]
	'''
	def calibrage(self):
		boucle = True
		
		# Nao
		#videoProxy = ALProxy("ALVideoDevice", "192.168.1.3", 9559)
		#cam = Camera(videoProxy, "Calibrage")
		#cam.subscribe()
		#image = camera.getNewImage()

		# Webcam du pc pour les moments sans nao
		cap = cv2.VideoCapture(0)
		ret, image = cap.read()

		#On affiche la capture originale (Sinon, on fera sur video)
		cv2.imshow("Original", image)

		#On convertis le colorspace de l'image en HSV
		imageHSV = cv2.cvtColor(image,cv2.COLOR_BGR2HSV)

		#definition des fenêtres
		cv2.namedWindow("Original",cv.CV_WINDOW_AUTOSIZE)
		
		#Callback pour les trackbar
		def callback(x):
			pass

		#Ouverture du fichier 
		fichier = open("./Data/colors2.txt", "w+")

		print "===== Calibrage ====="
		while boucle:
			nom = raw_input("Nom de l'objet : ")

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
				h1 = cv2.getTrackbarPos("H_MIN","Configuration")
				h2 = cv2.getTrackbarPos("H_MAX","Configuration")
				s1 = cv2.getTrackbarPos("S_MIN","Configuration")
				s2 = cv2.getTrackbarPos("S_MAX","Configuration")
				v1 = cv2.getTrackbarPos("V_MIN","Configuration")
				v2 = cv2.getTrackbarPos("V_MAX","Configuration")

				mini = np.array([h1,s1,v1],np.uint8)
				maxi = np.array([h2,s2,v2],np.uint8)
				thresh = cv2.inRange(imageHSV,mini,maxi)
				kernel = cv2.getStructuringElement(cv2.MORPH_ELLIPSE,(5,5))
				thresh = cv2.dilate(thresh,kernel,iterations=2)
				thresh = cv2.erode(thresh,kernel,iterations=1)
				
				cv2.imshow("Calibrage", thresh)

				key = cv2.waitKey(10)

				''' Bug connu avec ubuntu...
				Voir : http://stackoverflow.com/questions/9172170/python-opencv-cv-waitkey-spits-back-weird-output-on-ubuntu-modulo-256-maps-corre'''
			 	key -= 0x100000
				if key == 113: #on quitte avec la touche q
					break

			#remplacer par une ecriture dans le fichier
			print "Data : ", nom, ", ", h1, ", ", h2, ", ", s1, ", ", s2, ", ", v1, ", ", v2 
			ligne = str(nom) + ", " + str(h1) + ", " + str(h2) + ", " + str(s1) + ", " + str(s2) + ", " + str(v1) + ", " + str(v2) + "\n" 

			fichier.write(ligne)
			

			cv2.destroyWindow("Calibrage")
			cv2.destroyWindow("Configuration")
			cv2.waitKey(1)

			rep = raw_input("Faire une autre saisie ? <n pour stopper>")
			if rep == "n":
				break;
				

			
		
		
class BallObject:

	def __init__(self):
		self.precision = 80

	
