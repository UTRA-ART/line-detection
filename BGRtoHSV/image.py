import cv2
import numpy as np

img = cv2.imread('img_3.jpg',1)
hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
lower_range = np.array([31, 100, 100], dtype=np.uint8)
upper_range = np.array([51, 255, 255], dtype=np.uint8)


mask = cv2.inRange(hsv, lower_range, upper_range)

cv2.imshow('mask',mask)
cv2.imshow('image', img)

while(1):
  k = cv2.waitKey(0)
  if(k == 27):
    break

cv2.destroyAllWindows()

