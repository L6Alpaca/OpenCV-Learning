import cv2
import numpy as np

img = cv2.imread('../img.jpg')

dst = cv2.GaussianBlur(img, (5, 5), sigmaX=10)  #sigma(标准差)越大，越模糊
                                                      #未指定sigma时将会根据kernel长宽自动计算sigma

cv2.imshow('dst', dst)
cv2.imshow('img', img)
#cv2.imwrite("../dst.jpg", dst)
key = cv2.waitKey(0) & 0xff
if key == ord('q'):
    cv2.destroyAllWindows()

#由于高斯函数的性质，距离中心像素越远的像素对新值的贡献越小，对图像中的像素进行加权平均处理
#线性平滑滤波