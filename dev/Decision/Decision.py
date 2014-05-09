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
        self.a = Analyse(self.videoProxy, self.motion, self.posture, camera=0)
        
        self.initialisation()
        #self.a.filtre.calibrage()
        #self.rootine()

        #self.routine2()
        #self.modePrendreBalle()
        #self.routine4()
        #self.routine3()
        
        cameraFinRecherche = self.modeRecherche()
        while self.marcheVersBalle(cameraFinRecherche) == False:
            print "On a perdu la balle... il faut rechercher a nouveau la balle"
            cameraFinRecherche = self.modeRecherche()
        
        print "On doit maintenant essayer de s'approcher de la balle"
        self.a.afficheImagesCourantes() #petit affichage pour voir

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
        

    '''
    TODO: VIEILLE VERSION
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
    '''

    '''
    marcheVersBalle va avancer jusqu'a ce que la balle soit totalement perdue
    Ce mode va chercher a faire une approche grossière jusqu'a la balle
    '''
    def marcheVersBalle(self, cameraDebut = 0):
        camera = cameraDebut #On va commencer avec la camera demandée en paramètre
        if camera == 0:
            self.a.setCameraHaut()
        else:
            self.a.setCameraBas()

        resolution = self.a.camera.getResolution()
        '''
        ZONES
        '''
        #Zones de recherche globale de la balle
        zone_camera_haut = DU.Zone((0,resolution[1]/2), resolution[0], resolution[1] /2 )
        zoneBas_camera_bas = DU.Zone((0, (4 * resolution[1])/5), resolution[0], resolution[1]/5)
        
        #Zone centrale que l'on regardera en priorité durant la marche vers la balle
        zoneCentre_camera_haut = DU.Zone((resolution[0]/3, resolution[1]/2), resolution[0]/3, resolution[1]/2)
        zoneCentre_camera_bas  = DU.Zone((resolution[0]/3, 0), resolution[0]/3, resolution[1])

        angle = 0
        cerclesP = []
        nbSpeculationsTotalCentre = 2 #Le nombre de fois qu'on fera comme si on avait vu la balle dans le cas ou on n'en voit pas durant l'analyse
        nbSpeculationsTotal = 0
        nbSpeculations = nbSpeculationsTotal
        nbSpeculationsCentre = nbSpeculationsTotalCentre
        while True:
            #On va analyser l'image
            centre = False

            if camera == 0:
                cerclesP = self.a.AnalyseImg(zone_camera_haut, cercle=60)
                self.a.afficheImagesCourantes()
                balle = self.a.meilleureBalle(cerclesP)
                #centre = self.a.testZone(zoneCentre_camera_haut)
                print balle
                if balle is not None:
                    centre = zoneCentre_camera_haut.isIn(balle)
                else:
                    centre =  False
            else:
                cerclesP = self.a.AnalyseImg(cercle=60)
                self.a.afficheImagesCourantes()
                balle = self.a.meilleureBalle(cerclesP)
                #centre = self.a.testZone(zoneCentre_camera_bas)
                print balle
                if balle is not None:
                    centre = zoneCentre_camera_bas.isIn(balle)
                else: centre = False
            
            

            #On va essayer de chercher au centre dans un premier temps
            if centre:
                print "La balle est au centre de l'image donc je vais tout droit"
                nbSpeculationsCentre = nbSpeculationsTotalCentre
                angle = 0

            else: #Sinon, on va voir dans l'image où est la balle
                if nbSpeculationsCentre <= 0: #On a regardé trop longtemps le centre uniquement
                    print "Je n'ai pas vu la balle au centre, je vais tenter de me redresser"
                    print cerclesP
                    if cerclesP != []:
                        nbSpeculations = nbSpeculationsTotal #On remet notre compteur de speculation à l'état initial
                        nbSpeculationsCentre = nbSpeculationsTotalCentre
                    
                        if zoneBas_camera_bas.isIn(balle) and camera == 1: #Si on est dans la zone basse de la camera du bas
                    #On s'est rapproché de la balle, on arrete de marcher et on renvoie True
                            self.motion.stopMove()
                            return True
                    
                        angle = self.a.getAngle(balle)
                        print "Balle vue !"
                    else: 
                        print "Balle non vue !"
                        if nbSpeculations > 0:
                            print "Je fais comme si elle etait devant moi tout de même"
                            angle = 0 #On fait comme si la balle etait devant nous
                            nbSpeculations -= 1
                        elif camera == 0:
                            print "Je change de camera"
                            self.a.switchCamera() #On passe maintenant a la camera du bas
                            camera = 1
                            nbSpeculations = nbSpeculationsTotal
                            nbSpeculationsCentre = nbSpeculationsTotalCentre
                            continue #On recommence la boucle après notre changement de camera
                        else: #On a completement perdu la balle, on renvoie False car il faut repasser en mode recherche de balle
                            self.motion.stopMove()
                            return False
                else: #On retire une boucle de verification du centre
                    print "Je n'ai pas vu la balle devant moi, mais je continue quand même"
                    nbSpeculationsCentre -= 1
                    angle = 0 #On va aller tout droit

            #On va maintenant changer l'angle de marche
            print "DEBUG : l'angle de rotation est de ", angle
            #self.motion.setWalkTargetVelocity(0.5,0,angle,0.3)
            self.motion.moveTo(0.08,0,angle)
    
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





    def modeRecherche(self, typeRecherche="balle"):
	#tourner en rond sur lui meme jusqu'à trouver la balle
        #alterner entre camera du haut et camera du bas entre chaque position
	#reduire le pourcentage si on ne trouve pas la balle
	#utilisation de redBall traking
	#si on trouve toujours pas prendre le rouge pour cible
	#si il a plusieurs balles prendre celle qui est plus à gauche
        #une fois la balle trouvée, tourner le robot le plus possible vers la balle

        if typeRecherche != "balle" and typeRecherche != "poteau":
            print "[modeRecherche] : Type inconnu : ", typeRecherche
            raise Exception

        cameraNao = 0
        self.a.setCameraHaut() #On commence la recherche avec la camera du haut
        mh = Head(self.motion,self.posture)
        mo = Move(self.motion,self.posture)
        pourcentage = 80
        self.initialisation()
        #self.a.filtre.calibrage(0)
        #self.a.filtre.calibrage(1)
        rotationsTete = 0
        rotationsCorps = 0
        direction = 1 #1 pour la gauche et -1 pour la droite
        trouve = False
        balle = None
        
        resolution = self.a.camera.getResolution()
        zone_camera_haut = DU.Zone((0,resolution[1]/2), resolution[0], resolution[1] /2 )

        while trouve is not True:
            nbImages = 5
            while nbImages > 0:
                if cameraNao == 0:
                    cerclesP = self.a.AnalyseImg(zone=zone_camera_haut, cercle=pourcentage)
                else:
                    cerclesP = self.a.AnalyseImg(cercle=pourcentage)

                if cerclesP != []:
                    trouve = True
                    balle = self.a.meilleureBalle(cerclesP)
                    break
                nbImages -= 1

            if not trouve:

                if cameraNao == 0:
                    self.a.switchCamera()
                    cameraNao += 1
                else:
                    self.a.switchCamera()
                    cameraNao = 0
                    if rotationsTete < 4: #Si on n'a pas la balle, on va tourner la tete
                        #if rotationsTete > 0 and rotationsTete % 2 == 0:
                        if rotationsTete > 0:
                            mh.reset() #On remet la tete droite
                            direction *= -1

                        #angleIncr = direction * math.pi/4
                        angleIncr = direction * math.radians(60)
                        mh.incrAnglesTo(angleIncr,0.0)
                        rotationsTete += 1

                    else: #On doit maintenant bouger le corps
                        rotationsTete = 0
                        mh.reset()
                        #mo.seRetourner()
                        mo.turnTo(math.pi/2)

                        #rotationsCorps = 1 #OLD
                        rotationsCorps += 1

                        #if rotationsCorps % 2 == 0: #OLD
                        if rorationsCorps % 4 == 0:
                            rotationsCorps = 0
                            #On reduit finalement le pourcentage
                            pourcentage -= 20
                            if pourcentage < 0:
                                pourcentage = 0
                            
        
        #ici on a trouvé la balle, il faudra surement enregistrer la zone ou autre
        print "La balle est : ", balle
        self.a.afficheImagesCourantes()
        while True:
            key = cv2.waitKey(33)
            key -= 0x100000
            if key == 113: #on quitte avec la touche q
                break 

        #Calcul de l'angle pour centrer la balle
        angleBalleImage = self.a.getAngle(balle)
        #On ajoute l'angle de la tete a l'angle calculé pour savoir de combien le corps devra se tourner 

        angleYaw = mh.getYawAngle()

        mh.reset() #on remet la tete droite
        #on tourne le corps

        mo.turnTo(angleBalleImage + angleYaw)

        return cameraNao





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

    
