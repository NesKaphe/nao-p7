# -*- coding: utf-8 -*-
#problème j'ai oublier de mettre ça donc il n'y a pas d'accent dans le code
import cv2
import cv2.cv as cv
import numpy as np
import time
import math


'''
classe Abstraite forme, pour la detection de forme
'''
class Forme(object):
    def __init__(self, (x,y)):
        self.x = x
        self.y = y

    def getCentre(self):
        raise NotImplementedError("La methode getCentre n'est pas implementé dans la classe abstraite Forme")


'''
class Cercle, pour la detection de balle
'''
class Cercle(Forme):
    def __init__(self, (x,y), rayon):
        super(Cercle,self).__init__((x,y))
        self.rayon = rayon

    def getCentre(self):
        return (self.x, self.y)

    def __str__(self):
        return "(("+str(self.x)+","+str(self.y)+"),"+str(self.rayon)+")"


'''
class Rectangle, pour la detection de poteau
'''
class Rectangle(Forme):
    def __init__(self, (x,y), cote1, cote2):
        super(Rectangle,self).__init__((x,y))
        self.cote1 = cote1
        self.cote2 = cote2

    def getCentre(self):
        return (self.x+self.cote1, self.y+self.cote2)

    def __str__(self):
        return "(("+str(self.x)+","+str(self.y)+"),"+str(self.cote1)+","+str(self.cote2)+")"


"""
class zone coordonées x,y plus la dimension dx,dy si dy = None la zone est carré 
"""
class Zone():
	def __init__(self,(x,y),dx,dy=None) :
		if x<0 or y<0 :
			raise NameError ("zone malformée")
		self.x,self.y = (x,y)
		self.dx = dx
		if dy is None :
			self.dy = dx
		else :
			self.dy = dy
		
	def __str__(self):
		return "("+str(self.x)+","+str(self.y)+"), dx:"+str(self.dx)+" dy:"+str(self.dy)

		
	def isIn(self,forme):#prend le centre d'un cercle et répond si le cercle est dans la zone
		centre = forme.getCentre()
		testX = (centre[0] >= self.x) and (centre[0] <= self.x+self.dx)#on évide de dupliquer le teste
		if self.dy is not None :
			return testX and (centre[1] >= self.y) and (centre[1] <= self.y+self.dy)
		else :
			return testX and (centre[1] >= self.y) and (centre[1] <= self.y+self.dx)




"""
createEmptyThresh (shape):
-----------------------------------
permet de creer une image thresh de la bonne dimension
"""
def createEmptyThresh (shape):
	return np.zeros(shape,dtype=np.uint8) #thresh de la bonne taille et vide (noir ou plein de zeros partout)


"""
vide(img_th):
-----------------------------------
renvoi si le threch est vide ou non (il y au moins un pixel blanc)
"""
def vide(img_th):
	return not(img_th.any())


"""
isInlist(l,element) :
------------------------------------
savoir si un element est dans la liste
"""
def isInlist(l,element) :
	for e in l :
		if e == element :
			return True
	return False



"""
union(img_th0,img_th1):
-------------------------------------
recupere 2 images thresh les compares en gardant tout les elements qui ont une intersection
retourne une image thresh avec les résultats des comparaisons
"""
def union(img_th0,img_th1):	
	if img_th0.shape != img_th1.shape :
		raise NameError("les threshs n'ont pas la meme dimension")
	conts0,h0 = cv2.findContours(img_th0.copy(),cv.CV_RETR_EXTERNAL ,cv.CV_CHAIN_APPROX_NONE)#contours img	1
	conts1,h1 = cv2.findContours(img_th1.copy(),cv.CV_RETR_EXTERNAL ,cv.CV_CHAIN_APPROX_NONE)# // 			2
	im_result = createEmptyThresh(img_th0.shape)#l'image thresh de resulat
	l_result0 = []#liste des numeros de contours0 (conts0) qui va premttre d'itentifier si le contours est deja pris en compte pour l'union
	l_result1 = []#liste des numeros de contours1 (conts1) qui va premttre d'itentifier si le contours est deja pris en compte pour l'union	
	l_des0 = []#liste contenant les different dessins des contours 	0
	l_des1 = []#			//										1
	if (conts0 is None) or (conts1 is None) :
		print "absolument aucun contours a comparer"
	else :#on dessine tout les contours 1 par 1:
		for i,c0 in enumerate(conts0) :
			#on dessine dans un thresh le contours :
			des0 = createEmptyThresh(img_th0.shape)#dessin du contour 0
			cv2.drawContours(des0,[c0],-1,(255,255,255),thickness=cv.CV_FILLED)
			l_des0.append(des0)			
		for j,c1 in enumerate(conts1) :
			#on dessine dans un thresh le contours :
			des1 = createEmptyThresh(img_th0.shape)#dessin du contour 0
			cv2.drawContours(des1,[c1],-1,(255,255,255),thickness=cv.CV_FILLED)
			l_des1.append(des1)
	#recherche d'intersections :
	for i,(des0,c0) in enumerate(zip(l_des0,conts0)) :
			for j,(des1,c1) in enumerate(zip(l_des1,conts1)) :
				inter = cv2.bitwise_and(des0,des1)#on dessine l'intersection			
				if not vide(inter) :#si il y a intersection
					#on ajoute a la liste des contours valides
					if not isInlist(l_result0,i) :
						l_result0.append(i)
					if not isInlist(l_result1,j) :
						l_result1.append(j)
					#on dessine directement le resultat :
					cv2.drawContours(im_result,[c0],-1,(0,255,255),thickness=cv.CV_FILLED)#dessin du contours 0#version avec couleur
					cv2.drawContours(im_result,[c1],-1,(0,0,255),thickness=cv.CV_FILLED)#dessin du contours 1#version avec couleur				
	return 	im_result
	
	
"""
unionV2(img_th0,img_th1):
------------------------------
version pour multiple_union() et autre du meme type
retourne que les contours
"""
def unionV2(img_th0,img_th1):	
	conts0,h0 = cv2.findContours(img_th0.copy(),cv.CV_RETR_EXTERNAL ,cv.CV_CHAIN_APPROX_NONE)#contours img	1
	conts1,h1 = cv2.findContours(img_th1.copy(),cv.CV_RETR_EXTERNAL ,cv.CV_CHAIN_APPROX_NONE)# // 			2
	l_result0 = []#liste des numeros de contours0 (conts0) qui va premttre d'itentifier si le contours est deja pris en compte pour l'union
	l_result1 = []#liste des numeros de contours1 (conts1) qui va premttre d'itentifier si le contours est deja pris en compte pour l'union
	conts_result0 =[]#va contenir la liste de tout les contours 0
	conts_result1 =[]#				//							1	
	l_des0 = []#liste contenant les different dessins des contours 	0
	l_des1 = []#			//										1
	if (conts0 is None) or (conts1 is None) :
		print "absolument aucun contours a comparer"
		pass 
	else :#on dessine tout les contours 1 par 1:
		for i,c0 in enumerate(conts0) :
			#on dessine dans un thresh le contours :
			des0 = createEmptyThresh(img_th0.shape)#dessin du contour 0
			cv2.drawContours(des0,[c0],-1,(255,255,255),thickness=cv.CV_FILLED)
			l_des0.append(des0)			
		for j,c1 in enumerate(conts1) :
			#on dessine dans un thresh le contours :
			des1 = createEmptyThresh(img_th0.shape)#dessin du contour 0
			cv2.drawContours(des1,[c1],-1,(255,255,255),thickness=cv.CV_FILLED)
			l_des1.append(des1)
	#recherche d'intersections :
	for i,(des0,c0) in enumerate(zip(l_des0,conts0)) :
			for j,(des1,c1) in enumerate(zip(l_des1,conts1)) :
				inter = cv2.bitwise_and(des0,des1)#on dessine l'intersection			
				if not vide(inter) :#si il y a intersection
					#on ajoute a la liste des contours valides
					if not isInlist(l_result0,i) :
						l_result0.append(i)
						conts_result0.append(c0)
					if not isInlist(l_result1,j) :
						l_result1.append(j)
						conts_result1.append(c1)					
	return 	conts_result0,conts_result1


"""
multipleUnion (imgs):
--------------------------------
parametre :
imgs = une liste d'images thresh
calcul absolument toute les unions possibles
##attention performance faible de plus en plus faible si il à trop d'image
"""
def multipleUnion (imgs):
	if len(imgs) <2 :
		raise NameError("besoin d'au moins 2 images")	
	im_result = createEmptyThresh(imgs[0].shape)#l'image thresh de resulat	
	cpt = 0#compteur d'itteration
	nb_tr = len(imgs)*len(imgs)#nb traitements	
	for i,img0 in enumerate(imgs) :
		for j,img1 in enumerate(imgs) :
			cpt = cpt + 1
			print "traitement :",cpt,"/",nb_tr#info dev : message pour connaitre l'avancee
			if i != j : #on ne se compare pas soit meme
				conts0,conts1 = unionV2(img0[0],img1[0])
				if conts0 != [] :
					cv2.drawContours(im_result,conts0,-1,(255,255,255),thickness=cv.CV_FILLED)
				if conts1 !=[] :
					cv2.drawContours(im_result,conts1,-1,(255,255,255),thickness=cv.CV_FILLED)					
	return im_result


"""
multipleUnionSucc (imgs):
----------------------------
autre vesion qui transmet a son successeur l'image avec les unions
avantage : cette version est linéaire alors 
inconvénient : risque de perdre des donnees
"""
def multipleUnionSucc (imgs):
	if len(imgs) <2 :
		raise NameError("besoin d'au moins 2 images")		
	im_result = createEmptyThresh(imgs[0].shape)#va contenir le thresh resultant
	c0,c1 = unionV2(imgs[0][0],imgs[1][0])	
	if len(imgs) <2 :
		raise NameError("besoin d'au moins 2 images")
	for i in range(1,len(imgs)) :
		print "traitement :",i,"/",len(imgs)#info dev : message pour connaitre l'avancee
		conts0 =[]
		conts1 =[]
		#pour la premiere iterration on fait l'union des premieres images :
		if i == 1 :
			conts0,conts1 = unionV2(imgs[0][0],imgs[1][0])
		else:
			conts0,conts1 = unionV2(im_result,imgs[i][0])		
		if conts0 != [] :
			cv2.drawContours(im_result,conts0,-1,(255,255,255),thickness=cv.CV_FILLED)
		if conts1 !=[] :
			cv2.drawContours(im_result,conts1,-1,(255,255,255),thickness=cv.CV_FILLED)

	return im_result

	
'''
detectZone (thresh,zone):
---------------------------------
retourne vrai si la zone contient au moins un px blanc
'''
def detectZone (thresh,zone):
	x_max = thresh.shape[0]
	y_max = thresh.shape[1]
	if zone.x+zone.dx > x_max or zone.y+zone.dy > y_max :#éventuel erreur (la zone sera au maximum de la dimensions du thresh
		raise NameError ("la zone étudié est plus grande que le thresh")

	for r in range(zone.y,zone.y+zone.dy):#r et c sont à  l'envers de se que je pensais
		for c in range(zone.x,zone.x+zone.dx):
			if thresh[c,r] > 0 :
				return True
	
	return False #on a rien trouvé dans la zone
		

'''
dessineCercle (img, cercle):
----------------------------------
prend une image et dessine le cercle passé en paramètre dedans
'''
def dessineCercle(img,cercle):
	cv2.circle(img,cercle.getCentre(),cercle.rayon,(0,255,255),2)


'''
dessineRectangle (img, rectangle):
-----------------------------------
prend une image et dessine le rectangle passé en paramètre dedans
'''
def dessineRectangle(img,rectangle):
	cv2.rectangle(img,rectangle.getCentre(),(rectangle.cote1, rectangle.cote2),(0,255,255),2)


'''
dessineZone(img, z, color):
-----------------------------------
prend une image et dessine la zone passée en paramètre dedans
'''
def dessineZone(img,z,color=(0,256,0)):
	cv2.rectangle(img,(z.x,z.y),(z.x+z.dx,z.y+z.dy),color,2)



'''
calculPourcentage(rayon, contour):
-----------------------------------
Permet de calculer le taux de remplissage du cercle par rapport à
son cercle circonscrit
'''
def calculPourcentage(rayon, contour):
        aire_objet = cv2.contourArea(contour)
        aire_cercle = math.pi*rayon*rayon
        return (aire_objet/aire_cercle)*100


'''
calculPourcentagePoteau(largeur, hauteur, contour):
----------------------------------------------------
Permet de calculer le taux de remplissage du poteau par rapport
au rectangle qui l'englobe
'''
def calculPourcentagePoteau(largeur,hauteur, contour):
        aire_objet = cv2.contourArea(contour)
        aire_rectangle = largeur * hauteur
        return (aire_objet / aire_rectangle)*100



'''
detectCercle(thresh, pourcentage):
--------------------------------------
Va chercher dans l'image binaire tous les objets ayant le 
taux de remplissage de cercle demandé.
Cette methode retourne les cercles trouvés ainsi que leur
taux de remplissage
'''
def detectCercle(thresh, pourcentage):
	contours = cv2.findContours(thresh.copy(),
				    cv.CV_RETR_EXTERNAL,
				    cv.CV_CHAIN_APPROX_NONE)[0]
	if contours != None:
		liste = []
		for i in contours:
			approx = cv2.approxPolyDP(i,0.1*cv2.arcLength(i,True),True)
			(x,y),rayon = cv2.minEnclosingCircle(approx)
			centre = (int(x),int(y))
			rayon = int(rayon)
			pourcent = calculPourcentage(rayon,i)
			if pourcent > pourcentage:
				cercle = Cercle(centre,rayon)
				liste.append([cercle,pourcent])

		return liste

	return []


'''
detectCercleHough(thresh):
------------------------------
Va chercher dans l'image binaire tous les objets 
ayant une forme circulaire.
Cette methode utilise hough circles d'opencv
'''
def detecteCercleHough(thresh):
	circles = cv2.HoughCircles(thresh.copy(),
				   cv.CV_HOUGH_GRADIENT,2,15,param1=200,
				   param2=50,minRadius=10,maxRadius=100)
        liste = []
	if circles != None:
		circles = np.uint16(np.around(circles))
		for i in circles[0,:]:
		    cercle = Cercle(i[0],i[1])
		    liste.append(cercle)
        return liste
        

'''
detectePoteau(thresh, pourcentage):
------------------------------------
Va chercher dans l'image binaire tous les objets ayant le 
taux de remplissage de rectangle demandé.
Cette methode retourne les rectangles trouvés ainsi que leur
taux de remplissage
'''
def detectePoteau(thresh, pourcentage):
	contours = cv2.findContours(thresh.copy(),
				    cv.CV_RETR_EXTERNAL,
				    cv.CV_CHAIN_APPROX_NONE)[0]
	if contours != None:
		liste = []
		for i in contours:
			approx = cv2.approxPolyDP(i,0.02*cv2.arcLength(i,True),True)
			#if len(approx) == 4 and cv2.isContourConvex(approx) and cv2.contourArea(approx) > 0:
                        rect = cv2.minAreaRect(approx)
                        box = cv2.cv.BoxPoints(rect)
                        box = np.int0(box)
                        (x,y) = box[0]
                        (w, h) = box[1]
                        pourcent = calculPourcentagePoteau(w,h,approx)

                        if pourcent > pourcentage: 
                            rectangle = Rectangle((int(x),int(y)),int(w),int(h))
                            liste.append((rectangle,pourcent))

		return liste
	return []


'''
distanceDuCentre(cercle, (centreX, centreY):
--------------------------------------------
Va retourner la distance d'un cercle par rapport au centre de l'image
de la caméra. Cette methode prend en compte la direction des repères
du nao
'''
def distanceDuCentre(cercle, (centreX, centreY)):
	#Le repère du nao est inversé donc on multipliera par -1
	vectX = (cercle.x - centreX) * -1
	vectY = (cercle.y - centreY) * -1
	return vectX, vectY


'''
pxToRad(distance, pxVision):
------------------------------
Va convertir une distance en px vers des degrés en radians
'''
def pxToRad(distance, pxVision):
	angleVision = math.radians(60) #Le nao à un angle de vision de 60 degrés
	
	pxToAngle = angleVision/pxVision

	return distance * pxToAngle

'''
distance(c1,c2):
--------------------------------
calculer la distance entre 2 centre de cercle
mettre en paramètre un couple de points
'''
def distance(c1,c2):
	math.sqrt( math.pow(c1.x-c2.x,2) + math.pow(c1.y-c2.y,2) )


