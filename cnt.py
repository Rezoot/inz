import cv2
import numpy as np



cap = cv2.VideoCapture(0)    
fgbg3 = cv2.bgsegm.createBackgroundSubtractorCNT()

 
ret, frame1 = cap.read()    
 
 
def convert_to_gray(frame):
# Oblicz wartość jasności pikseli przy użyciu odpowiednich wag dla każdego kanału
     gray = frame[:, :, 0] * 0.114 + frame[:, :, 1] * 0.587 + frame[:, :, 2] * 0.299
     return gray.astype('uint8')

frame1=convert_to_gray(frame1)
 
 
while(1):    
     ret, frame = cap.read()
     
     cv2.imshow('orginal',frame)
     
     frame=convert_to_gray(frame)
     
     fr=fgbg3.apply(frame)
     
    
     cv2.imshow('CNT',fr)
     
     
     
     k = cv2.waitKey(30) & 0xff
     if k == 27:
         break
cap.release()
cv2.destroyAllWindows()

