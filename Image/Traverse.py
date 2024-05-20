"""
彩色图像的遍历
    1)把第一个通道里面的颜色信息全部变为了0
"""

import cv2


def main():
    img = cv2.imread("ant.jpg")

    # 设置窗口属性，并显示图片
    cv2.namedWindow("Ant", cv2.WINDOW_KEEPRATIO)
   # cv2.imshow("Ant", img)

    # 得到图片的宽高、和维度
    height, width, n = img.shape
    # 拷贝一个图片
    img2 = img.copy()
    for i in range(height):
        for j in range(width):
            # 将第一个通道内的元素重新赋值 [0]表示第1个通道 一共3通道
            img2[i, j][0] = 0
    print(img2[1])
    # 设置窗口属性，并显示图片
    cv2.namedWindow("img2", cv2.WINDOW_KEEPRATIO)
   # cv2.imshow("img2", img2)

    cv2.waitKey(0)


if __name__ == '__main__':
    main()