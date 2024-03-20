from turtle import width
import numpy as np 
import cv2
import os
import time
import threading

def menu():
    print("|0| - wyjdz")
    print("|1| - kamerka")
    print("|2| - wybierz plik")


#def menu2():
#    print("1")
#    print("2")
#    print("3")
#    print("4")
#    print("0")
#    while(True):
#        try:
#            i=int(input("podaj opcje: "))
#        except :
#            print("brak takiej")
        


    

def przetwarzanie_kamery():


    cap = cv2.VideoCapture(0)    
   #fgbg3 = cv2.bgsegm.createBackgroundSubtractorCNT()
   #fgbg4 = cv2.bgsegm.createBackgroundSubtractorMOG()
    
    
    
    
    ret, frame1 = cap.read()    
    
    def convert_to_gray(frame):
    # Oblicz wartość jasności pikseli przy użyciu odpowiednich wag dla każdego kanału
        gray = frame[:, :, 0] * 0.114 + frame[:, :, 1] * 0.587 + frame[:, :, 2] * 0.299
        return gray.astype('uint8')
   
    frame1=convert_to_gray(frame1)
    
    
    while(1):

        #cv2.waitKey(50)
        
        ret, frame2 = cap.read()
        
        cv2.imshow('orginal',frame2)
        
        #frame2=convert_to_gray(frame2)
        frame2= cv2.cvtColor(frame2, cv2.COLOR_BGR2GRAY)
        
        #fr=frame2-frame1
        
        fr=cv2.absdiff(frame2, frame1)
        #for i in fr:
          #  print(i)
          
        _, fr = cv2.threshold(fr, 30, 255, cv2.THRESH_BINARY)
        #fr = cv2.medianBlur(fr, 3)
        
        
        

                
        #background = cv2.convertScaleAbs(frame2)
        
        cv2.imshow('roznica',fr)
        #cv2.imshow('mediana',background)
         
        #fgmask3 = fgbg3.apply(frame2) 
        #fgmask4 = fgbg4.apply(frame2) 
        
        frame1=frame2
        
        #cv2.imshow('medniana',fgmask2)
        #cv2.imshow('CNT',fgmask3)
        #cv2.imshow('MOG',fgmask4)

        k = cv2.waitKey(30) & 0xff
        if k == 27:
            break
    cap.release()
    cv2.destroyAllWindows()





#CNT (Counting-based Tracker): CNT jest oparty na zliczaniu pikseli, a tło jest aktualizowane tylko wtedy, gdy wystąpi pewna liczba zmian.
#różnica poprzednich pikseli
#Algorytmem detekcji ruchu opartym na medianie





przetwarzanie_kamery()