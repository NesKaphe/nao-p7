# -*- coding: utf-8 -*-
'''
	Fichier contenant de désicion
'''

import sys
from naoqi import ALProxy
from Analyse.Analyse import *
from Analyse.Vision import *
from Mouvement.Mouvement import *
import math
import almath
import time
from Analyse.Vision import DetectUtils as DU

class Decision:
    def __init__(self):
        
        self.IP = "192.168.1.3"
        self.PORT = 9559
        self.motion = ALProxy("ALMotion", self.IP , self.PORT)
        self.posture = ALProxy("ALRobotPosture", self.IP , self.PORT)
        self.videoProxy = ALProxy("ALVideoDevice", self.IP, self.PORT)
        #self.rootine()

        #self.marcheVersBalle()
        #self.routine2()



        self.routine4()

        self.routine3()

    def routine (self):
        #phase de calibrage
        a = Analyse(self.videoProxy)
        a.filtre.calibrage()
        
        angle_vision = (60*math.pi)/180 #angle de vision en radian
        px_vision = 640     
        
        px_to_ang = angle_vision/640

        mh = Head(self.motion,self.posture)
        mh.reset()
        while True :
            DirBalle = a.BallPosition()
            a.afficheImagesCourantes()
            print "angle reel",(self.motion.getAngles("HeadYaw",True)[0]*180.0)/math.pi#," , ",self.motion.getAngles("HeadPitch",True)
            #print "DirBalle",DirBalle
            
            if DirBalle is not None :
                #x= -((60*DirBalle[0])/640)
                x = -(DirBalle[0]* px_to_ang)#+(math.pi /2)
                print "angle calculé =",(x*180)/math.pi
                mh.incrAnglesTo(x,0.0)
                #time.sleep(1)
            #mh.incrAngle(DirBalle[0],DirBalle[1])
        

    def marcheVersBalle(self):
        self.posture.goToPosture("Stand",0.5)
        a = Analyse(self.videoProxy, cam=1)
       #a.filtre.calibrage()
        self.motion.moveInit()
        #print "j'attends 10 secondes que tu deplaces la balle devant moi"
        #time.sleep(10)
        if a.BallPosition() is not None: #On reporte le probleme de dectection a plus tard
            print "Non, je vois deja la balle"
            a.afficheImagesCourantes()
            while True:
                key = cv2.waitKey(33)
                key -= 0x100000
                if key == 113: #on quitte avec la touche q
                    break
        else:
            self.motion.moveToward(1,0,0) #marche vers l'avant
            while a.BallPosition() == None:
                a.afficheImagesCourantes()
                time.sleep(0.5)
            self.motion.stopMove() #On arrete le mouvement
            print "Je vois la balle"
            a.afficheImagesCourantes()
            while True:
                key = cv2.waitKey(33)
                key -= 0x100000
                if key == 113: #on quitte avec la touche q
                    break

    
    def routine2(self):#teste pour tourner la tête au bon endroit
        mh = Head(self.motion,self.posture)
        mo = Move(self.motion,self.posture)
        a = Analyse(self.videoProxy,camera=1)
        #a.filtre.calibrage()

        mo.debout()

        mh.tension(0.0)

        while True :
            DirBalle = a.BallPosition()
            a.afficheImagesCourantes()
            print "angle reel Pitch",\
            (self.motion.getAngles("HeadPitch",True)[0]*180.0)/math.pi," Yaw :",\
            (self.motion.getAngles("HeadYaw",True)[0]*180.0)/math.pi
        #mo.aCroupris()



    def routine4(self):
        mh = Head(self.motion,self.posture)
        mo = Move(self.motion,self.posture)
        a = Analyse(self.videoProxy,camera=1)
        mh.reset()
        #a.filtre.calibrage()
        mh.tension(0.0)

        while True:
            cercle = a.AnalyseImg()
            if cercle is not None :
                angle = a.getAngle(cercle)
                print "cercle : ",cercle," : angle calculé =",(angle*180)/math.pi
                mh.incrAnglesTo(angle,0.0)


    def routine3(self): #teste pour la nouvelle fonction d'analyseImg
		a = Analyse(self.videoProxy,camera=1)
		z = DU.Zone((200,200),200)
		#a.filtre.calibrage()
		while True:
			cerclesZone = a.AnalyseImg(zone=z,cercle=70)
			print "cercles = ",cerclesZone
			a.afficheImagesCourantes()








"""
#princilament une recherche plus que du code  :

def TrackingBalle(self,center=True):
	#le robot va chercher la balle si center est true on là centre dans l'image sinon stop la tete dès que on trouve
	pass#voir routine 2
	#faire une version qui fixe l'angle pitch et faire touner le robot sur lui même
	#si une position à ete valider plusieurs fois on la considère comme valide
	
	
	
def modeRechercheBalle(self):
	#tourner en rond sur lui meme jusqu'à trouver la balle
	#reduire le pourcentage si on trouve pas 
	#utilisation de redBall traking
	#si on trouve toujours pas prendre le rouge pour cible
	#si il a plusieurs balles prendre celle qui est plus à gauche
	pass
	
def modeAvanceVersBalle(self)
	#tant que la balle n'est pas dans le champs de vision de la camera du bas
	#si la balle est légèrement à gauche ou à droite calculer un angle pour une trajectoire en
	#courbe
	#faire un processus en tache de fond qui recherche la balle toutes les secondes (centré dans l'image)
	#si la tête ne ce recentre pas automatiquement ou si la balle ne c'est pas raproché du centre
	
	pass
>>>>>>> bfd1f724dc3710f54dafbd814a043afe5b55f5ea
	
def modePrendreBalle(self):
	while ?? :
		#detection vertical
			#fixer le pitch
			#touner sur lui même jusqu'à avoir la balle situé dans la bonne vertical
"""

    
