'''
import cv2

capture = cv2.VideoCapture(0, cv2.CAP_DSHOW)  # 打开笔记本内置摄像头
fourcc = cv2.VideoWriter_fourcc('X', 'V', 'I', 'D')  # 确定视频被保存后的编码格式
output = cv2.VideoWriter("output.avi", fourcc, 20, (640, 480))  # 创建VideoWriter类对象 20指fps

fps = 20
frame_Num = fps * 10 #10秒钟需要记录的帧数
while (capture.isOpened() and frame_Num >= 0):  # 笔记本内置摄像头被打开后
    retval, frame = capture.read()  # 从摄像头中实时读取视频
    if retval == True:  # 读取到摄像头视频后
        output.write(frame)  # 在VideoWriter类对象中写入读取到的帧
        cv2.imshow("frame", frame)  # 在窗口中显示摄像头视频
    key = cv2.waitKey(1)  # 窗口的图像刷新时间为1毫秒
    frame_Num -= 1 #通过这个记录十秒的视频
    if key == 27:  # 如果按下Esc键
        break
capture.release()  # 关闭笔记本内置摄像头
output.release()  # 释放VideoWriter类对象
cv2.destroyAllWindows()  # 销毁显示摄像头视频的窗口
'''
#以上 保存摄像头记录的视频
#一下 保存视频文件——转格式，定时长
import cv2

video = cv2.VideoCapture("公司宣传.avi")  # 打开视频文件
fps = video.get(cv2.CAP_PROP_FPS)  # 获取视频文件的帧速率——VideoWriter所需参数
# 获取视频文件的帧大小
size = (int(video.get(cv2.CAP_PROP_FRAME_WIDTH)),
        int(video.get(cv2.CAP_PROP_FRAME_HEIGHT)))
fourcc = cv2.VideoWriter_fourcc('X', 'V', 'I', 'D')  # 确定视频被保存后的编码格式
output = cv2.VideoWriter("ten_Seconds.avi", fourcc, fps, size)  # 创建VideoWriter类对象
frame_Num = 10 * fps  # 视频文件的前10秒视频含有的帧数
# 视频文件被打开后且视频文件的前10秒视频含有的帧数大于0
while (video.isOpened() and frame_Num > 0):
    retval, frame = video.read()  # 读取视频文件
    if retval == True:  # 读取到视频文件后
        output.write(frame)  # 在VideoWriter类对象中写入读取到的帧
    frame_Num -= 1  # 视频文件的前10秒视频含有的帧数减少一帧
# 控制台输出提示信息
print("公司宣传.avi的前10s视频已经保存为PyCharm当前项目路径下的ten_Seconds.avi。")
video.release()  # 关闭视频文件
output.release()  # 释放VideoWriter类对象

