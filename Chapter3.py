import cv2
import numpy as np

# How to resize an Image
img = cv2.imread("Resources/lambo.png")
# cv2.imshow("Image", img)
print(img.shape)
imgResize = cv2.resize(img, (300, 200))
# cv2.imshow("Resized Image", imgResize)
# How to crop an image
imgCropped = img[0:200, 0:500]
cv2.imshow("Cropped Image", imgCropped)
cv2.waitKey(0)
