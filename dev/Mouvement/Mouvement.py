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


IP = "192.168.1.3"
PORT = 9559

class Head:
	def __init__(self,motion,posture):
		self.motion = motion
		self.posture = posture
		#correspond au temps/vitesse pour atteindre l'angle voulut
		self.incrSpeeds = 0.05
		self.step = 0.02 #correspond au "pas" précis
	
	def getYawAngle (self):#retourne l'angle Yaw en radian
		return self.motion.getAngles("HeadYaw",True)[0]

	def getPitchAngle (self):#retourne l'angle Pitch en radian
		return self.motion.getAngles("HeadPitch",True)[0]


	def turnTo(self,angleYaw,anglePitch,speedX=1.5,speedY=1.5) :#va donner les angles directement a la tête (angle en radian)
		self.motion.setStiffnesses("Head", 1.0)
		names  = ["HeadYaw", "HeadPitch"]
		angles = [angleYaw, anglePitch]
		times  = [speedX, speedY]
		isAbsolute = True#?
		self.motion.angleInterpolation(names, angles, times, isAbsolute)
		#ici voir si il y a besion de relacher le stiffnesse
		print "mouvement tete - fini"		
	
	def tension (self,t):
		self.motion.setStiffnesses("Head", t)	

	def incrAnglesTo(self,angleYaw,anglePitch,speedX=1.5,speedY=1.5) :#va donner les angles directement a la tête (angle en radian)
		self.motion.setStiffnesses("Head", 1.0)

		angleYaw += self.getYawAngle()
		anglePitch += self.getPitchAngle()

		names  = ["HeadYaw", "HeadPitch"]
		angles = [angleYaw, anglePitch]
		times  = [speedX, speedY]
		isAbsolute = True#?
		self.motion.angleInterpolation(names, angles, times, isAbsolute)
		#ici voir si il y a besion de relacher le stiffnesse
		print "mouvement tete - fini"


		
	def incrAngles(self,dirX,dirY) :#incrémenter l'angle d'un "pas"(step)
		self.motion.setStiffnesses("Head", 1.0) 
		names  = ["HeadYaw", "HeadPitch"]
		angleYaw =  self.getYawAngle() + self.angleYaw+(dirX*self.step)
		anglePitch = self.getPitchAngle() + self.anglePitch+(dirY*self.step)
		angles = [angleYaw,anglePitch]
		times  = [self.incrSpeeds, self.incrSpeeds]
		isAbsolute = True#?
		self.motion.angleInterpolation(names, angles, times, isAbsolute)	

		
	def reset(self) :#met la tete à l'angle 0,0
		self.motion.setStiffnesses("Head", 1.0) 
		names  = ["HeadYaw", "HeadPitch"]
		angles = [0.0, 0.0]
		times  = [1.5, 1.5]
		isAbsolute = True#??
		self.motion.angleInterpolation(names, angles, times, isAbsolute)
		print "reset"


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

"""
contient tout ce qui concerne la marche
"""

class Move :
	def __init__(self,motion,posture):
		self.motion = motion
		self.posture = posture
	
	def debout(self):
		self.posture.goToPosture("Stand", 0.5)
		#self.motion.moveInit()	

	def marche(self):
		self.debout()
		pass
		
	def aCroupris(self):
		a_croupis.move(self.motion)
	
	def seRetourner(self):
		self.motion.moveTo(0,0,math.pi)
	
	def turnTo(self,angle):
		self.motion.moveTo(0,0,angle)
