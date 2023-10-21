# Read Image or Video From File
import cv2 as cv

# Image!
img  = cv.imread('photos/derpCat.jpeg') 
cv.imshow("image", img)

# Videos!
capture = cv.VideoCapture('videos/catVid.mp4')

while True:
    isTrue, frame = capture.read()

    cv.imshow("Video", frame) # Program *crashes* when it runs out of frames to display!
    if cv.waitKey(20) & 0xFF==ord('d'):
        break 

capture.release()
cv.waitKey(0)
cv.destroyAllWindows()