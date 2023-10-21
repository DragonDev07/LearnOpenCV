# Resize & Rescale images and videos
import cv2 as cv

# This method will work for Images, Videos and Live Video
def rescaleFrame(frame, scale=0.75):
    height = int(frame.shape[0] * scale)
    width = int(frame.shape[1] * scale)
    dimensions = (width, height)
    
    return cv.resize(frame, dimensions, interpolation=cv.INTER_AREA)

# This method will only work for Live Video
def changeRes(width, height):
    capture.set(3,width)
    capture.set(4,height)

# Display Resized Images!
img = cv.imread("photos/cat-large.png")
resized_img = rescaleFrame(img, scale=0.25)

cv.imshow("Image", img)
cv.imshow("Resized Image", resized_img)

# Display Resized Videos!
capture = cv.VideoCapture('videos/catVid.mp4')

while True:
    isTrue, frame = capture.read()

    frame_resized = rescaleFrame(frame, scale=0.25)

    cv.imshow("Video", frame) # Program *crashes* when it runs out of frames to display!
    cv.imshow("Resized Video", frame_resized)

    if cv.waitKey(20) & 0xFF==ord('d'):
        break 

capture.release()
cv.waitKey(0)
cv.destroyAllWindows()