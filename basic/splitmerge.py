import cv2 as cv
import numpy as np

img = cv.imread('Photos/park.jpg')
cv.imshow('park', img)

blank = np.zeros(img.shape[:2], dtype='uint8')

b,g,r = cv.split(img)

blue = cv.merge([b, blank, blank])
green = cv.merge([blank, g, blank])
red = cv.merge([blank, blank, r])

blue_green = cv.merge([b, g, blank])

cv.imshow('B', blue)
cv.imshow('g', green)
cv.imshow('r', red)

cv.imshow('b_g', blue_green)

# if more white shown means more that color on that pixel

print(img.shape)
print(b.shape)
print(g.shape)
print(r.shape)

merged = cv.merge([b,g,r])
cv.imshow('merged', merged)

cv.waitKey(0)