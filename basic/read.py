import cv2 as cv

# img = cv.imread('Photos/cat_large.jpg') #image is too large 

# cv.imshow('Cat', img) #name of window and img to display;

# reading videos

capture = cv.VideoCapture('Videos/dog.mp4') #file name with '' and if u want camera then do 0, 1, 2, 3

while True:
    isTrue, frame = capture.read() #isTrue = success? frame is output

    cv.imshow('Video', frame) #display each frame

    if cv.waitKey(20) & 0xFF == ord('d'): #if letter d is press break out loop
        break

capture.release()
cv.waitKey(0) #wait infinitely until key pressed