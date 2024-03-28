import cv2
import numpy as np



def obraz():
    cap = cv2.VideoCapture(0)
    # Wczytanie pierwszej klatki z sekwencji obrazów
    ret, frame = cap.read()


    # Inicjalizacja modelu tła jako pierwszej klatki
    background = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    #background = cv2.medianBlur(background, 5)

    total_pixels = frame.shape[0] * frame.shape[1]


    while(cap.isOpened()):
    
        ret, frame = cap.read()
    
        
        if not ret:
            break
    
        # Konwersja klatki na przestrzeń kolorów Grayscale
        #gray_frame = convert_to_gray(frame)

        gray_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        # Obliczenie mediany dla każdego piksela jako modelu tła
    
    
        # Detekcja ruchu poprzez różnicę pomiędzy klatką a modelem tła
        diff =np.abs(gray_frame-background) 
        diff=cv2.absdiff(gray_frame, background)
    
        _, thresholded = cv2.threshold(diff, 30, 1, cv2.THRESH_BINARY)
    
        sum_diff=np.sum(thresholded)
 
        percent=sum_diff/total_pixels*100
        if percent>50:
            background = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
            #background = cv2.medianBlur(background, 5)
    
        _, thresholded = cv2.threshold(diff, 30, 255, cv2.THRESH_BINARY)
    
        # Wyświetlenie klatek
        #cv2.imshow('Orginal', frame)
        cv2.imshow('orginal',frame)
        cv2.imshow('Tlo', background)
        cv2.imshow('roznica z tlem', thresholded)
    
    
    
        k = cv2.waitKey(30) & 0xff
        if k == 27:
            break
        elif k==ord('b'):
                background = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
                #background = cv2.medianBlur(background, 5)
    cap.release()
    cv2.destroyAllWindows()


