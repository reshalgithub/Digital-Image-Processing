import cv2
# Loading the image named test.jpg
img = cv2.imread("flw.jpg")
# Converting color mode to Grayscale as thresholding requires a single channeled image
img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
cv2.imshow('Image', img)

#Binary Thresholding
ret, thresh = cv2.threshold(img, 127, 255, cv2.THRESH_BINARY) 
cv2.imshow('Binary Threshold', thresh)

#Binary-Inverse Thresholding
ret, thresh = cv2.threshold(img, 127, 255, cv2.THRESH_BINARY_INV)
cv2.imshow('Binary Inverse Threshold', thresh)

#Truncate Thresholding
ret, thresh = cv2.threshold(img, 127, 255, cv2.THRESH_TRUNC)
cv2.imshow('Truncate Threshold', thresh)

#Zero Thresholding
ret, thresh = cv2.threshold(img, 127, 255, cv2.THRESH_TOZERO)
cv2.imshow('Truncate Threshold', thresh)

#Inverse Thresholding to Zero
ret, thresh = cv2.threshold(img, 127, 255, cv2.THRESH_TOZERO_INV)
cv2.imshow('Truncate Threshold', thresh)

cv2.waitKey(0)
cv2.destroyAllWindows
