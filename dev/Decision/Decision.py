# -*- coding: utf-8 -*-
'''
	Fichier contenant de désicion
'''

import sys
from naoqi import ALProxy
from Analyse.Analyse import *
from Analyse.Vision import *
from Mouvement.Mouvement import *


class Decision:
    def __init__(self):
        
        self.IP = "192.168.1.3"
        self.PORT = 9559
        self.motion = ALProxy("ALMotion", self.IP , self.PORT)
        self.posture = ALProxy("ALRobotPosture", self.IP , self.PORT)
        self.videoProxy = ALProxy("ALVideoDevice", self.IP, self.PORT)
        self.rootine()
        
    def rootine (self):
        #phase de calibrage
        a = Analyse(self.videoProxy)
        #a.filtre.calibrage()
        
        
        
        mh = Head(self.motion,self.posture)
        while True :
            DirBalle = a.BallPosition()
            a.afficheImagesCourantes()
            print "DirBalle",DirBalle
            #mh.incrAngle(DirBalle[0],DirBalle[1])
        
