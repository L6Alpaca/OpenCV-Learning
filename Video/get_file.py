import cv2

video = cv2.VideoCapture("output.avi")  # 打开视频文件

while (video.isOpened()):  # 视频文件被打开后
    retval, image = video.read()  # 读取视频文件
    # 设置“Video”窗口的宽为420，高为300
    cv2.namedWindow("Video", 0)
    cv2.resizeWindow("Video", 420, 300)
    if retval == True:  # 读取到视频文件后
        #img_Gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY) #可转换为灰度图
        cv2.imshow("Video", image)  # 在窗口中显示读取到的视频文件
    else:  # 没有读取到视频文件
        break
    key = cv2.waitKey(20)  # 窗口的图像刷新时间为1毫秒
    if key == 32:   # 如果按下空格键
        cv2.waitKey(0)  # 不刷新图像，实现暂停效果
        continue    # 再按一次空格键，继续播放
    if key == 27:  # 如果按下Esc键
        break
video.release()  # 关闭视频文件
cv2.destroyAllWindows()  # 销毁显示视频文件的窗口

#获得视频相关信息——不可和播放同时进行
'''
fps = video.get(cv2.CAP_PROP_FPS)  # 获取视频文件的帧速率
frame_Count = video.get(cv2.CAP_PROP_FRAME_COUNT)  # 获取视频文件的帧数
frame_Width = int(video.get(cv2.CAP_PROP_FRAME_WIDTH))  # 获取视频文件的帧宽度
frame_Height = int(video.get(cv2.CAP_PROP_FRAME_HEIGHT))  # 获取视频文件的帧高度

# 输出获取到的属性值
print("帧速率:", fps)
print("帧数:", frame_Count)
print("帧宽度:", frame_Width)
print("帧高度:", frame_Height)
'''