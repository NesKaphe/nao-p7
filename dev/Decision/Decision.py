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

class Decision:
    def __init__(self):
        
        self.IP = "192.168.1.3"
        self.PORT = 9559
        self.motion = ALProxy("ALMotion", self.IP , self.PORT)
        self.posture = ALProxy("ALRobotPosture", self.IP , self.PORT)
        self.videoProxy = ALProxy("ALVideoDevice", self.IP, self.PORT)
        #self.rootine()
        self.marcheVersBalle()
        
    def rootine (self):
        #phase de calibrage
        a = Analyse(self.videoProxy)
        #a.filtre.calibrage()
        
        angle_vision = (60*math.pi)/180 #angle de vision en radian
        px_vision = 640     
        
        px_to_ang = angle_vision/640

        mh = Head(self.motion,self.posture)
        mh.reset()
        while True :
            DirBalle = a.BallPosition()
            #a.afficheImagesCourantes()
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
    
