
import cv2
import numpy as np
	
img1 = cv2.imread('image1.jpg') 
img2 = cv2.imread('image2.jpg')
img1_resize=cv2.resize(img1, (300,300)) 
img2_resize=cv2.resize(img2, (300,300)) 

# cv2.addWeighted is applied over the
# image inputs with applied parameters
weightedSum = cv2.addWeighted(img1_resize, 0.5, img2_resize, 0.4, 0)

# the window showing output image
cv2.imshow('Weighted Image', weightedSum)
# De-allocate any associated memory usage
if cv2.waitKey(0) & 0xff == 27:
	cv2.destroyAllWindows()
