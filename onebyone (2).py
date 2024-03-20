from turtle import width
import numpy as np 
import cv2
import os
import time
import threading


def przetwarzanie_kamery():
    def convert_to_gray(frame):
        gray = frame[:, :, 0] * 0.114 + frame[:, :, 1] * 0.587 + frame[:, :, 2] * 0.299
        return gray.astype('uint8')



    cap = cv2.VideoCapture(0)    
    ret, frame1 = cap.read()    
    

    
    frame1=convert_to_gray(frame1)
    delay=0
    
    t=0


    while(1):
        t+=1
        #cv2.waitKey(100)
        
        
        ret, frame2 = cap.read()

        cv2.imshow('orginal',frame2)
        
        frame2= cv2.cvtColor(frame2, cv2.COLOR_BGR2GRAY)
        
        #fr=frame2-frame1
        
        fr1=cv2.absdiff(frame2, frame1)
        

          
        _, fr1 = cv2.threshold(fr1, 30, 255, cv2.THRESH_BINARY)
        
        delay+=fr1
        delay[delay>30]-=20
        delay[delay<=30]=0
        print(delay)
        
        #fr = cv2.medianBlur(fr, 3)
        
        
        c=delay
        c[c>30]=55
        fr=fr1+c
        

                

        
        cv2.imshow('roznica',fr)

        frame1=frame2


        k = cv2.waitKey(10) & 0xff
        if k == 27:
            break
    cap.release()
    cv2.destroyAllWindows()





    

przetwarzanie_kamery()