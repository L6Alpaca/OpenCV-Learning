import cv2
import numpy as np


img = cv2.imread("ant.jpg", 0)

cv2.namedWindow("ant", cv2.WINDOW_KEEPRATIO)
cv2.imshow("ant", img)

# 图像二值化
thresh, dst = cv2.threshold(img, 127, 255, cv2.THRESH_BINARY)

# 设置窗口属性，并显示图片
cv2.namedWindow("dst", cv2.WINDOW_KEEPRATIO)
cv2.imshow("dst", dst)


cv2.waitKey(0)
