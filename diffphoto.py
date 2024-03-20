import cv2
import numpy as np


def convert_to_gray(frame):
# Oblicz wartość jasności pikseli przy użyciu odpowiednich wag dla każdego kanału
    gray = frame[:, :, 0] * 0.114 + frame[:, :, 1] * 0.587 + frame[:, :, 2] * 0.299
    return gray.astype('uint8')

# Wczytanie pierwszej klatki z sekwencji obrazów
cap = cv2.VideoCapture(0)
ret, frame = cap.read()


# Inicjalizacja modelu tła jako pierwszej klatki
background = convert_to_gray(frame)
#background = cv2.medianBlur(background, 5)

total_pixels = frame.shape[0] * frame.shape[1]




while(cap.isOpened()):
    
    ret, frame = cap.read()
    
    
    if not ret:
        break
    
    # Konwersja klatki na przestrzeń kolorów Grayscale
    gray_frame = convert_to_gray(frame)
    gray_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    # Obliczenie mediany dla każdego piksela jako modelu tła
    
    
    # Detekcja ruchu poprzez różnicę pomiędzy klatką a modelem tła
    diff =np.abs(gray_frame-background) 
    diff=cv2.absdiff(gray_frame, background)
    
    _, thresholded = cv2.threshold(diff, 25, 1, cv2.THRESH_BINARY)
    
    sum_diff=np.sum(thresholded)
 
    percent=sum_diff/total_pixels*100
    if percent>70:
        background = convert_to_gray(frame)
        #background = cv2.medianBlur(background, 5)
    
    _, thresholded = cv2.threshold(diff, 25, 255, cv2.THRESH_BINARY)
    
    # Wyświetlenie klatek
    cv2.imshow('Orginal', frame)
    cv2.imshow('tlo', background)
    cv2.imshow('diff', thresholded)
    
    
    
    k = cv2.waitKey(30) & 0xff
    if k == 27:
        break
    elif k==ord('b'):
            background = convert_to_gray(frame)
            #background = cv2.medianBlur(background, 5)
cap.release()
cv2.destroyAllWindows()
