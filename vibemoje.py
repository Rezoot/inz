# -*- coding: utf-8 -*-
"""
Created on Fri Mar 15 12:26:09 2024

@author: Woofel
"""

import cv2
import time
import funk

cap=cv2.VideoCapture(0)


numberOfSamples = 20
matchingThreshold = 20
matchingNumber = 2
updateFactor = 16

# Storage for the history
historyImage = None
historyBuffer = None
lastHistoryImageSwapped = 0
numberOfHistoryImages = 2

# Buffers with random values
jump = None
neighbor = None
position = None

frame_index = 0
segmentation_time = 0
update_time = 0



ret,frame=cap.read()
gray_frame=funk.convert_to_gray(frame)

height, width = image.shape[:2]



while True:
    ret,frame=cap.read()
    if not ret:
        break
    gray_frame=funk.convert_to_gray(frame)
    