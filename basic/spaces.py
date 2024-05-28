import cv2 as cv
import matplotlib.pyplot as plt

img = cv.imread('Photos/park.jpg')
#img got read here is bgr image and opencv translate bgr image
cv.imshow('park', img)

# #since our image is bgr and plt show rgb img so it looks diff
# plt.imshow(img)
# plt.show()

# what we can do is to convert bgr to rgb and use plt again then it will show normal image example below

gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
cv.imshow('gray', gray)

# BGR to HSV image

hsv = cv.cvtColor(img, cv.COLOR_BGR2HSV)
cv.imshow('hsv', hsv)

# BGR to Lab

lab = cv.cvtColor(img, cv.COLOR_BGR2LAB)
cv.imshow('lab', lab)

#opencv read bgr but we use rgb to do that
rgb = cv.cvtColor(img, cv.COLOR_BGR2RGB)
cv.imshow('rgb', rgb)

plt.imshow(rgb)
plt.show()

#convert hsv to BGR
hsv_bgr = cv.cvtColor(lab, cv.COLOR_LAB2BGR)
cv.imshow('HSV --> BGR', hsv_bgr)

# however there is no conversion from grey scale to lab u need to convert gray to bgr and bgr to lab

cv.waitKey(0)