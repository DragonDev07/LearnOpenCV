import cv2 as cv
import numpy as np

blank = np.zeros((500, 500, 3), dtype='uint8')
cv.imshow("Blank", blank)

# 1a. Paint the image a certain colour
blank[:] = 0, 255, 0
cv.imshow("#1a Fills", blank)

# 1b. Paint certain potion of image
blank[200:300, 300:400] = 0, 0, 255
cv.imshow("#1b Portions", blank)

# 2. Draw a Rectangle
cv.rectangle(blank, (0, 0), (250, 500), (255, 0, 0), thickness=cv.FILLED)
cv.imshow("#2 Rectangle", blank)

# 3. Draw a Circle
cv.circle(blank, (blank.shape[1]//2, blank.shape[0]//2), 40, (0, 0, 255), thickness=-1)
cv.imshow("#3 Circle", blank)

# 4. Draw a Line
cv.line(blank, (100, 250), (300, 400), (255, 255, 255), thickness=5)
cv.imshow("#4 Line", blank)

# 5. Write text
cv.putText(blank, "Hello World", (255, 255), cv.FONT_HERSHEY_COMPLEX, 1.0, (255, 255, 255), 2)
cv.imshow("#5 Text", blank)

cv.waitKey(0)