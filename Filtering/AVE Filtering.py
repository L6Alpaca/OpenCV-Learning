#均值滤波
#方盒滤波 若正则化（Normalize = True） == 均值滤波
#即方盒最终 是否 除以（方盒尺寸）
import numpy as np
import cv2

img = cv2.imread("img.jpg")
cv2.imshow("img",img)
cv2.blur(img,(5,5))
#==cv2.boxFilter(img,-1,ksize=(5,5),normalize=True)
cv2.imshow("blur",img)
cv2.imwrite("blur.jpg",img)
cv2.waitKey(0)

# 它是指在图像上对目标像素给一个模板，该模板包括了其周围的临近像素（以目标像素为中心的周围8个像素，构成一个滤波模板，即去掉目标像素本身），
# 再用模板中的全体像素的平均值来代替原来像素值它是指在图像上对目标像素给一个模板，该模板包括了其周围的临近像素（以目标像素为中心的周围8个像素.
# 构成一个滤波模板，即去掉目标像素本身），再用模板中的全体像素的平均值来代替原来像素值
# 线性滤波