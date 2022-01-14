import cv2, numpy as np
img = cv2.imread("Resources/lena.png")
kernel = np.ones((5, 5), np.uint8)

# To turn image to Gray Scale
imgGray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
# To blur the image
imgBlur = cv2.GaussianBlur(imgGray, (7, 7), 0)
# Edge Detector
imgCanny = cv2.Canny(img, 100, 100)
imgDilation = cv2.dilate(imgCanny, kernel, iterations=1)
imgEroded = cv2.erode(imgDilation, kernel, iterations=1)

# cv2.imshow("Gray Image", imgGray)
# cv2.imshow("Blur Image", imgBlur)
# cv2.imshow("Canny Image", imgCanny)
# cv2.imshow("Dilation Image", imgDilation)
cv2.imshow("Eroded Image", imgEroded)
cv2.waitKey(0)
