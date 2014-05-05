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
        self.modePrendreBalle()
        #self.routine4()
        #self.routine3()
        #self.modeRechercheBalle()





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



    def routine4(self):#routine 4 je crois qu'elle incrma
        mh = Head(self.motion,self.posture)
        mo = Move(self.motion,self.posture)
        a = Analyse(self.videoProxy,camera=1)
        mh.reset()
        #a.filtre.calibrage()
        mh.tension(0.0)
        while True:
            cercle = a.AnalyseImg()#manque des paramètres sinon ça marche pas
            if cercle is not None :
                angle = a.getAngle(cercle)
                print "cercle : ",cercle," : angle calculé =",(angle*180)/math.pi #TODO math.radian() à la place
                mh.incrAnglesTo(angle,0.0)



    def routine3(self): #teste pour la nouvelle fonction d'analyseImg
		a = Analyse(self.videoProxy,self.motion,self.posture,camera=1)
		z = DU.Zone((200,200),200)


		print"zone:",z
		#a.filtre.calibrage()#pour calibrer
		while True:
			cerclesZone = a.AnalyseImg(zone=z,cercle=70)
			print "cercles = ",cerclesZone
			a.afficheImagesCourantes()



    def modePrendreBalle(self):#premiere vesion pour prendre la balle
		mo = Move(self.motion,self.posture)
		a = Analyse(self.videoProxy,self.motion,self.posture,camera=1)
		mo.debout()
		while not a.takeOk() :
			print "je ne peux pas prendre la balle"
			a.afficheImagesCourantes()
		print "je peux prendre la balle!"
		#mo.ouvreMain()#ouvrir la main gauche
		mo.aCroupris()
		print "ici je dois prendre la balle!!"
		time.sleep(2)#attente histoire de ..
		#ici faire aussi un check sur les capteurs
		mo.relever()
		mo.fermeMain()
		#ici il faudrait faire une fonction check hand (verif main) 





    def modeRechercheBalle(self):
	#tourner en rond sur lui meme jusqu'à trouver la balle
        #alterner entre camera du haut et camera du bas entre chaque position
	#reduire le pourcentage si on trouve pas 
	#utilisation de redBall traking
	#si on trouve toujours pas prendre le rouge pour cible
	#si il a plusieurs balles prendre celle qui est plus à gauche

        cameraNao = 0
        mh = Head(self.motion,self.posture)
        mo = Move(self.motion,self.posture)
        a = Analyse(self.videoProxy,camera=cameraNao)
        pourcentage = 80
        self.initialisation()
        #a.filtre.calibrage(0)
        #a.filtre.calibrage(1)
        rotationsTete = 0
        rotationsCorps = 0
        direction = 1 #1 pour la gauche et -1 pour la droite
        trouve = False
        balle = None
        resolution = a.camera.getResolution()
        zone_camera_haut = DU.Zone((0,resolution[1]/2), resolution[0], resolution[1] /2 )

        while trouve is not True:
            nbImages = 5
            while nbImages > 0:
                if cameraNao == 0:
                    cerclesP = a.AnalyseImg(zone=zone_camera_haut, cercle=pourcentage)
                else:
                    cerclesP = a.AnalyseImg(cercle=pourcentage)

                if cerclesP != []:
                    trouve = True
                    balle = a.meilleureBalle(cerclesP)
                    break
                nbImages -= 1

            if not trouve:

                if cameraNao == 0:
                    a.switchCamera()
                    cameraNao += 1
                else:
                    a.switchCamera()
                    cameraNao = 0
                    if rotationsTete < 4: #Si on n'a pas la balle, on va tourner la tete
                        if rotationsTete > 0 and rotationsTete % 2 == 0:
                            mh.reset() #On remet la tete droite
                            direction *= -1

                        angleIncr = direction * math.pi/4
                        mh.incrAnglesTo(angleIncr,0.0)
                        rotationsTete += 1

                    else: #On doit maintenant bouger le corps
                        rotationsTete = 0
                        mh.reset()
                        mo.seRetourner()
                        rotationsCorps = 1
                        if rorationsCorps % 2 == 0:
                            rotationsCorps = 0
                            #On reduit finalement le pourcentage
                            pourcentage += 20
                            if pourcentage < 0:
                                pourcentage = 0
                            
        
        #ici on a trouvé la balle, il faudra surement enregistrer la zone ou autre
        print "La balle est : ", balle
        a.afficheImagesCourantes()
        while True:
            key = cv2.waitKey(33)
            key -= 0x100000
            if key == 113: #on quitte avec la touche q
                break 

        #Calcul de l'angle pour centrer la balle
        angleBalleImage = a.getAngle(balle)
        #On ajoute l'angle de la tete a l'angle calculé pour savoir de combien le corps devra se tourner 

        angleYaw = mh.getYawAngle()

        mh.reset() #on remet la tete droite
        #on tourne le corps

        mo.turnTo(angleBalleImage + angleYaw)







    def initialisation(self):
        mh = Head(self.motion,self.posture)
        mo = Move(self.motion, self.posture)
        
        mo.debout()
        mh.reset() #Regard devant soi







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

	
def modePrendreBalle(self):
	while ?? :
		#detection vertical
			#fixer le pitch
			#touner sur lui même jusqu'à avoir la balle situé dans la bonne vertical
"""

    
