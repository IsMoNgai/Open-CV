#boundary of object
#is not edges

import cv2 as cv

import numpy as np

img = cv.imread('Photos/cats.jpg')

cv.imshow('CAT', img)

blank = np.zeros(img.shape, dtype='uint8')
cv.imshow('blank', blank)

gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
cv.imshow('gray', gray)

blur = cv.GaussianBlur(gray, (5,5), cv.BORDER_DEFAULT)
cv.imshow('Blur', blur)

canny = cv.Canny(blur, 125, 175) 
cv.imshow('canny', canny)

# rather than using canny we ccan use threshold

# use canny first and then use contours. Is better that way than using threshold

ret, thresh = cv.threshold(gray, 125, 255, cv.THRESH_BINARY) # if below 125 set to black and above 255 set to white (convert it to 0 or 1)
cv.imshow('THresh', thresh)

contours, hierarchies = cv.findContours(thresh, cv.RETR_LIST, cv.CHAIN_APPROX_SIMPLE) #hierarchies used to find the layors REtERLIST list out all RETERTREE will 
print(f'{len(contours)} contours found')

cv.drawContours(blank, contours, -1, (0,0,255, 2), 1)
cv.imshow('Contours draw', blank)

cv.waitKey(0)