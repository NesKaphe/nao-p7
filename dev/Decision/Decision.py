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
        
        
    '''
    run (self, demo=0):
    ----------------------------
    liste des demonstrations : 
	0 : lancement complet du programme
	1 : recherche uniquement
	2 : recherche et marche
	3 : approche de balle
	4 : ramasser la balle
	5 : approche et ramasser la balle
    '''
    def run (self, demo=0, verbose = True):
	""" #TODO: a virer
	#self.initialisation()
        #self.a.filtre.calibrage()


        #TEST CLEMENT
        #self.modePositionneBalle()
        print "PASSE EN MODE PRENDRE BALLE"
        self.modePrendreBalle()
        #self.modeRechercheBalle()

		#teste Alain
        pourcentageRecherche = 70
        cameraFinRecherche = self.modeRecherche(pourcentage=pourcentageRecherche)
        while self.marcheVersBalle(cameraFinRecherche) == False:
            print "On a perdu la balle... il faut rechercher a nouveau la balle"
            pourcentageRecherche -= 20
            cameraFinRecherche = self.modeRecherche(pourcentage=pourcentageRecherche)
        
        print "On doit maintenant essayer de s'approcher de la balle"
        self.a.afficheImagesCourantes() #petit affichage pour voir
	
	#self.modePositionneBalle()
	"""
	texte = "Lancement de : "

	if demo == 1: #recherche uniquement
	    doRecherche = True
	    doMarche = False
	    doPosition = False
	    doRamasse = False
	    doLancer = False
	    texte = texte+" Recherche"

	elif demo == 2: #recherche et marche
	    doRecherche = True
	    doMarche = True
	    doPosition = False
	    doRamasse = False
	    doLancer = False
	    texte = texte+" Recherche et marche"

	elif demo == 3: #approche de balle
	    doRecherche = False
	    doMarche = False
	    doPosition = True
	    doRamasse = False
	    doLancer = False
	    texte = texte+" Approche de balle"
	
	elif demo == 4: #ramasser la balle
	    doRecherche = False
	    doMarche = False
	    doPosition = False
	    doRamasse = True
	    doLancer = False
	    texte = texte+" Ramasser la balle"

	elif demo == 5: #approcher et ramasser la balle
	    doRecherche = False
	    doMarche = False
	    doPosition = True
	    doRamasse = True
	    doLancer = False
	    texte = texte+" Approcher et ramasser la balle"

	elif demo == 6:
	    doRecherche = False
	    doMarche = False
	    doPosition = False
	    doRamasse = True
	    doLancer = True
	    texte = texte+" Ramasser et lancer la balle"

	else: #Par defaut on lance le programme completment
	    doRecherche = True
	    doMarche = True
	    doPosition = True
	    doRamasse = True
	    doLancer = True
	    texte = texte+" Programme complet"

	print texte

        trouve = False
        marche = True
        position = False
	ramasse = False
        fin = False
        

	pourcentageRecherche = 70
		
        while fin is not True:
		if doRecherche is True:
			if trouve is False :
				zoneMarche = self.modeRecherche(pourcentage=pourcentageRecherche)
				trouve = True
		else:
			trouve = True
			zoneMarche = None

		if doMarche is True:
			if self.marcheVersBalle(zoneMarche) is False  and   marche is True:
				print "On a perdu la balle... il faut rechercher a nouveau la balle"
				trouve = False
				continue
			else :
				marche = False
		else:
			marche = False

		if doPosition is True:
			if self.modePositionneBalle() is False :
				print "modePositionneBalle : balle perdu"
				trouve = False
				marche = True
				position = False
			else :
				print "modePositionneBalle : "
				position = True
		else:
			position = True

		if doRamasse is True:
			if position is True :
				if self.modePrendreBalle() is False :
					position = False
					ramasse = False
				else:
					ramasse = True

		else:
			ramasse = True


		if doLancer is True:
			if ramasse is True:
				self.modeLancer()

		#On va regarder si on a remplis toutes les conditions
		if trouve is True and marche is False and position is True and ramasse is True:
			fin = True
	
	print "Execution terminée"

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
    marcheVersBalle va avancer jusqu'a ce que la balle soit totalement perdue
    Ce mode va chercher a faire une approche grossière jusqu'a la balle
    '''
    def marcheVersBalle(self, zone_marche = None):
        print "debut mode : marcheVersBalle"

        camera = self.a.camera.getActiveCamera() 

        resolution = self.a.camera.getResolution()
        '''
        ZONES
        '''
        zoneBas_camera_haut = DU.Zone((0, (5 * resolution[1]/6)), resolution[0], resolution[1]/6)

        #Zones de recherche globale de la balle
        if zone_marche is None:
            zone_camera_haut = DU.Zone((0,resolution[1]/2), resolution[0], resolution[1] /2 )
        else:
            if zone_marche.y > zoneBas_camera_haut:
                zone_camera_haut = zone_marche

        

        zoneBas_camera_bas = DU.Zone((0, (5 * resolution[1])/6), resolution[0], resolution[1]/5)
        
        #Zone centrale que l'on regardera en priorité durant la marche vers la balle
        zoneCentre_camera_haut = DU.Zone((2 * resolution[0]/4, resolution[1]/2), resolution[0]/4, resolution[1]/2)
        zoneCentre_camera_bas  = DU.Zone((2 * resolution[0]/4, 0), resolution[0]/4, resolution[1])

        angle = 0
        cerclesP = []
        nbSpeculationsTotalCentre = 1 #Le nombre de fois qu'on fera comme si on avait vu la balle dans le cas ou on n'en voit pas durant l'analyse
        nbSpeculationsTotal = 0
        nbSpeculations = nbSpeculationsTotal
        nbSpeculationsCentre = nbSpeculationsTotalCentre
        while True:
            #On va analyser l'image
            centre = False

            if camera == 0:
                #cerclesP = self.a.AnalyseImg(zone=zone_camera_haut, cercle=60)
                self.a.afficheImagesCourantes()
                #balle = self.a.meilleureBalle(cerclesP)
                balle = self.a.AnalyseMultiImage(zone=zone_camera_haut, cercle=60)
                #centre = self.a.testZone(zoneCentre_camera_haut)
                print balle
                if balle is not None:
                    centre = zoneCentre_camera_haut.isIn(balle)
                else:
                    centre =  False
            else:
                #cerclesP = self.a.AnalyseImg(cercle=60)
                self.a.afficheImagesCourantes()
                #balle = self.a.meilleureBalle(cerclesP)
                balle = self.a.AnalyseMultiImage(cercle=60)
                #centre = self.a.testZone(zoneCentre_camera_bas)
                print balle
                if balle is not None:
                    centre = zoneCentre_camera_bas.isIn(balle)
                else: centre = False
            
            

            #On va essayer de chercher au centre dans un premier temps
            if centre:
                if zoneBas_camera_bas.isIn(balle) and camera == 1:
                    #On s'est rapproché de la balle, on arrete de marcher et on renvoie True
                    self.motion.stopMove()
                    return True
               
                elif zoneBas_camera_haut.isIn(balle) and camera == 0:
                    #on va changer de camera car la balle va passer dans le champ de vision de la camera du bas
                    print "Je change de camera car je peux continuer avec la camera du bas"
                    self.a.switchCamera()
                    camera = 1
                    nbSpeculations = nbSpeculationsTotal
                    nbSpeculationsCentre = nbSpeculationsTotalCentre

                print "La balle est au centre de l'image donc je vais tout droit"
                nbSpeculationsCentre = nbSpeculationsTotalCentre
                angle = 0

            else: #Sinon, on va voir dans l'image où est la balle
                if nbSpeculationsCentre <= 0: #On a regardé trop longtemps le centre uniquement
                    print "Je n'ai pas vu la balle au centre, je vais tenter de me redresser"
                    print balle
                    if balle is not None:
                        nbSpeculations = nbSpeculationsTotal #On remet notre compteur de speculation à l'état initial
                        nbSpeculationsCentre = nbSpeculationsTotalCentre
                    
                        if zoneBas_camera_bas.isIn(balle) and camera == 1: #Si on est dans la zone basse de la camera du bas
                    #On s'est rapproché de la balle, on arrete de marcher et on renvoie True
                            self.motion.stopMove()
                            return True
                        elif zoneBas_camera_haut.isIn(balle) and camera == 0:
                            #on va changer de camera
                            print "Je change de camera car je peux continuer avec la camera du bas"
                            self.a.switchCamera()
                            camera = 1
                            nbSpeculations = nbSpeculationsTotal
                            nbSpeculationsCentre = nbSpeculationsTotalCentre

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
                            #nbSpeculationsCentre = nbSpeculationsTotalCentre
                            continue #On recommence la boucle après notre changement de camera
                        else: #On a completement perdu la balle, on renvoie False car il faut repasser en mode recherche de balle
                            self.motion.stopMove()
                            return False
                else: #On retire une boucle de verification du centre
                    print "Je n'ai pas vu la balle au centre, mais je continue quand même"
                    nbSpeculationsCentre -= 1
                    angle = 0 #On va aller tout droit

            #On va maintenant changer l'angle de marche
            print "DEBUG : l'angle de rotation est de ", angle
            #self.motion.setWalkTargetVelocity(0.5,0,angle,0.3)
            self.motion.moveTo(0.08,0,angle)

        print "fin mode : marcheVersBalle"       


    '''
	modePrendreBalle(self):
	---------------------------------------
	c'est le mode ou le robot va ce mettre à croupis
	et prendre la balle. Et ce relever.
    '''
    def modePrendreBalle(self):#premiere vesion pour prendre la balle
 		print "debut mode : modePrendreBalle" 
		mo = Move(self.motion,self.posture)
		mo.deboutPrendre()
		self.a.setCameraBas()
	
		cpt = 0
		while not self.a.takeOk() :
			print "je ne peux pas prendre la balle"
			self.a.afficheImagesCourantes()
			cv2.waitKey(0)
			cpt+=1
			if cpt > 30 :
				return False
		print "je peux prendre la balle!"
		mo.aCroupris()#TODO modifier l'angle de tete pour 
		print "ici je dois prendre la balle!!"
		"""
		while True :
			pos = a.AnalyseImg(zone=zo,cercle=70)#pour dessiner la zone et le cercle
			if pos != [] :
				print "pos = ",pos[0][0]
			a.afficheImagesCourantes()
		"""
		#ici faire aussi un check sur les capteurs
		mo.relever()
		#mo.fermeMain()
		#ici il faudrait faire une fonction check hand (verif main) 
		print "fin mode : modePrendreBalle"
		return True



    '''
	modeRecherche(self, typeRecherche="balle"):
	-----------------------------------------
	mode qui permet de rerchercher la balle autour du robot ou les poteaux
    '''
    def modeRecherche(self, typeRecherche="balle", pourcentage=70):

	#tourner en rond sur lui meme jusqu'à trouver la balle
        #alterner entre camera du haut et camera du bas entre chaque position
	#reduire le pourcentage si on ne trouve pas la balle
	#utilisation de redBall traking
	#si on trouve toujours pas prendre le rouge pour cible
	#si il a plusieurs balles prendre celle qui est plus à gauche
        #une fois la balle trouvée, tourner le robot le plus possible vers la balle
        
        if typeRecherche != "balle" and typeRecherche != "poteau":
            print "[modeRecherche] : Type de recherche inconnu : ", typeRecherche
            raise Exception

        cameraNao = 0
        self.a.setCameraHaut() #On commence la recherche avec la camera du haut
        mh = Head(self.motion,self.posture)
        mo = Move(self.motion,self.posture)
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
        	#TODO : remplacer par AnalyseMultiImg !! AVOIR !!
        	#----------------------------------------
            """
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
            """
            
            if cameraNao == 0:
                balle = self.a.AnalyseMultiImage(zone=zone_camera_haut, cercle=pourcentage, nb_matching=3)
            else:
                balle = self.a.AnalyseMultiImage(cercle=pourcentage, nb_matching=3)
            
            if balle is not None:
                trouve = True
                 #----------------------------------------
                 #----------------------------------------
            if not trouve:
                self.a.afficheImagesCourantes()
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
        print "La balle choisie est : ", balle
        self.a.afficheImagesCourantes()
        '''
        while True:
            key = cv2.waitKey(33)
            key -= 0x100000
            if key == 113: #on quitte avec la touche q
                break 
        '''
        #Calcul de l'angle pour centrer la balle
        angleBalleImage = self.a.getAngle(balle)
        #On ajoute l'angle de la tete a l'angle calculé pour savoir de combien le corps devra se tourner 

        angleYaw = mh.getYawAngle()

        mh.reset() #on remet la tete droite
        #on tourne le corps
        mo.turnTo(angleBalleImage + angleYaw)
        haut_zone = balle.y - 20
        if haut_zone < 0:
            haut_zone = 0
        zone_marche = DU.Zone((0, haut_zone), resolution[0], (resolution[1] - haut_zone))
        return zone_marche



    """
	modePositionneBalle(self):
	----------------------------------------------------------
	C'est le mode qui permet de ce positionner au bon endroit
	pret de la balle.
	retourne faux si la balle est considéré comme perdu
	retourne vrai si la balle est à la bonne position
    """
    def modePositionneBalle(self):
		print "debut mode : modePositionneBalle"
		cameraNao = 0
		a = Analyse(self.videoProxy,self.motion,self.posture,camera=cameraNao)
		mo = Move(self.motion,self.posture)
		
		cpt_bp = 0 #compteur de balles perdu
		cpt_max = 4 #max de balle perdu
		#on continu tant que la position de la balle n'est pas bonne
		while not a.takeOk() :
		
			#placement horizontal:
			while True :
				h = a.HrzOk()
				print "h = ",h
				if h is None :
					cpt_bp+=1
				elif h == "ok" :
					pass
				elif h == "avant":
					mo.pasEnAvant()
				elif h == "arriere":
					mo.pasEnArriere()
					
				if cpt_bp >= cpt_max :
					return False
					
			#placement vertical :
				vert = a.VertOk()
				print "vert =",vert
				if vert is None :
					cpt_bp+=1
				elif vert == "ok" :
					pass
				elif vert == "gauche":
					print "debug nao pas à gauche"
					mo.pasAGauche()
				elif vert == "droite":
					print "debug nao pas à droite"
					mo.pasADroite()
				
				#sortir si on est ok
				if h == "ok" and vert == "ok" :
					print "position ok"
					return True
				
				if cpt_bp >= cpt_max :
					return False
		
		print "fin mode : modePositionneBalle"
		return True
				

    def modeLancer(self):
	mo = Move(self.motion,self.posture)
	#mo.deboutMarche()
	mo.lancer()


    def initialisation(self):
        mh = Head(self.motion,self.posture)
        mo = Move(self.motion, self.posture)
        
        mo.debout()
        mh.reset() #Regard devant soi
        

