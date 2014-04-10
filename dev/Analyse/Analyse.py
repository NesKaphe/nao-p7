# -*- coding: utf-8 -*-
#from Vision import Camera
from naoqi import ALProxy
from Vision.Camera import Camera
from Vision import DetectUtils as DU
from Vision.ColorObjects import FilterColor
import cv2
import cv2.cv as cv
import numpy as np
import math
from vision_definitions import *


class Analyse:

    def __init__(self, videoProxy, camera=1):
        #
        self.videoProxy = videoProxy

        #On recupère l'interface avec la caméra du nao
        self.camera = Camera(self.videoProxy, "Analyse", camera=camera,resolution=kVGA)
        #self.camera.subscribe()

        #On recupère notre filtre de couleurs
        self.filtre = FilterColor()
        
        #Pourcentage de ressemblance avec un cercle (detection de la balle)
        self.pourcentage = 70
        
        #nom du filtre de la balle
        self.bfname = "Balle"#balle filtrer name#TODO trouver un moyen de directement le recuperer dans le fichier

    def createProxies(self):
        #A changer par des paramètres dans un fichier de config
        self.videoProxy = ALProxy("ALVideoDevice", "192.168.1.3", 9559)#TODO utiliser Decision pour récupérer l'IP et port (ou autre fichier si changement)

    
    def switchCamera(self):
		self.camera.switchCamera()

    '''
    getCentreImage: Retourne un couple (x,y) representant le point central de l'image
    capturée par la caméra du Nao
    '''
    def getCentreImage(self):
        resX, resY = self.camera.getResolution()
        centreX = resX / 2
        centreY = resY / 2
        return centreX, centreY

    '''
    calculPourcentage: Calcule un pourcentage de remplissage de l'objet par rapport a son cercle
    circonscrit
    '''
    #A changer pour une meilleure précision
    def calculPourcentage(self, rayon, contour):
        aire_objet = cv2.contourArea(contour)
        aire_cercle = math.pi*rayon*rayon
        return (aire_objet/aire_cercle)*100

    '''
    ChercheBalles: Va chercher tous les objets ressemblant à une balle dans une image
    capturée par la caméra du Nao et renvoie une liste de la forme (centre, rayon)
    -centre est un couple de la forme (x,y)
    '''
    #Renvoie une liste de la forme : (centre,rayon)
    def ChercheBalles(self):
		#On commence par recuperer une image venant de nao
		self.imageCourante = self.camera.getNewImage()

		#On change de colorspace (BGR -> HSV)
		imageHSV = cv2.cvtColor(self.imageCourante, cv2.COLOR_BGR2HSV)

		#On demande a notre filtre de filtrer l'image pour la balle
		#Changer le parametre nom de balle avec un fichier de config (a faire)
		self.imageFiltreCourante = self.filtre.filtrer(imageHSV, self.bfname)

		liste = []
		contours = cv2.findContours(self.imageFiltreCourante.copy(),cv.CV_RETR_EXTERNAL ,cv.CV_CHAIN_APPROX_NONE)[0]
		if contours is not None:
			for i in contours:
				approx = cv2.approxPolyDP(i,0.1*cv2.arcLength(i,True),True)
				(x,y),rayon = cv2.minEnclosingCircle(approx)
				centre = (int(x),int(y))
				rayon = int(rayon)
				pourcent = self.calculPourcentage(rayon,i)
				if pourcent > self.pourcentage:
					liste.append(((centre,rayon), pourcent))

		return liste
  
    '''
    ChercheBallesV2(self):
    version 2 avec plusieurs images
    utilisation de la fonction union et multiunion
    '''

    def ChercheBallesV2(self):
		#On commence par recuperer une image venant de nao
		self.imgs = self.camera.getMultipleImages(nbImages= 3,pauseCapture = 50)
		
		#On change de colorspace (BGR -> HSV)
		self.imgsHSV = self.camera.multiHSVConvert(imgs)

		#On demande a notre filtre de filtrer l'image pour la balle
		#Changer le parametre nom de balle avec un fichier de config (a faire)
			
		self.imgsFiltre = self.filtre.multipleFilter(self.imgsHSV, self.bfname)

		mu = multipleUnion (imgsFiltre)#version 1 
		#mus = multipleUnionSucc (imgsFiltre)#version 2 #TODO a tester 
		contours = cv2.findContours(mu,cv.CV_RETR_EXTERNAL ,cv.CV_CHAIN_APPROX_NONE)[0]
		liste = []#liste des endroits ou est suppose se trouver la balle

		if contours != None:
			for i in contours:
			            approx = cv2.approxPolyDP(i,0.1*cv2.arcLength(i,True),True)
			            (x,y),rayon = cv2.minEnclosingCircle(approx)
			            centre = (int(x),int(y))
			            rayon = int(rayon)
			            pourcent = self.calculPourcentage(rayon,i)
			            if pourcent > self.pourcentage:
			                liste.append(((centre,rayon), pourcent))
		#TODO -- faire une methode spécialement dédidé à la detection de contours
		#réintroduire la detection avec HougthCircle

		return liste
        
    '''
    BallPosition: Va retourner :
    - Un vecteur de direction par rapport au centre de l'image vers l'objet ayant le plus 
    de ressemblance avec une Balle (Si au moins une balle est detectée)
    - None si aucune balle n'a été trouvée dans l'image
    '''
    def BallPosition(self):
        listeBalles = self.ChercheBalles()
        if len(listeBalles) > 0:
            meilleure = listeBalles[0]
            for cercle in listeBalles:
                cv2.circle(self.imageCourante,cercle[0][0],cercle[0][1],(0,255,255),2)
                if meilleure[1] < cercle[1]: #On compare les pourcentages
                    meilleure = cercle
             
            posX = meilleure[0][0][0]
            posY = meilleure[0][0][1]
            
            centreX, centreY = self.getCentreImage()
            print "La balle est a la position : ",(posX,posY), "de l'image"
	    resX = posX - centreX
	    resY = posY - centreY
            return resX, resY
        else:
            return None





    '''
    afficheImagesCourantes: Permet d'afficher l'image courante traitée par l'analyse à l'écran
    '''
    def afficheImagesCourantes(self):
        cv2.imshow("Original",self.imageCourante)
        cv2.imshow("Filtre",self.imageFiltreCourante)
        cv2.waitKey(1)

	#parametre cercle = pourcentage de remplissage du cercle
	# zone = objet zone à analyser
	#la combinaison des 2 nous remvois les cercles dans la zone	
    def AnalyseImg(self,zone=None,cercle=None) :#va contenir la nouvelle version
	
		if zone is None and cercle is None :
			raise NameError("pas de paramettres")
			
			
		#mise creation du thresh :
		self.imageCourante = self.camera.getNewImage()
		imageHSV = cv2.cvtColor(self.imageCourante, cv2.COLOR_BGR2HSV)
		thresh = self.filtre.filtrer(imageHSV, self.bfname)
		self.imageFiltreCourante = thresh
		
		
		
		cerclesP = []#liste de cercles plus pourcentages
		zones = []#va contenir la liste des objets dans la zone
		
		if zone is not None :
				#dessiner la zone (pour le developpeur):
				DU.dessineZone(self.imageCourante,zone)
		
		if cercle is not None:
			cerclesP = DU.detectCercle(thresh,cercle)

			if zone is not None :
				for c in cerclesP :
					if zone.isIn(c[0]) :
						zones.append(c)
						#dessiner les cercle (pour le developpeur):
						DU.dessineCercle(self.imageCourante,c[0])
				#traitement fini
				#retourne un liste qui contient tout les cercles dans la zone
				return zones
			else :
				return cerclesP
		else :
			return DU.detectZone(thresh,zone)
		

#========Zone de test à effacer===========



	
	
