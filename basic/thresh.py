import cv2 as cv

img = cv.imread('Photos/cats.jpg')
cv.imshow('Cat', img)

gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
cv.imshow('Gray', gray)

# simple thresholding
threshold, thresh = cv.threshold(gray, 150, 255, cv.THRESH_BINARY) # thresh the img that being outputed

cv.imshow('Simple threshold', thresh)

threshold, thresh_inv = cv.threshold(gray, 150, 255, cv.THRESH_BINARY_INV)

cv.imshow('Simple threshold_inv', thresh_inv) # basically inverse

#Adaptive threshold
adaptive_thresh = cv.adaptiveThreshold(gray, 255, cv.ADAPTIVE_THRESH_GAUSSIAN_C, cv.THRESH_BINARY, 13, 3) # use GaUSSIAN OR MEAN
cv.imshow('Adaptive threshold', adaptive_thresh)

cv.waitKey(0)