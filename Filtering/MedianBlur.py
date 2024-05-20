import numpy as np
import cv2

img = cv2.imread("salt.png")
cv2.imshow("img",img)
img = cv2.medianBlur(img,7)
cv2.imshow("BLUR",img)
cv2.waitKey(0)
cv2.destroyAllWindows()

#中值滤波的原理:假设有一个数组[1,5,5,6,7,8,9]，取中间值(即中位数)作为卷积后的结果即可.中值滤波对胡椒噪音(也叫椒盐噪音)效果明显
#在一块区域中取中值，去除了椒盐点这样的极端值，让周围的像素值接近真实的值从而消除孤立的噪声点。
#非线性滤波