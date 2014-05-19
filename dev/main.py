# -*- coding: utf-8 -*-

from Decision.Decision import *
#import Decision
#from Analyse import Analyse
import time

calibrage = False
demo = 0

if len(sys.argv) > 1 and len(sys.argv) == 2:
	if sys.argv[1] == "calibrage":
		calibrage = True
	elif sys.argv[1] == "complet":
		demo = 0
	elif sys.argv[1] == "recherche":
		demo = 1
	elif sys.argv[1] == "rechMarche":
		demo = 2
	elif sys.argv[1] == "approche":
		demo = 3
	elif sys.argv[1] == "ramasse":
		demo = 4
	elif sys.argv[1] == "approcheRamasse":
		demo = 5
	elif sys.argv[1] == "lancer":
		demo = 6
	else:
		print "Paramètre ",sys.argv[1], " inconnu"
		exit(1)

while True:
	try :
		print "start"
		de = Decision()
		de.initialisation()

		if calibrage is True:
			filtre = FilterColor()
			filtre.calibrage()
			calibrage = False #Calibrage effecté, on ne le recommencera pas

		de.run(demo) #On lance notre demonstration
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
