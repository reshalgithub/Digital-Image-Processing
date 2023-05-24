import cv2
import numpy as np

# Read image
img = cv2.imread('flw.jpg')

# Function to flip image horizontally
def flip_horizontal(image):
    return cv2.flip(image, 1)
flipped_horizontally = flip_horizontal(img)
cv2.imshow("Original Image", img)
cv2.imshow("Horizontally Flipped Image", flipped_horizontally)

# Wait for a key press and close all windows
cv2.waitKey(0)
cv2.destroyAllWindows()