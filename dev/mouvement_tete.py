from Analyse import Analyse
from Mouvement import *

def main() :
	analyse = Analyse()
	mouvement = Mouvement()
	
	
	while True :
		coord = analyse.BallPosition()
		print "rien"
		if coord != None :
			print coord
			mouvement.incrAngles(dirX=coord[0],dirY=coord[1])



main()
