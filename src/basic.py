import cv2 as cv

img = cv.imread("Photos/derpCat.jpeg")
cv.imshow("Cat", img)

# Converting to grayscale
gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
cv.imshow("Grayscale", gray)

# Blur
blur = cv.GaussianBlur(img, (3, 3), cv.BORDER_DEFAULT)
cv.imshow("Blur", blur)

# Edge Cascade
canny = cv.Canny(img, 125, 175) # IF a reduction in found edges is necessary, pass in blur instead of img
cv.imshow("Edge Cascade", canny)

# Dilating the Image
dilated = cv.dilate(canny, (7, 7), iterations=1)
cv.imshow("Dilated", dilated)

# Eroding
eroded = cv.erode(dilated, (7, 7), iterations=1)
cv.imshow("Eroded", eroded)

# Resize
resized = cv.resize(img, (500, 500), interpolation=cv.INTER_AREA)
cv.imshow("Resized", resized)

# Cropping
cropped = img[50:200, 200:400]
cv.imshow('Cropped', cropped)

cv.waitKey(0)