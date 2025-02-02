import cv2
import numpy as np

img = cv2.imread("blank.png")
d1 = cv2.Sobel(img, cv2.CV_64F,1,0,ksize=5)
d2 = cv2.Sobel(img, cv2.CV_64F,0,1,ksize=5)
dst = cv2.add(d1,d2)

cv2.imshow("img",img)
cv2.imshow("d1",d1)
cv2.imshow('d2',d2)
cv2.imshow("merge",dst)
cv2.waitKey(0)