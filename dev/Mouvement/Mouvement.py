# -*- coding: utf-8 -*-
'''
	Fichier contenant les mouvements
'''

import sys
from naoqi import ALProxy
from vision_definitions import *
import cv2
import cv2.cv as cv
import numpy as np
import time
import almath
import math#contien pi
import a_croupis
import relever
import lancer
import debout_prendre


"""
class Head
-------------------------------------------
Contient les methodes utilisées pour les mouvements
de tête du Nao
"""
class Head:
	def __init__(self,motion,posture):
		self.motion = motion
		self.posture = posture

		#correspond au temps/vitesse pour atteindre l'angle voulu
		self.incrSpeeds = 0.05
	
	"""
	getYawAngle (self):
	--------------------------------------------
	retourne l'angle Yaw de la tête en radians
	"""
	def getYawAngle (self):
		return self.motion.getAngles("HeadYaw",True)[0]

	"""
	getPitchAngle (self):
	--------------------------------------------
	retourne l'angle Pitch de la tête en radians
	"""
	def getPitchAngle (self):
		return self.motion.getAngles("HeadPitch",True)[0]


	"""
	turnTo(self,angleYaw,anglePitch,speedX=1.5,speedY=1.5):
	--------------------------------------------------------
	Va donner directement les angles à la tête.
	Les angles doivent être en radians.
	Un angle positif fera tourner la tête vers la gauche.
	Un angle négatif fera tourner la tête vers la droite.	
	Il est possible de controler les différentes vitesse de
	rotation des moteurs.
	"""
	def turnTo(self,angleYaw,anglePitch,speedX=1.5,speedY=1.5) :
		print "debug - angle = ",angleYaw,"  ",anglePitch
		self.motion.setStiffnesses("Head", 1.0)
		names  = ["HeadYaw", "HeadPitch"]
		angles = [angleYaw, anglePitch]
		times  = [speedX, speedY]
		isAbsolute = True
		self.motion.angleInterpolation(names, angles, times, isAbsolute)
		#print "mouvement tete - fini" #message de debug pour les developpeurs	
	
	"""
	tension (self, t):
	------------------------------------------------
	Permet de choisir l'état de rigidité des moteurs de la tête
	"""
	def tension (self,t):
		self.motion.setStiffnesses("Head", t)	

	"""
	incrAnglesTo(self,angleYaw,anglePitch,speedX=1.5,speedY=1.5):
	-------------------------------------------------------------
	Va incrementer les angles de la tete avec ceux en parametres.
	Les angles doivent être en radians
	Il est possible de contrôler les différentes vitesse 
	de rotation des moteurs
	"""
	def incrAnglesTo(self,angleYaw,anglePitch,speedX=1.5,speedY=1.5) :#
		self.motion.setStiffnesses("Head", 1.0)
		angleYaw += self.getYawAngle()
		anglePitch += self.getPitchAngle()
		names  = ["HeadYaw", "HeadPitch"]
		angles = [angleYaw, anglePitch]
		times  = [speedX, speedY]
		isAbsolute = True#?
		self.motion.angleInterpolation(names, angles, times, isAbsolute)
		#print "mouvement tete - fini" #Message de debug pour les developpeurs
	

	"""
	reset(self) :
	--------------------------------------------
	Remet les angles Yaw et Pitch à 0
	Nao regardera devant lui après un appel à
	cette methode
	"""
	def reset(self) :#met la tete à l'angle 0,0
		self.motion.setStiffnesses("Head", 1.0) 
		names  = ["HeadYaw", "HeadPitch"]
		angles = [0.0, 0.0]
		times  = [1.5, 1.5]
		isAbsolute = True
		self.motion.angleInterpolation(names, angles, times, isAbsolute)
		print "reset"



"""
class Move
------------------------------------------------
Contient les methodes utilisées pour les mouvements de
deplacements du Nao.
"""

class Move :
	def __init__(self,motion,posture):
		self.motion = motion
		self.posture = posture
		self.pas = 0.02#un pas représente 1 cm
	
	"""
	debout(self):
	-----------------------------------------
	Va mettre Nao en position debout avec le corps
	droit	
	"""
	def debout(self):
		self.posture.goToPosture("Stand", 0.5)	

	"""
	deboutMarche(self):
	-----------------------------------------
	Va mettre Nao en position debout comme durant
	la marche
	"""
	def deboutMarche(self):
		self.posture.goToPosture("StandInit", 0.5)

	"""
	deboutPrendre(self):
	------------------------------------------
	Va faire appel à un mouvement pré-enregistré
	grâce à choregraphe pour placer le robot en
	position debout pret à ramasser la balle
	"""
	def deboutPrendre(self):
		debout_prendre.move(self.motion)
	
	"""
	aCroupris(self):
	--------------------------------------------
	Va faire appel à un mouvement pré-enregistré
	grâce à choregraphe pour ramasser la balle
	"""	
	def aCroupris(self):
		a_croupis.move(self.motion)
	

	"""
	relever(self):
	--------------------------------------------
	Va faire appel à un mouvement pré-enregistré
	grâce à choregraphe pour relever le robot
	après la prise de balle
	"""
	def relever(self):
		relever.move(self.motion)

	"""
	lancer(self):
	--------------------------------------------
	Va faire appel à un mouvement pré-enregistré
	grâce à choregraphe pour lancer la balle
	en avant
	"""
	def lancer(self):
		lancer.move(self.motion)
	
	
	"""
	ouvreMain(self):
	--------------------------------------------
	Va ouvrir la main gauche de Nao
	"""
	def ouvreMain(self):
		self.motion.openHand("LHand")
	

	"""
	fermerMain(self):
	-------------------------------------------
	Va fermer la main gauche de Nao
	"""
	def fermeMain(self):
		self.motion.closeHand("LHand")
	
	
	"""
	turnTo(self,angle):
	------------------------------------------
	Va tourner le corps de Nao de l'angle passé
	en paramètre.
	L'angle doit être en radians
	"""
	def turnTo(self,angle):
		self.motion.moveTo(0,0,angle)
	

	"""
	Methodes de pas:
	-------------------------------------------
	Ces methodes vont permettre à Nao d'effectuer
	un unique pas.
	"""	
	def pasEnAvant(self):
		self.motion.moveTo(self.pas,0,0)
	

	def pasEnArriere(self):
		self.motion.moveTo(-self.pas,0,0)
	
	
	def pasAGauche(self):
		self.motion.moveTo(0,self.pas,0)
	
	
	def pasADroite(self):
		self.motion.moveTo(0,-self.pas,0)
