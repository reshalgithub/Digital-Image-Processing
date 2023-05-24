
import cv2
#Read original color image
image = cv2.imread('flw.jpg')
cv2.imshow('Original', image)
cv2.waitKey(0)
#Convert to Grayscale
gray_image = cv2.cvtColor(image, cv2. COLOR_BGR2GRAY)
cv2.imshow('Grayscale', gray_image)
cv2.waitKey(0)

cv2.destroyAllWindows()
