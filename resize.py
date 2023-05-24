import cv2
image = cv2.imread('flw.jpg')
cv2.imshow('Original', image)
cv2.waitKey(0)
#Resizing image
resize_image = cv2.resize(image, (500,500))

cv2.imshow('Resized Image', resize_image)
cv2.waitKey(0)

cv2.destroyAllWindows()