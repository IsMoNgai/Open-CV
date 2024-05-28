import cv2 as cv

def rescaleFrame(frame, scale=0.2):
    #images, videos and live videos
    width = int(frame.shape[1] * scale)
    height = int(frame.shape[0] * scale)
    dimensions = (width, height)

    return cv.resize(frame, dimensions, interpolation=cv.INTER_AREA)

def changeRes(width, height):
    # only work for live videos
    capture.set(3, width)
    capture.set(4, height)


capture = cv.VideoCapture('Videos/dog.mp4')

# while True:
#     isTrue, frame = capture.read()

#     frame_resized = rescaleFrame(frame)

#     cv.imshow('Before Rescale', frame)
#     cv.imshow('Resized', frame_resized)

#     if cv.waitKey(20) & 0xFF == ord('d'):
#         break

# capture.release()
# cv.destroyAllWindows()

# ---- img -----

img = cv.imread('Photos/cat_large.jpg')
cv.imshow('Before resized Cat', img)
cv.imshow('resized Cat', rescaleFrame(img))

cv.waitKey(0);