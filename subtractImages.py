import cv2 
import numpy as np 
    
# path to input images are specified and  
# images are loaded with imread command 
img1 = cv2.imread('image1.jpg') 
img2 = cv2.imread('image2.jpg')
img1_resize=cv2.resize(img1, (300,300)) 
img2_resize=cv2.resize(img2, (300,300)) 

# cv2.subtract is applied over the
# image inputs with applied parameters
sub = cv2.subtract(img1_resize, img2_resize)
  
# the window showing output image
# with the subtracted image 
cv2.imshow('Subtracted Image', sub)
  
# De-allocate any associated memory usage  
if cv2.waitKey(0) & 0xff == 27: 
    cv2.destroyAllWindows() 