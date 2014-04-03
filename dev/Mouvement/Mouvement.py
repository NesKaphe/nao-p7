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


IP = "192.168.1.3"
PORT = 9559

class Head:
	def __init__(self,motion,posture):
		self.motion = motion
		self.posture = posture
		self.angleYaw = 0.0 #récupérer les angles plustôt que ça
		self.anglePitch = 0.0 #récupérer les angles plustôt que ça
		#correspond au temps/vitesse pour atteindre l'angle voulut
		self.incrSpeeds = 0.05
		self.step = 0.02 #correspond au "pas" précis
		
	def turnTo(self,angleX,angleY,speedX=1.5,speedY=1.5) :#va donner les angles directement a la tête (angle en degré)
		self.motion.setStiffnesses("Head", 1.0)
		angleYaw= angleX*almath.TO_RAD
		anglePitch = angleY*almath.TO_RAD

		names  = ["HeadYaw", "HeadPitch"]
		angles = [angleYaw, anglePitch]
		times  = [speedX, speedY]
		isAbsolute = True#??
		self.motion.angleInterpolation(names, angles, times, isAbsolute)
		#ici voir si il y a besion de relacher le stiffnesse
		print "mouvement tete - fini"
		
		
	def reset(self) :#met la tete à l'angle 0,0
		self.motion.setStiffnesses("Head", 1.0) 
		names  = ["HeadYaw", "HeadPitch"]
		angles = [0.0, 0.0]
		times  = [1.5, 1.5]
		isAbsolute = True#??
		self.motion.angleInterpolation(names, angles, times, isAbsolute)
		print "reset"
		
	def incrAngles(self,dirX,dirY) :#incrémenter l'angle d'un "pas"(step)
		self.motion.setStiffnesses("Head", 1.0) 
		names  = ["HeadYaw", "HeadPitch"]
		self.angleYaw = self.angleYaw+(dirX*self.step)
		self.anglePitch = self.anglePitch+(dirY*self.step)
		angles = [self.angleYaw,self.anglePitch]
		times  = [self.incrSpeeds, self.incrSpeeds]
		isAbsolute = True#??
		self.motion.angleInterpolation(names, angles, times, isAbsolute)	




	def test (self):#petit teste pour faire des mouvements de tete
		i=2
		while (i!=0) :
			self.turnTo(50.0,50.0)
			self.turnTo(50.0,-50.0)
			self.turnTo(-50.0,-50.0)
			self.turnTo(-50.0,50.0)
			i-=1
		self.reset()
	
	def test2 (self) :#petit teste pour faire des mouvements de tete
		#self.posture.goToPosture("StandInit",0.5)
		i=100
		while (i!=0) :
			self.incrAngles(dirX=-1,dirY=0)
			print i
			i-=1
		i=100
		while (i!=0) :
			self.incrAngles(dirX=1,dirY=0)
			print i
			i-=1

"""
#petit test
h = Head()	
h.test2()
h.reset()
h.motion.setStiffnesses("Head", 0.0)
print "fin"
"""

