import cv2
import numpy as np

cap = cv2.VideoCapture(0)

while True:
    ret, frame = cap.read()
    width = int(cap.get(3))
    height = int(cap.get(4))

    image = np.zeros(frame.shape, np.uint8)
    smaller_frame = cv2.resize(frame, (0, 0), fx=0.5, fy=0.5)
    
    image[:height//2, :width//2] = smaller_frame # Top Left Quadrant
    image[height//2:, :width//2] = smaller_frame # Bottom Left Quadrant
    image[:height//2, width//2:] = smaller_frame # Top Right Quadrant
    image[height//2:, width//2:] = smaller_frame # Bottom Right Quadrant

    outline = cv2.Canny(image, 100, 175)

    cv2.imshow('frames', frame)
    cv2.imshow('Tiled View', image)
    cv2.imshow('Outline', outline)

    if cv2.waitKey(1) == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()