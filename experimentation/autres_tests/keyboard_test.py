import sys,pygame
#from pygame import event ,key
from pygame.locals import *

pygame.init()

def clavier():
	try:
		keys = pygame.key.get_pressed()
		#print "type de keys",type(keys[0])
		#print keys
	
		if keys[pygame.locals.K_LEFT] :
			print "left"
		if keys[pygame.locals.K_RIGHT]:
			print "right"  
		if keys[pygame.locals.K_UP]:
			print "up"
		if keys[pygame.locals.K_DOWN]:
			print "down"
		if keys[pygame.locals.K_q]:
			print "quit"
			#return False
		"""
		else :
			print "rien"
		"""
	except Exception, e:
		print "probleme",e
		#return False
		
	#return True



def main():
	print "hello"
	while True :
 		clavier()

	print "fin"


main()

