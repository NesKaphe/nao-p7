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
import random
from Mouvement.Mouvement import *
from vision_definitions import *


class Analyse:
    
    def __init__(self, videoProxy,motion,posture, camera=1):
        #recuperation des proxy :
        self.videoProxy = videoProxy
        self.motion = motion
        self.posture = posture
        #On recupère l'interface avec la caméra du nao
        self.camera = Camera(self.videoProxy, "Analyse", camera=camera,resolution=kVGA)
        #self.camera.subscribe()#TODO : à retirer si pas utile

        #On recupère notre filtre de couleurs
        self.filtre = FilterColor()
        
        #Pourcentage de ressemblance avec un cercle (detection de la balle)
        self.pourcentage = 70
        
        #nom du filtre de la balle
        self.BalleCamHaut = "Balle0" #balle filtrer name #TODO trouver un moyen de directeme

        self.BalleCamBas = "Balle1"
 
        self.poteauCamHaut= "poteau0"
	
	self.poteauCamBas = "poteau1"

        self.imageCourante = None
    
    def switchCamera(self):
        self.camera.switchCamera()

    def setCameraHaut(self):
        self.camera.setCameraHaut()

    def setCameraBas(self):
        self.camera.setCameraBas()

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
    afficheImagesCourantes: Permet d'afficher l'image courante traitée par l'analyse à l'écran
    note : exception si l'image n'est pas initialisé
    '''
    def afficheImagesCourantes(self):
    	if self.imageCourante is None:
    		raise NameError("image courante non initialisé")
        cv2.imshow("Original",self.imageCourante)
        cv2.imshow("Filtre",self.imageFiltreCourante)
        cv2.waitKey(33)


    #TODO : commentaire (Alain : voir même supprimer ca, c'est completement faux)
    def testZone(self, zone):
        return DU.detectZone(self.imageFiltreCourante, zone)

    '''
	AnalyseImg :
	--------------------------------------------
	méthode qui permet de faire les analyses sur une image.
	Elle à plusieurs retours differents en fonction de ces paramètres.
	
	parametres :
	--------------------------------------------
	cercle = pourcentage de remplissage du cercle
	zone = objet zone à analyserunexpected indent
	dessin = si on veux que la zone et du cercle soit dessiné dans l'image courrante !!!!pas encore implémenté
	thresh = si nous avons une image que nous voulons garder ou passé en paramètre on peut le faire
	!!!! dans un futur développement il sera possible d'ajouter de nouveaux parametres
	retour :
	--------------------------------------------
	cercle : retourne la position de tout les cercles trouvés avec leur pourcentage remplissage
	zone : vrai si la zone observée (après fitrage) contient quelque chose (au moins un pixel blanc)
	cerlce + zone : renvois les cercles dans la zone (avec leurs pourcentages de remplissage respectif)
					Un cercle est considéré dans la zone si son centre est dans la zone.
    '''

    def AnalyseImg(self,thresh=None,zone=None,cercle=None,poteau=None,dessin=True) :#va contenir la nouvelle version
    
		if zone is None and cercle is None and poteau is not True :
			raise NameError("pas de paramettres")
			
		if poteau is not None and cercle is not None and thresh is not None:
			raise NameError("paramètres poteau et cercle non compatible")


		#creation du thresh :
		if thresh is None :
			self.imageCourante = self.camera.getNewImage()
			imageHSV = cv2.cvtColor(self.imageCourante, cv2.COLOR_BGR2HSV)

			if poteau is not None:
				thresh = self.filtre.filtrer(imageHSV, self.poteauName)
			else:
                                #masqueRouge = self.filtre.filtrerCoucheRouge(self.imageCourante)
				thresh = None
                                #On applique le masque a l'image hsv
				if self.camera.getActiveCamera() == 0:
					thresh = self.filtre.filtrer(imageHSV, self.BalleCamHaut)
				else :
					thresh = self.filtre.filtrer(imageHSV, self.BalleCamBas)

			self.imageFiltreCourante = thresh
                        
		
		
		cerclesP = []#liste de cercles plus pourcentages
		zones = []#va contenir la liste des objets dans la zone

		#dessiner la zone (pour le developpeur):
		if zone is not None :
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
				"""
				#issu d'un merge mais je sais pas si il faut la garder
				#dessiner les cercle (pour le developpeur):
				DU.dessineCercle(self.imageCourante,c[0])
				return cerclesP
				"""
				for c in cerclesP :
					#dessiner les cercle (pour le developpeur):
					DU.dessineCercle(self.imageCourante,c[0])
				return cerclesP
		else :
			return DU.detectZone(thresh,zone)
	

    '''
	AnalyseMultiImage(self,thresh=None,zone=None,cercle=None,dessin=True,nb_img):
	---------------------------------------------------------------------------
	Analyse plusieurs images et détermine ou est la balle grâce à une 
	estimation particulière paramètre nb_img = nb d'images à analyser.
	Elle peut aussi déterminer si la zone observé contient quelque chose.
	comment ça marche : elle forme des groupes de points (centre de cercle) 
	proches et détermine ou est la balle grace à cela.
	un point est proche d'un autre si il est à une distance de 1/20 de la taille
	de l'image (par exemple pour 640x480 la distance proche est de 36 px)
	Elle prend le plus grand groupe de points.
	
	Note : ceci est une méthode naïve elle n'est pas optimsé et peut former
	des groupes abérrants.
	Il est conseillé de ne pas l'utiliser en marchant si l'accisition video
	est longue
    '''
	
    def AnalyseMultiImage(self,thresh=None,zone=None,cercle=None,poteau=None, dessin=True,nb_img=5,nb_matching=2):
	
		if nb_matching > nb_img :
			raise NameError ("nb_matching > nb_img")
		
		#PARTIE 1 : (pas super utile)
		#detection de zone uniquement :
		#on retourne vrai si on détecte au moins un px blanc dans la zone
		if zone is not None   and   cercle is None :
			for i in range(nb_img):
				if self.AnalyseImg(None,zone,cercle,poteau,dessin) == True :
					return True
			return False	
		
		
		#PARTIE 2 :
		#detection de cercles:
		#on analyse plusieurs images :
		detect_cercles = [] #contient tout les cercles détecté
		for i in range(nb_img):
			detect_cercles += self.AnalyseImg(None,zone,cercle,poteau,dessin)#ajout de nouveaux résultats dans "c" sur de nouvelles images
		
		#si on a aucun cercles on ne peux rien faire
		if not detect_cercles :
			return None
	
	
		#formation des groupes qui on une distance proche:
		pp = [] #va contenir la liste des points proches
		ajoutOk = False # pour savoir si l'ajout est effectif et sortir des boucles
		
		for cercle_p in detect_cercles :
			c = cercle_p[0]#le pourcentage ne nous intéresse pas
			ajoutOk = False
			for groupe in pp :
				#on recherche dans ce groupe si le point est proche de "c":
				for g in groupe :
					#on ajoute dans ce ce groupe si un des cercles nous est proche
					#on est proche si l'un des 2 cercles on une intersection
					dist = DU.distance(g,c)
					if dist <= (g.rayon*2) or  dist <= (c.rayon*2) :
						groupe.append(c)
						ajoutOk = True
						break
				if ajoutOk :
					break
					
			#si le cercle "c" n'a pus être ajouté on forme un nouveau groupe
			#va initialiser pp si il n'y a aucun groupe
			if not ajoutOk :
				pp.append([c])
		
		#détermination de où ce trouve la balle :
		#prendre le cercle qui à le rayon médian...
		pg_groupe = [] # =le ou les plus grands groupes
		taille = 0 #taille du groupe
		for groupe in pp :
			#on trouve un plus grand groupe:
			if taille < len(groupe):
				pg_groupe = []#vide la liste
				pg_groupe += [groupe]
				taille = len(groupe)
			#on trouve un groupe de la même taille:
			elif taille == len(groupe) :
				pg_groupe += [groupe]
		
		#on stop si les groupes de points ne sont pas assé dense
		if taille < nb_matching :
			print "pas assé de points dans le groupe"
			return None
		
		#on choisit le groupe au hazard (si il en a plusieurs):
		random.seed()
		r = random.randint(0,len(pg_groupe)-1)
		the_groupe = pg_groupe[r]
		
		#on calcul la position moyenne de tout les points (cercle) :
		posx = 0
		posy = 0
		for cg in the_groupe :
			posx+= cg.x
			posy+= cg.y
			r+= cg.rayon
		
		posx/=len(the_groupe)
		posy/=len(the_groupe)
		r/=len(the_groupe)
		
		return DU.Cercle((posx,posy),r)
		
	
	#TODO : commenter !!!!!!
	#COMMENT : problème cette distance au centre ne ce fait que avec des cercles 
	#il faudrait que ce soit possible de passer des coordonées et/ou des cercles
	# exemple :
	#getAngle(cercle) possible
	#getAngle((100,150)) possible
	#prend en paramètre un cercle et calcul angle qui permet de centrer 
	#le cercle dans l'iage
    def getAngle(self, cercle):
        centre = self.getCentreImage()
        pxVision = self.camera.getResolution() #self.getPxVision()
        vectX, vectY = DU.distanceDuCentre(cercle,centre)#mm commentaire
        angleX = DU.pxToRad(vectX, pxVision[0])
        return angleX


    #TODO : commenter
    def meilleureBalle(self, listeBalles):
        meilleurCercle, meilleurPourcent = None, 0
        for (cercle,pourcent) in listeBalles:
            if pourcent > meilleurPourcent:
                meilleurCercle, meilleurPourcent = cercle, pourcent
                
        return meilleurCercle	

    '''
	takeOk(self):
	----------------------------
	retourne vrai si la ball est aux bonnes coordonées pour être prise
    '''
    def takeOk(self):
		#Pitch de la tête entre 25° Yaw = 0°
		mh = Head(self.motion,self.posture)
		mh.turnTo(math.radians(0),math.radians(25))
		z = self.getZoneTake()
		print "la zone:",z#INFO developpeur

		#ancienne version 
		c = self.AnalyseImg(zone=z,cercle=70)#TODO ici faire une analyse fine !!
		if len(c) > 0 :
			return True
		else :
			return False

		"""
		#nouvelle version en cours de teste :
		c = self.AnalyseMultiImage(zone=z,cercle=70,nb_img=5,nb_matching=3)
		if c is not None:
			return True
		else :
			return False
		"""
		
		
    '''
	VrtOk(self):
	--------------------------
	sert à placer le robot à la bonne position verticalment
	pour prendre la balle.
	retourne "ok" si la position vertical de la balle est bonne
			 "droite" si il faut allé à droite
			 "gauche" si il faut allé à gauche
			 None aucun cercle trouvé
    '''
    def VertOk(self):
		#Pitch de la tête entre 25° Yaw = 0°:
		mh = Head(self.motion,self.posture)
		mh.turnTo(math.radians(0),math.radians(25))
		zone_v = self.getZoneTake()
		zone_v.dy = self.camera.getResolution()[1]
		zone_v.y = 0
		
		my_thresh = None
		#on situe ou est la balle
		self.camera.setCameraBas()
		
		cercle = self.AnalyseMultiImage(thresh=my_thresh,cercle=70,nb_img=1,nb_matching=1)
		DU.dessineZone(self.imageCourante,zone_v,color=(255,255,0))#dessiner la zone_v
		DU.dessineZone(self.imageCourante,self.getZoneTake())
		#debug : 
		self.afficheImagesCourantes()		
		#cv2.waitKey(0)
		
		
		if cercle is None :
			return None
		
		if zone_v.isIn(cercle) :
			return "ok"
		else :
			if zone_v.x < cercle.x :
				return "droite"
			else :
				return "gauche"
		
		
    '''
	HrzOk(self):
	---------------------------
	sert à placer le robot à la bonne position horizontalement
	pour prendre la balle.
	retourne "ok" si la position vertical de la balle est bonne
			 "avant" si il faut allé vers l'avant
			 "arrière" si il faut allé vers l'arrière
			 None aucun cercle trouvé
    '''
    def HrzOk(self):
    	#Pitch de la tête entre 25° Yaw = 0°:
		mh = Head(self.motion,self.posture)
		mh.turnTo(math.radians(0),math.radians(25))
		zone_h = self.getZoneTake()
		zone_h.dx = self.camera.getResolution()[0]
		zone_h.x = 0
		
		
		#on situe ou est la balle
		self.camera.setCameraBas()
		#cercle = self.AnalyseMultiImage(cercle=70,nb_img=1,nb_matching=1)
		cercle = self.AnalyseMultiImage(cercle=70,nb_img=1,nb_matching=1)
		DU.dessineZone(self.imageCourante,zone_h,color=(255,0,0))#dessiner la zone_h
		DU.dessineZone(self.imageCourante,self.getZoneTake())
		#debug : 
		self.afficheImagesCourantes()		
		#cv2.waitKey(0)
		
		if cercle is None :
			return None
		
		if zone_h.isIn(cercle) :
			return "ok"
		else :
			if zone_h.y < cercle.y :
				return "arriere"
			else :
				return "avant"
	
    '''
	getZoneTake(self):
	---------------------------
	retourne la zone où la balle doit être prise en fonction de la résolution
    '''
    def getZoneTake(self):
		width = self.camera.getResolution()[0]
		
		#ceci est la zone idéale pour la résolution kVGA :
		x=87
		y=295
		dx = 30
		dy = 30
		
		if   width == 640 :
			return DU.Zone((x,y),dx,dy)
		elif width == 320 :
			return DU.Zone((x//2,y//2),dx//2,dy//2)
		elif width == 160 :
			return DU.Zone((x//4,y//4),dx//4,dy//4)	
		else :
			return DU.Zone((x*2,y*2),dx*2,dy*2)

        
