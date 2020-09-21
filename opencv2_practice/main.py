import cv2
import numpy as np

image = cv2.imread("test.jpg", cv2.IMREAD_UNCHANGED)

cv2.imshow("test", image)