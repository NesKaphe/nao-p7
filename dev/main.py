# -*- coding: utf-8 -*-

from Decision.Decision import *
#import Decision
#from Analyse import Analyse
import time


while True:
	try :
		print "start"
		de = Decision()
		break
	except KeyboardInterrupt:
		break
	except Exception as e:#en cas d'exception non prévu par les développeurs le code redémarre
		print "error ",e
		print "restart dans 3 secondes"
		time.sleep(3)
		#TODO : rajouter un sleep de 3 secondes !! afficher 3 2 1 restart

