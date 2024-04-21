import math
import cv2
import numpy as np

def obraz():
    #sta³e
    segama=30
    e=math.e
    pi=math.pi
    numFrame=10
    numInitial=1
    numMRF=4
    num_write=500
    threshhold=0.65


    
    
    

    cap = cv2.VideoCapture(0)
    alpha = 0.05
    std_init = 20 
    var_init = std_init*std_init
    lamda = 2.5 * 1.2


    


    pixel = [0, 0, 0]
    pixel_u = [0, 0, 0]
    pixel_var = [0, 0, 0]
    pixel_std = [0, 0, 0]
    pixel_for = [255, 0, 0]
    pixel_back = [0, 0, 0]

    a=100
    b=100
    ret, frame = cap.read()
    frame = cv2.resize(frame,(200, 200)) 
    h, w = frame.shape[:2]


    frame_u = np.zeros((h, w, 3), dtype=np.uint8)
    frame_var = np.zeros((h, w, 3), dtype=np.uint8)
    frame_std = np.zeros((h, w, 3), dtype=np.uint8)
    frame_diff = np.zeros((h, w, 3), dtype=np.uint8)
    frame_bin = np.zeros((h, w), dtype=np.uint8)
    

    for y in range(h):
        for x in range(w):
            pixel=frame[y,x]
            
            pixel_u=pixel

            pixel_std[0] = std_init
            pixel_std[1] = std_init
            pixel_std[2] = std_init
            
            
            
            frame_u[y,x]=pixel_u
            frame_var[y,x]=pixel_var
            frame_std[y,x]=pixel_std


    num=0

    while(1):

        ret, frame = cap.read()
        frame = cv2.resize(frame,(200, 200)) 

        for y in range(h):
            for x in range(w):
                
                pixel = frame[y,x]
                pixel_u = frame_u[y,x]
                pixel_std = frame_std[y,x]
                pixel_var = frame_var[y,x]
                
                a=np.abs(pixel,pixel_u)

                if (a[0] < lamda * pixel_std[0]) and (a[1] < lamda * pixel_std[1]) and (a[2] < lamda * pixel_std[2]) :
                    pixel_u=(1-alpha) * pixel_u + alpha * pixel
                    pixel_var = (1-alpha) * pixel_var +  (pixel-pixel_u) * (pixel-pixel_u) #niewiadomo czy ta druga alpha
                    pixel_std[0]=math.sqrt(pixel_var[0])
                    pixel_std[1]=math.sqrt(pixel_var[1])
                    pixel_std[2]=math.sqrt(pixel_var[2])

                    frame_u[y,x]=pixel_u
                    frame_var[y,x]=pixel_var
                    frame_std[y,x]=pixel_u

        frame_diff=cv2.absdiff(frame_u,frame)
        
        for y  in range(h):
            for x in range(x):
                #print(frame_diff[y,x])
                if all(frame_diff[y, x][i] > 20 for i in range(3)):
                    frame_bin[y,x]=255
                    
         
                else:
                    frame_bin[y,x]=0
                    
        
        cv2.imshow("origin", frame);
        cv2.imshow("processing", frame_u);
        cv2.imshow("result", frame_bin);


        k = cv2.waitKey(30) & 0xff
        if k == 27:
             break
    cap.release()
    cv2.destroyAllWindows()