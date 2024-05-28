import cv2 as cv

img = cv.imread('Photos/cats.jpg')
cv.imshow('Cat', img)

# sometimes the image will have so many noises so you want to reduce the effect by bluring the img

# FIRST METHOD OF BLURING 
# AVERAGING
average = cv.blur(img, (3,3)) #higher the int more blur it is basically setting the size of matrix
cv.imshow('Average blur', average)


# Gaussian Blur (more natural blur)
gauss = cv.GaussianBlur(img, (3,3), 0)
cv.imshow('Gaussian blur', gauss)

# Median blur (more effective to reduce noise oftern use in advance machien learning)
median = cv.medianBlur(img, 3)
cv.imshow('Median Blur', median)

# Bilateral bluring (most effecctive reduec noise to blur) apply bluring and also keep edge

bilateral = cv.bilateralFilter(img, 10, 35, 35) # larger alpha more color in the neighbourhood to be consider
cv.imshow('bilateral', bilateral)

cv.waitKey(0)