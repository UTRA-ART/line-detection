import cv2
import numpy as np


image = cv2.imread("img_3.jpg")
gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
lower_yellow = np.array([20, 100, 100], dtype = "uint8")
upper_yellow = np.array([30, 255, 255], dtype="uint8")
img_hsv = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)
mask_yellow = cv2.inRange(img_hsv, lower_yellow, upper_yellow)
mask_white = cv2.inRange(gray_image, 200, 255)
mask_yw = cv2.bitwise_or(mask_white, mask_yellow)
mask_yw_image = cv2.bitwise_and(gray_image, mask_yw)
cv2.imshow('image', mask_yw_image)
cv2.waitKey(0)