import cv2 as cv

img = cv.imread('Photos/cat.jpg')
cv.imshow('Cat', img)

# converting to grayscale

gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
cv.imshow('gray!!', gray)

# Blur
blur = cv.GaussianBlur(img, (7,7), cv.BORDER_DEFAULT) # higher (int, int) result in more blur
cv.imshow('blur', blur)

# Edge detect
canny = cv.Canny(blur, 125, 175)
cv.imshow('canny', canny)

# Dilating the imagae
# enhance the edges
dilated = cv.dilate(canny, (7,7), iterations = 5)
cv.imshow('Dillated', dilated)

# Eroding
# ATTEMPT TO get back the edge canny from dilated
eroded = cv.erode(dilated, (7,7), iterations = 5)
cv.imshow('eroded', eroded)

# resize
resized = cv.resize(img, (500, 500), interpolation=cv.INTER_CUBIC) #Inter_cubic result in higher resolution but slower or use INTER_AERA
cv.imshow('Resized', resized)

# Cropping
cropped = img[50:100, 100:400]
cv.imshow('Cropped', cropped)

cv.waitKey(0);