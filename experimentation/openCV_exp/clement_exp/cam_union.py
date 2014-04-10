# -*- coding: utf-8 -*-
import cv2
import cv2.cv as cv
import numpy as np
import time
import math



#pour le thresh vide :
cap= None
ret= None
im= None
thresh_vide = None







def init_thresh_vide ():
	global im
	global thresh_vide
	if im is not None :
		#thresh_vide = np.zeros(im.shape,dtype=np.uint8) #thresh de la bonne taille et vide (noir ou plein de zeros partout)
		thresh_vide = np.zeros((im.shape[0], im.shape[1]),dtype=np.uint8) #thresh de la bonne taille et vide (noir ou plein de zeros partout)







def rien(x):
	pass




def getPercentage(radius,contour):
	aire_objet = cv2.contourArea(contour)
	aire_cercle = math.pi*radius*radius
	return (aire_objet/aire_cercle)*100






def get_one_img(id):
	global im
	global thresh_vide
	cap = cv2.VideoCapture(0)#a refaire a chaque fois si on veux une nouvelle imgage a l'instant t
	thresh = None #image apres le traitement 
	ret,im = cap.read()
	if thresh_vide is None :#initialisation du thresh vide
		init_thresh_vide ()
	im2 = cv2.cvtColor(im,cv2.COLOR_BGR2HSV)
	h1 = cv2.getTrackbarPos('H_MIN','cnt')
	h2 = cv2.getTrackbarPos('H_MAX','cnt')
	s1 = cv2.getTrackbarPos('S_MIN','cnt')
	s2 = cv2.getTrackbarPos('S_MAX','cnt')
	v1 = cv2.getTrackbarPos('V_MIN','cnt')
	v2 = cv2.getTrackbarPos('V_MAX','cnt')
	
	minDist = 10
	pourcent = 80
	med = cv2.getTrackbarPos('flou_mediant','cnt')
	glo = cv2.getTrackbarPos('flou_global','cnt')
	
	mini = np.array([h1,s1,v1],np.uint8)
	maxi = np.array([h2,s2,v2],np.uint8)
	
	############################################################
	#petit teste avec les differents flou
	#-median blur fait disparaire du bruit et lisse l'image
	# 	reduit le nombres de contours
	#-global blur 
	# 	arondis les formes
	# 	reduit le nombres de contours
	"""
	if med > 1 :
		__med =3
		if (med % 2) == 0:
			__med =  med+1
		else :
			__med = med
		im = cv2.medianBlur(im,__med)#pour le dev
		im2 = cv2.medianBlur(im2,__med)#im_hsv
	else :
		print "pas de median blur"
	if glo > 0 :
		im = cv2.blur(im,(glo,glo))#pour le dev
		im2 = cv2.blur(im2,(glo,glo))#im_hsv
	else :
		print "pas de global blur"
	"""
	im2 = cv2.medianBlur(im2,15)#im_hsv
	im2 = cv2.blur(im2,(6,6))#im_hsv
	#######################################################
		
	thresh = cv2.inRange(im2,mini,maxi)
	kernel = cv2.getStructuringElement(cv2.MORPH_ELLIPSE,(5,5))
	thresh = cv2.dilate(thresh,kernel,iterations=2)
	thresh = cv2.erode(thresh,kernel,iterations=1)

	#print "type thresh :",type(thresh),"  shape : ",thresh.shape#info dev
	
	#################################################################################################
	#Tout ce qui est mis en commentaire c'est pour reduire le temps de calcul
	"""
	contours = cv2.findContours(thresh.copy(),cv.CV_RETR_EXTERNAL ,cv.CV_CHAIN_APPROX_NONE)[0]
	if contours != None:
		for i in contours:
			approx = cv2.approxPolyDP(i,0.05*cv2.arcLength(i,True),True)
			#x,y,w,h = cv2.boundingRect(approx)
			(x,y),radius = cv2.minEnclosingCircle(approx)
			#cv2.rectangle(im,(x,y),(x+w,y+h),(0,255,0),2)
			center = (int(x),int(y))
			radius = int(radius)
			if getPercentage(radius,i) > pourcent:
				cv2.circle(im,center,radius,(0,255,255),2)
			cv2.drawContours(im,approx,-1,cv.CV_RGB(0,255,0))
	"""
	
	#TODO : manque des testes avec houghCircles
	"""
	circles = cv2.HoughCircles(thresh,cv.CV_HOUGH_GRADIENT,1,minDist,param1=50,param2=30,minRadius=0,maxRadius=0)
	if circles != None:
		circles = np.uint16(np.around(circles))
		print "cercle !!"
		for i in circles[0,:]:
			# draw the outer circle
			cv2.circle(im,(i[0],i[1]),i[2],(0,255,0),2)
			# draw the center of the circle
			cv2.circle(im,(i[0],i[1]),2,(0,0,255),3)
	"""		    
	#cv2.imshow("thresh"+str(id),thresh)
	#cv2.imshow("video"+str(id),im)
	#################################################################################################
	cv2.waitKey(1)
	return thresh,im,id




	



"""
revoi si le threch est vide ou non (il y au moins un pixel blanc)
"""
def vide(img_th):#
	return not(img_th.any())




"""
savoir si un element est dans la liste
"""
def is_inlist(l,element) :
	for e in l :
		if e == element :
			return True
	return False





"""
retourne vrai si il y a une intersection entre les 2 thresh d'image (2px blanc au meme endroit)
utiliser par union2
"""
def intersection2(img_th0,img_th1):#j'ai mis 2 pour tester une nouvelle version 
	print "runnig"
	for (row0,row1) in zip(img_th0,img_th1) :
		for (px0,px1) in zip(row0,row1) :
			#print "px :",px0," type :",type(px0),"  dtype",px0.dtype#info dev
			#TODO il est possible de reduire le nombre de testes en faisant le calcul logique
			if  (px0[0] != 0)\
			and (px0[1] != 0)\
			and (px0[2] != 0)\
			and	(px1[0] != 0)\
			and (px1[1] != 0)\
			and (px1[2] != 0)\
			and (px0[0] == px1[0]) :#ici on ne teste que la valeur R (de RBG) (parce que c'est soit noir '0x000' soit blanc '0xFFF') 
				return True
	
	return False


def intersection(img_th0,img_th1):#marche pas 
	im2 = img_th0.all() & img_th1.all()
	cv2.imshow("im2 = ",im2)#DEBUG
	cv2.waitKey(0)#DEBUG
	cv2.destroyAllWindows()#DEBUG
	return not vide(im2)
	
#TODO utiliser .all() 
#amelioration possible du champ de recherche en limitant aux lignes et aux colonnes des dessins .all([axis, out])
#sinon uniquement reduire la zone de recherche (si incompatible renvoyer none)



"""
recupere 2 images thresh les compares en gardant tout les elements qui ont une intersection
"""
def union(img_th0,img_th1):

	global thresh_vide
	
	conts0,h0 = cv2.findContours(img_th0.copy(),cv.CV_RETR_EXTERNAL ,cv.CV_CHAIN_APPROX_NONE)#contours img	1
	conts1,h1 = cv2.findContours(img_th1.copy(),cv.CV_RETR_EXTERNAL ,cv.CV_CHAIN_APPROX_NONE)# // 			2

	im_result = thresh_vide.copy()#l'image thresh de resulat
	l_result0 = []#liste des numeros de contours0 (conts0) qui va premttre d'itentifier si le contours est deja pris en compte pour l'union
	l_result1 = []#liste des numeros de contours1 (conts1) qui va premttre d'itentifier si le contours est deja pris en compte pour l'union
	
	
	l_des0 = []#liste contenant les different dessins des contours 	0
	l_des1 = []#			//										1
	
	

	if (conts0 is None) or (conts1 is None) :
		print "absolument aucun contours a comparer"
		pass 
	else :#on dessine tout les contours 1 par 1:
		for i,c0 in enumerate(conts0) :
			#on dessine dans un thresh le contours :
			des0 = thresh_vide.copy()#dessin du contour 0
			cv2.drawContours(des0,[c0],-1,(255,255,255),thickness=cv.CV_FILLED)
			l_des0.append(des0)
			
			
		for j,c1 in enumerate(conts1) :
			#on dessine dans un thresh le contours :
			des1 = thresh_vide.copy()#dessin du contour 0
			cv2.drawContours(des1,[c1],-1,(255,255,255),thickness=cv.CV_FILLED)
			l_des1.append(des1)

	#recherche d'intersections :
	for i,(des0,c0) in enumerate(zip(l_des0,conts0)) :
			for j,(des1,c1) in enumerate(zip(l_des1,conts1)) :
				inter = cv2.bitwise_and(des0,des1)#on dessine l'intersection
			
				if not vide(inter) :#si il y a intersection
					#on ajoute a la liste des contours valides
					if not is_inlist(l_result0,i) :
						l_result0.append(i)
					if not is_inlist(l_result1,j) :
						l_result1.append(j)

					#on dessine directement le resultat :
					cv2.drawContours(im_result,[c0],-1,(0,255,255),thickness=cv.CV_FILLED)#dessin du contours 0#version avec couleur
					cv2.drawContours(im_result,[c1],-1,(0,0,255),thickness=cv.CV_FILLED)#dessin du contours 1#version avec couleur

					
	return 	im_result



"""
version 2 (performances catastrophique)
recupere 2 images threch les compares en gardant tout les elements qui ont une intersection
"""
#TODO solution faire en sorte que intersection soit code en C ou C++ (parce que beacoup d'iterrations)
#ou regarder comment faire avec les fonctions de numpy

def union2(img_th0,img_th1):

	global thresh_vide
	
	conts0,h0 = cv2.findContours(img_th0.copy(),cv.CV_RETR_EXTERNAL ,cv.CV_CHAIN_APPROX_NONE)#contours img	1
	conts1,h1 = cv2.findContours(img_th1.copy(),cv.CV_RETR_EXTERNAL ,cv.CV_CHAIN_APPROX_NONE)# // 			2

	im_result = thresh_vide.copy()#l'image thresh de resulat
	l_result0 = []#liste des numeros de contours0 (conts0) qui va premttre d'itentifier si le contours est deja pris en compte pour l'union
	l_result1 = []#liste des numeros de contours1 (conts1) qui va premttre d'itentifier si le contours est deja pris en compte pour l'union
	
	l_des0 = []#liste contenant les different dessins des contours 	0
	l_des1 = []#			//										1
	
	

	if (conts0 is None) or (conts1 is None) :
		print "absolument aucun contours a comparer"
		pass 
	else :#on dessine tout les contours 1 par 1:
		for i,c0 in enumerate(conts0) :
			#on dessine dans un thresh le contours :
			des0 = thresh_vide.copy()#dessin du contour 0
			cv2.drawContours(des0,[c0],-1,(255,255,255),thickness=cv.CV_FILLED)
			l_des0.append(des0)
			
			
		for j,c1 in enumerate(conts1) :
			#on dessine dans un thresh le contours :
			des1 = thresh_vide.copy()#dessin du contour 0
			cv2.drawContours(des1,[c1],-1,(255,255,255),thickness=cv.CV_FILLED)
			l_des1.append(des1)

	print "nb elements img0 :", len(l_des0),"  img1:",len(l_des1)
	#recherche d'intersections :
	for i,(des0,c0) in enumerate(zip(l_des0,conts0)) :
			#print "i",i#DEBUG
			for j,(des1,c1) in enumerate(zip(l_des1,conts1)) :
				#print "j",j#DEBUG
				#si l'element est dans la liste on sort de la sous-boucle :
	
				
	
				if intersection(des0,des1) :#si il y a intersection
					#on ajoute a la liste des contours valides
					if not is_inlist(l_result0,i) :
						l_result0.append(i)
					if not is_inlist(l_result1,j) :
						l_result1.append(j)

					#on dessine directement le resultat :
					cv2.drawContours(im_result,[c0],-1,(0,255,255),thickness=cv.CV_FILLED)#dessin du contours 0
					cv2.drawContours(im_result,[c1],-1,(255,255,255),thickness=cv.CV_FILLED)#dessin du contours 1

	return 	im_result


def union3(img_th0,img_th1):#version pour multicontours ne retourne que les contours

	global thresh_vide
	
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
			des0 = thresh_vide.copy()#dessin du contour 0
			cv2.drawContours(des0,[c0],-1,(255,255,255),thickness=cv.CV_FILLED)
			l_des0.append(des0)
			
			
		for j,c1 in enumerate(conts1) :
			#on dessine dans un thresh le contours :
			des1 = thresh_vide.copy()#dessin du contour 0
			cv2.drawContours(des1,[c1],-1,(255,255,255),thickness=cv.CV_FILLED)
			l_des1.append(des1)

	#recherche d'intersections :
	p
	for i,(des0,c0) in enumerate(zip(l_des0,conts0)) :
			for j,(des1,c1) in enumerate(zip(l_des1,conts1)) :
				inter = cv2.bitwise_and(des0,des1)#on dessine l'intersection
			
				if not vide(inter) :#si il y a intersection
					#on ajoute a la liste des contours valides
					if not is_inlist(l_result0,i) :
						l_result0.append(i)
						conts_result0.append(c0)
					if not is_inlist(l_result1,j) :
						l_result1.append(j)
						conts_result1.append(c1)

					
	return 	conts_result0,conts_result1








#calcul absolument toute les unions possibles
#attention performance en tres gross baisse
def multiple_union (imgs):

	global thresh_vide
	
	im_result = thresh_vide.copy()#l'image thresh de resulat
	
	
	if len(imgs) <2 :
		raise NameError("besoin d'au moins 2 images")
		
	cpt = 0#compteur d'itteration
	nb_tr = len(imgs)*len(imgs)#nb traitements
	
	for i,img0 in enumerate(imgs) :
		for j,img1 in enumerate(imgs) :
			cpt = cpt + 1
			print "traitement :",cpt,"/",nb_tr#info dev : message pour connaitre l'avancee
			if i != j : #on ne se compare pas soit meme
				conts0,conts1 = union3(img0[0],img1[0])
				if conts0 != [] :
					cv2.drawContours(im_result,conts0,-1,(255,255,255),thickness=cv.CV_FILLED)
				if conts1 !=[] :
					cv2.drawContours(im_result,conts1,-1,(255,255,255),thickness=cv.CV_FILLED)

					
	return im_result

"""
autre vesion qui transmet a son successeur l'image avec les unions (attention risque de perdre des donnees)
"""
def multiple_union_succ (imgs):

	global thresh_vide
	im_result = thresh_vide.copy()#va contenir le thresh resultant
	
	c0,c1 = union3(imgs[0][0],imgs[1][0])
	
	if len(imgs) <2 :
		raise NameError("besoin d'au moins 2 images")
	for i in range(1,len(imgs)) :
		print "it :",i,"/",len(imgs)
		
		conts0 =[]
		conts1 =[]
		#pour la premiere iterration on fait l'union des premieres images :
		if i == 1 :
			conts0,conts1 = union3(imgs[0][0],imgs[1][0])
		else:
			conts0,conts1 = union3(im_result,imgs[i][0])
		
		if conts0 != [] :
			cv2.drawContours(im_result,conts0,-1,(255,255,255),thickness=cv.CV_FILLED)
		if conts1 !=[] :
			cv2.drawContours(im_result,conts1,-1,(255,255,255),thickness=cv.CV_FILLED)

	return im_result

##########################################################################################
##########################################################################################
##########################################################################################
####TESTES DES ZONES AVEC DES THRESH
##########################################################################################
##########################################################################################

"""
class Cercle :
"""
class Cercle:
	def __init__(self, (x,y), rayon):
		self.x = x
		self.y = y
		self.rayon = rayon

	def __str__(self):
		return "(("+str(self.x)+","+str(self.y)+"),"+str(self.rayon)+")"


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

		
	def isIn(self,cercle):
		testX = (cercle.x >= self.x) and (cercle.x <= self.x+self.dx)#on évide de dupliquer le teste
		if self.dy is not None :
			return testX and (cercle.y >= self.y) and (cercle.y <= self.y+self.dy)
		else :
			return testX and (cercle.y >= self.y) and (cercle.y <= self.y+self.dx)
			
			
def detectZone (thresh,zone):
	
	x_max = thresh.shape[0]
	y_max = thresh.shape[1]
	if zone.x+zone.dx > x_max or zone.y+zone.dy > y_max :#éventuel erreur (la zone sera au maximum de la dimensions du thresh
		raise NameError ("la zone étudié est plus grande que le thresh")

	"""
	#vesion qui prend 3 plombes
	for r in range(zone.y,zone.y+zone.dy):#r et c sont à  l'envers de se que je pensais
		for c in range(zone.x,zone.x+zone.dx):
			if thresh[c,r] > 0 :
				return True
	"""
	#version qui utilise les fonctions numpy (du C compilé) donc plus rapide vv
	return thresh[zone.y:zone.y+zone.dy,zone.x:zone.x+zone.dx].any()
	
	#return False #on a rien trouvé dans la zone
##########################################################################################
##########################################################################################
##########################################################################################
##########################################################################################
##########################################################################################


def main() :
	global cap
	global ret
	global im
	global thresh_vide

	cv2.namedWindow("cnt",cv.CV_WINDOW_AUTOSIZE)



	#variables pour le trackbar
	#(jour avec cyan)
	"""
	h1=127
	h2=193
	s1=89
	s2=255
	v1=106
	v2=144
	"""
	
	#(nuit cercle rouge)
	"""
	h1=0
	h2=11
	s1=197
	s2=255
	v1=125
	v2=186
	"""
	
	#reglage amphi
	h1=0
	h2=255
	s1=0
	s2=255
	v1=125
	v2=186
	
	
		
	med=15
	glo=5
	
	
	#creation des trackbar
	cv.CreateTrackbar("H_MIN","cnt",h1,255,rien)
	cv.CreateTrackbar("H_MAX","cnt",h2,255,rien)
	cv.CreateTrackbar("S_MIN","cnt",s1,255,rien)
	cv.CreateTrackbar("S_MAX","cnt",s2,255,rien)
	cv.CreateTrackbar("V_MIN","cnt",v1,255,rien)
	cv.CreateTrackbar("V_MAX","cnt",v2,255,rien)
	cv.CreateTrackbar("flou_mediant","cnt",med,30,rien)
	cv.CreateTrackbar("flou_global","cnt",glo,30,rien)


	
	#premiers testes intersection difference et somme :
	"""
	t1,i1,id1 = get_one_img(0)
	cv2.waitKey(0)
	
	t2,i2,id2 = get_one_img(2)
	cv2.waitKey(0)
	
	
	t3 = cv2.add(t1,t2)
	inter = cv2.bitwise_and(t1,t2)
	t5 = cv2.absdiff(t1,t2)
	
	cv2.imshow("somme",t3)
	cv2.imshow("intersection",inter)
	cv2.imshow("difference",t5)
	"""
	
	#reglages :
	#pour faire des reglages rapides 
	#(noter les valeurs hsv qui nous interessent) ctrl+c pour sortir 
	"""
	while True :
		get_one_img(1)
	"""
	
	#teste d'union simple :
	"""
	print "image 0"
	img0 = get_one_img(0)
	print "image 1"
	cv2.waitKey(0)#attendre l'utilisateur
	img1 = get_one_img(1)
	
	u = union(img0[0],img1[0])
	
	cv2.imshow("img0 ", img0[0])
	cv2.imshow("img1 ", img1[0])
	cv2.imshow("fusion !!! ", u)
	"""
	#teste d'unions multiples :
	"""
	print "image 0?"
	cv2.waitKey(0)#attendre l'utilisateur
	img0 = get_one_img(0)
	print "image 1?"
	cv2.waitKey(0)#attendre l'utilisateur
	img1 = get_one_img(1)
	print "image 2?"
	cv2.waitKey(0)#attendre l'utilisateur
	img2 = get_one_img(2)
	print "image 3?"
	cv2.waitKey(0)#attendre l'utilisateur
	img3 = get_one_img(3)
	
	imgs = [img0,img1,img2,img3]
	tps1 = time.clock()#calcul du temps
	mu = multiple_union(imgs)#LE Coeur du code
	tps2 = time.clock()#calcul du temps
	print"temps mis par multiple_union :",(tps2 - tps1)
		
	cv2.imshow("img0 ", img0[0])
	cv2.imshow("img1 ", img1[0])
	cv2.imshow("img2 ", img2[0])
	cv2.imshow("img3 ", img3[0])
	cv2.imshow("multi fusion !!! ", mu)
	"""
	"""
	##############################################################
	#ICI C'est le banc de teste :
	#teste d'unions multiples succ
	print "image 0?"
	cv2.waitKey(0)#attendre l'utilisateur
	img0 = get_one_img(0)
	print "image 1?"
	cv2.waitKey(0)#attendre l'utilisateur
	img1 = get_one_img(1)
	print "image 2?"
	cv2.waitKey(0)#attendre l'utilisateur
	img2 = get_one_img(2)
	print "image 3?"
	cv2.waitKey(0)#attendre l'utilisateur
	img3 = get_one_img(3)
	
	imgs = [img0,img1,img2,img3]
	tps1 = time.clock()#calcul du temps
	mu = multiple_union_succ(imgs)#LE Coeur du code
	tps2 = time.clock()#calcul du temps
	print"temps mis par multiple_union :",(tps2 - tps1)
		
	cv2.imshow("img0 ", img0[0])
	cv2.imshow("img1 ", img1[0])
	cv2.imshow("img2 ", img2[0])
	cv2.imshow("img3 ", img3[0])
	cv2.imshow("multi fusion !!! ", mu)
	"""
	
	print "image 0?"
	cv2.waitKey(0)#attendre l'utilisateur
	img0 = get_one_img(0)
	z = Zone ((0,0),img0[0].shape[0],img0[0].shape[1])#toute l'image
	#z = Zone ((200,200),100)#toute l'image
	
	
	
	print "shape =",img0[0].shape
	print z
	while True:
		img0 = get_one_img(0)
		
		
		tps1 = time.clock()#calcul du temps
		print "y a t'il quelque chose dans la zone? ",detectZone (img0[0],z)
		tps2 = time.clock()#calcul du temps
		print"temps mis par detectZone :",(tps2 - tps1)
		
		
		cv2.rectangle(img0[0],(z.x,z.y),(z.y+z.dy,z.x+z.dx),(128,128,128),5)#pour dessiner la zone
		cv2.imshow("img0 ", img0[0])
	
	#############################################################
	
	cv2.waitKey(0)#fermer si il a y une touche appuye
	cv2.destroyAllWindows()

	
	

main()
