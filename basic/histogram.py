import cv2 as cv
import matplotlib.pyplot as plt
import numpy as np

# img = cv.imread('Photos/cats.jpg')
# cv.imshow('Cats', img)

# blank = np.zeros(img.shape[:2], dtype = "uint8")

# circle = cv.circle(blank, (img.shape[1]//4+300, img.shape[0]//4+100), 100, 255, -1)

# gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
# cv.imshow('Gray', gray)

# mask = cv.bitwise_and(gray, gray, mask = circle)
# cv.imshow('mask', mask)

# GRayscale histogram
# gray_hist = cv.calcHist([gray], [0], mask, [256], [0, 256])

# plt.figure()
# plt.title('Grayscale histogram')
# plt.xlabel('Bin')
# plt.ylabel('# of pixels')
# plt.plot(gray_hist)
# plt.xlim([0, 256])
# plt.show()

# Color histogram

img = cv.imread('Photos/cats.jpg')
cv.imshow('Cats', img)

blank = np.zeros(img.shape[:2], dtype = "uint8")

#for computer to use
mask = cv.circle(blank, (img.shape[1]//4+300, img.shape[0]//4+100), 100, 255, -1)

#for us to see the masked area
masked = cv.bitwise_and(img, img, mask = mask)
cv.imshow('mask', masked)

plt.figure()
plt.title('Colorscale histogram')
plt.xlabel('Bin')
plt.ylabel('# of pixels')
colors = ('b', 'g', 'r')
for i,col in enumerate(colors):
    hist = cv.calcHist([img], [i], mask, [256], [0,256])
    plt.plot(hist, color = col)
    plt.xlim([0,256])


plt.show()


cv.waitKey(0)