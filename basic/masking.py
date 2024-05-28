import cv2 as cv
import numpy as np

img = cv.imread('Photos/cats.jpg')
cv.imshow('Cats', img)

# only focus on faces??

blank = np.zeros(img.shape[:2], dtype='uint8')
cv.imshow('Blank img', blank)

mask = cv.circle(blank.copy(), (img.shape[1]//2, img.shape[0]//2), 100, 255, -1)
mask2 = cv.circle(blank, (img.shape[1]//2 + 90, img.shape[0]//2), 100, 255, -1)
cv.imshow('Mask', mask)
cv.imshow('Mask2', mask2)

masked = cv.bitwise_and(img, img, mask=mask)
cv.imshow('Masked img', masked)
masked2 = cv.bitwise_and(img, img, mask=mask2)
cv.imshow('Masked img2', masked2)


cv.waitKey(0)