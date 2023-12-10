import cv2
import numpy as np

cap = cv2.VideoCapture(0)

while True:
    ret, frame = cap.read()
    width = int(cap.get(3))
    height = int(cap.get(4))

    # Will detect in range between these two colors
    lower_blue = np.array([0, 0, 0])
    upper_blue = np.array([255, 255, 255])

    # Different Conversions
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
    mask = cv2.inRange(hsv, lower_blue, upper_blue)
    result = cv2.bitwise_and(frame, frame, mask=mask)

    # Put into one image
    image = np.zeros(frame.shape, np.uint8)
    smaller_mask = cv2.resize(mask, (0, 0), fx=0.5, fy=0.5)
    smaller_mask = np.expand_dims(smaller_mask, axis=2)
    smaller_hsv = cv2.resize(hsv, (0, 0), fx=0.5, fy=0.5)
    smaller_frame = cv2.resize(frame, (0, 0), fx=0.5, fy=0.5)
    smaller_result = cv2.resize(result, (0, 0), fx=0.5, fy=0.5)

    image[0:height//2, 0:width//2] = smaller_frame # Top Left Quadrant
    image[height//2:, 0:width//2] = smaller_hsv # Bottom Left Quadrant
    image[0:height//2, width//2:] = smaller_mask # Top Right Quadrant
    image[height//2:, width//2:] = smaller_result # Bottom Right Quadrant

    cv2.imshow('Color Detection', image)
    
    if cv2.waitKey(1) == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()