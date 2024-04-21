from asyncio.windows_events import NULL
import cv2
import numpy as np

#zdjêcie po zdjeciu z buforem
def obraz():
    
    ilepikseli = 5
    ilerazy = 2
    radius=3
    
    def dopelnienie():
            for i in range(h):
                a=np.where(fr1[i] == 255)[0] #x where white
                if a.any()!=NULL:
                    start=a[0]
                    stop=0
                    #fr1[i,start:stop]=255
                    for k in a[1:]:
                        d = k-start
                        if d>1 and d<ile:
                            fr1[i,start:k]=255
                        else:
                            start=k
        
    def dopasowaniepelne(fr1):

        

        def dopelnienie(dlugosc):
            for i in range(dlugosc):
                a=np.where(fr1[i] == 255)[0] #x where white
                if a.size > 0:
                    start=a[0]
                    stop=0
                    #fr1[i,start:stop]=255
                    for k in a[1:]:
                        d = k-start
                        if d>1 and d<=ilepikseli:
                            fr1[i,start:k]=255
                        else:
                            start=k



        def dopelnienie2(dlugosc):
            for i in range(dlugosc):
                # Find indices where fr1[i] equals 255
                a = np.where(fr1[i] == 255)[0]  # Get x-coordinates where white
        
                # Check if any pixels with value 255 are found
                if a.size > 0:
                    start = a[0]
            
                    # Iterate over the x-coordinates
                    for k in a[1:]:
                        d = k - start
                        if d > 1 and d <= ilepikseli:
                            # Set pixels to 255 within the specified range
                            fr1[i, start:k] = 255
                        start = k
     

        def pogrubienie():
            a=np.where(fr1 == 255) # where white
            if a[0].size>0:
                for i in range(a[0].size):
                    x1=np.clip(a[0][i]-radius, 0, h - 1)
                    x2=np.clip(a[0][i]+radius, 0, h - 1)
                    y1=np.clip(a[1][i]-radius, 0, w - 1)
                    y2=np.clip(a[1][i]+radius, 0, w - 1)
                    fr1[x1:x2,y1:y2]=255
                
                
       
   
            
            
           
       

        
        
    
        for x in range(ilerazy):
            pogrubienie()
            dopelnienie(h)
            fr1=np.transpose(fr1)
            dopelnienie(w) 
            fr1=np.transpose(fr1)
            

        return fr1
            


    cap = cv2.VideoCapture(0)
    ret, frame1 = cap.read()    
    

    
    frame1=cv2.cvtColor(frame1, cv2.COLOR_BGR2GRAY)
    delay=0
    
    h, w = frame1.shape[:2]
    mask=np.zeros((h,w))

    prog=25 #wykrycia
    odejmowanie = 10 #buforu

    j=0

    kernel_size = (15, 15)
    while(1):
        
        
        ret, frame2 = cap.read()

        frame3=frame2
        frame4=frame2
        
        frame2= cv2.cvtColor(frame2, cv2.COLOR_BGR2GRAY)
        
        #fr=frame2-frame1
        
        fr1=cv2.absdiff(frame2, frame1)
        

          
        _, fr1 = cv2.threshold(fr1, prog, 255, cv2.THRESH_BINARY)
        
        
            
        
        
        
      
          
        
         

        delay+=fr1
        delay[delay>prog]-=odejmowanie
        delay[delay<=prog]=0
        
       
       
        fr1[delay>prog]=255
        
        
        fr1=dopasowaniepelne(fr1)            
        
        
        
        
        
        
        
        #mask2=fr1[:]

        

        
        

        mask[fr1==0]=1
        mask[fr1==255]=0
        blurred_region = cv2.blur(frame3, (30, 30))  
        result = np.where(mask[..., None] != 0, blurred_region, frame3)
        
        
        
        frame4[fr1==0]=0

        cv2.imshow('roznica zdjec z buforem',fr1)
        cv2.imshow('wymazanie',frame4) 
        
        

        #cv2.imshow('rozem',blurred_region)
        
        
        
        cv2.imshow('blure',result)
        
        #cv2.imshow('dasd',obrot)
        

        frame1=frame2

        j+=1

        k = cv2.waitKey(10) 
        if k == 27:
            break
    cap.release()
    cv2.destroyAllWindows()





