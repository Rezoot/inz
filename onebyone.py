import cv2

def org():
    cap2 = cv2.VideoCapture(0)
    while(1):
        
        ret, frame1 = cap2.read()    
        cv2.imshow('orginal',frame1)
        k = cv2.waitKey(30) & 0xff
        if k == 27:
            break
    cap2.release()
    cv2.destroyAllWindows()


def obraz():
    cap = cv2.VideoCapture(0)
    ret, frame1 = cap.read()    
    
    
   
    frame1=cv2.cvtColor(frame1, cv2.COLOR_BGR2GRAY)
    
   
    while(1):
       
      
        
        ret, frame2 = cap.read()
        
        
        

        frame2= cv2.cvtColor(frame2, cv2.COLOR_BGR2GRAY)
        
        
        
        fr=cv2.absdiff(frame2, frame1)

          
        _, fr = cv2.threshold(fr, 20, 255, cv2.THRESH_BINARY)
        
 
        
        cv2.imshow('roznica zdjec 1',fr)

        frame1=frame2


        k = cv2.waitKey(30) & 0xff
        if k == 27:
            break
    cap.release()
    cv2.destroyAllWindows()



