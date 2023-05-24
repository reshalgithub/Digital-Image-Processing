import cv2
import numpy as np

# Read image
img = cv2.imread('flw.jpg')
def flip_vertical(image):
    return cv2.flip(image, 0)
flipped_vertically = flip_vertical(img)

cv2.imshow("Original Image", img)
cv2.imshow("Vertically Flipped Image", flipped_vertically)

# Wait for a key press and close all windows
cv2.waitKey(0)
cv2.destroyAllWindows()