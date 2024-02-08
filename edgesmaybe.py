import numpy as np
import cv2

cap = cv2.VideoCapture(0)

while True:
    # Capture frame-by-frame
    ret, frame = cap.read()

    # Width and Height of the frame
    width = int(cap.get(3))
    height = int(cap.get(4))

    # Create a blank image
    image = np.zeros(frame.shape, np.uint8)

    # Comvert the frame to grayscale
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # Convert to HSV
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

    # Detect the edges
    edges = cv2.Canny(gray, 100, 200)

    # Resize all frames to half of the main image's dimensions
    frame = cv2.resize(frame, (width//2, height//2))
    gray = cv2.resize(gray, (width//2, height//2))
    hsv = cv2.resize(hsv, (width//2, height//2))
    edges = cv2.resize(edges, (width//2, height//2))

    # Place images in a grid
    image[:height//2, :width//2] = frame
    image[height//2:, :width//2] = gray
    image[:height//2, width//2:] = hsv
    image[height//2:, width//2:] = edges

    # Display the resulting frame
    cv2.imshow('frame', image)

    if cv2.waitKey(1) == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
