import cv2 as cv
import numpy as np

blank = np.zeros((500, 500, 3), dtype = 'uint8') # (width, height, color channel)  datatype of img
cv.imshow('Blank', blank)

# 1. Paint the image a certain colour
blank[420:450, 400:450] = 0, 255, 0 # b g r
cv.imshow('Green', blank)

# 2. Draw a Rectangle

cv.rectangle(blank, (0, 0), (blank.shape[1]//2, blank.shape[0]//2), (0, 255, 0), thickness=cv.FILLED)
cv.imshow('Rectangle', blank)

# 3. Draw  a circle

cv.circle(blank, (blank.shape[1]//4, blank.shape[0]//4), 20, (255, 0, 0), thickness=3)
cv.imshow('Circle', blank)

# 4. draw a line

cv.line(blank, (100, 250), (300, 400), (255, 255, 255), thickness=3) #pt1 to pt2
cv.imshow('line', blank)

# 5.Write text
cv.putText(blank, 'Hello', (200, 300), cv.FONT_HERSHEY_TRIPLEX, 1.0, (0,255,0), 2)
cv.imshow('text', blank)

cv.waitKey(0)