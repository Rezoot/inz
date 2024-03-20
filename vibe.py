# -*- coding: utf-8 -*-
"""
Created on Sat Jul 18 17:43:58 2020

@author: curya
"""

# import numpy as np
import cv2
import time
from lib_vibe import vibe_gray
import funk

cap = cv2.VideoCapture(0)
vibe = vibe_gray()



ret, frame = cap.read()
#gray_frame = funk.convert_to_gray(frame)
frame=cv2.resize(frame,(500,350))

gray_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

vibe.AllocInit(gray_frame)


while True:
    ret, frame = cap.read()
    frame=cv2.resize(frame,(500,350))
    gray_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
   # gray_frame = funk.convert_to_gray(frame)
        
    
    
    segmentation_map = vibe.Segmentation(gray_frame)
    
    vibe.Update(gray_frame, segmentation_map)
   
    #segmentation_map= cv2.medianBlur(segmentation_map, 3)
    
    
    cv2.imshow('Actual Frame!', frame)  
    #cv2.imshow('Gray Frame!', gray_frame)
    cv2.imshow('Segmentation Frame!', segmentation_map)
    
    if cv2.waitKey(1) & 0xFF == ord('q'):                                 # Break while loop if video ends
        break


cap.release()
#cv2.waitKey()
cv2.destroyAllWindows()