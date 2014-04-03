# -*- coding: utf-8 -*-
#from Vision import Camera
from naoqi import ALProxy
from Vision.Camera import Camera
from Vision.ColorObjects import FilterColor
import cv2
import cv2.cv as cv
import numpy as np
import math

class Analyse:

    def __init__(self, videoProxy):
        #
        self.videoProxy = videoProxy

        #On recupère l'interface avec la caméra du nao
        self.camera = Camera.Camera(self.videoProxy, "Analyse")
        #self.camera.subscribe()

        #On recupère notre filtre de couleurs
        self.filtre = FilterColor()
        
        #Pourcentage de ressemblance avec un cercle (detection de la balle)
        self.pourcentage = 80

    def createProxies(self):
        #A changer par des paramètres dans un fichier de config
        self.videoProxy = ALProxy("ALVideoDevice", "192.168.1.3", 9559)

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
        self.imageFiltreCourante = self.filtre.filtrer(imageHSV, "Balle")

        liste = []
        contours = cv2.findContours(self.imageFiltreCourante.copy(),cv.CV_RETR_EXTERNAL ,cv.CV_CHAIN_APPROX_NONE)[0]
	if contours != None:
		for i in contours:
                    approx = cv2.approxPolyDP(i,0.05*cv2.arcLength(i,True),True)
                    (x,y),rayon = cv2.minEnclosingCircle(approx)
                    centre = (int(x),int(y))
                    rayon = int(rayon)
                    pourcent = self.calculPourcentage(rayon,i)
                    if pourcent > self.pourcentage:
                        liste.append(((centre,rayon), pourcent))

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
            print (centreX,centreY)," et ", (posX,posY)
            if posX < centreX:
                resX = 1
            else:
                resX = -1

            if posY < centreY:
                resY = -1
            else:
                resY = 1

            return resX, resYxxx
        else:
            return None
    
    '''
    afficheImagesCourantes: Permet d'afficher l'image courante traitée par l'analyse à l'écran
    '''
    def afficheImagesCourantes(self):
        cv2.imshow("Original",self.imageCourante)
        cv2.imshow("Filtre",self.imageFiltreCourante)

#========Zone de test à effacer===========

#filtre = FilterColor()
#filtre.calibrage()
'''
analyse = Analyse()
while True:
    result = analyse.BallPosition()
    print result
    analyse.afficheImagesCourantes()
    cv2.waitKey(1)

'''
