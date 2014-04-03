import cv2
import numpy as np
cap = cv2.VideoCapture(0)
 
while True:
    ret,im = cap.read()
    ret2,im2 = cap.read()
    
    #superposition des deux images pour les avoir dans la meme fenetre avec imshow
    im3 = np.concatenate((im,im2),axis=1)
    cv2.imshow('video test',im3)
    key = cv2.waitKey(10)

    key -= 0x100000
    if key == 113: #on quitte avec la touche q
        break

