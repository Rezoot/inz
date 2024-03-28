import cv2


#zdjêcie po zdjeciu z buforem
def obraz():
    



    cap = cv2.VideoCapture(0)
    ret, frame1 = cap.read()    
    

    
    frame1=cv2.cvtColor(frame1, cv2.COLOR_BGR2GRAY)
    delay=0
    
    prog=20


    while(1):
        
        
        ret, frame2 = cap.read()

        
        
        frame2= cv2.cvtColor(frame2, cv2.COLOR_BGR2GRAY)
        
        #fr=frame2-frame1
        
        fr1=cv2.absdiff(frame2, frame1)
        

          
        _, fr1 = cv2.threshold(fr1, prog, 255, cv2.THRESH_BINARY)
        
        delay+=fr1
        delay[delay>prog]-=20
        delay[delay<=prog]=0
        
        #fr = cv2.medianBlur(fr, 3)
        
        
        c=delay
        fr1[c>prog]=255
        

                

        
        cv2.imshow('roznica zdjec z buforem',fr1)

        frame1=frame2


        k = cv2.waitKey(10) & 0xff
        if k == 27:
            break
    cap.release()
    cv2.destroyAllWindows()





