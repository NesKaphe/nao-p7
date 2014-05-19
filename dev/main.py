# -*- coding: utf-8 -*-

from Decision.Decision import *
#import Decision
#from Analyse import Analyse
import time

calibrage = False

if len(sys.argv) > 1 and len(sys.argv) == 2:
	if sys.argv[1] == "-c":
		calibrage = True
	else:
		print "Paramètre ",sys.argv[1], " inconnu"
		exit(1)

while True:
	try :
		if calibrage is True:
			filtre = FilterColor()
			filtre.calibrage()
			calibrage = False #Calibrage effecté, on ne le recommencera pas

		print "start"
		de = Decision()
		break
	except KeyboardInterrupt:
		break
"""
	except Exception as e:#en cas d'exception non prévu par les développeurs le code redémarre
		print "error ",e
		print "restart dans 3 secondes"
		time.sleep(3)
		#TODO : rajouter un sleep de 3 secondes !! afficher 3 2 1 restart

"""
