# 如何利用opencv从摄像头采集视频
"""
1、VideoCapture()  需要有摄像头
参数0表示默认为笔记本的内置第一个摄像头，
如果需要读取已有的视频则参数改为视频所在路径路径，
例如：cap=cv2.VideoCapture('video.mp4')

2、cap.read()
返回两个值，第一个为状态值，读到帧为true
如果文件读取到结尾，它的返回值就为False
第二个值为视频帧frame。电影动画片为一秒24帧
frame为每一帧的图像，这里图像是三维矩阵

3、imshow()

4、cap.release() 释放资源
ap.release的功能是关闭视频文件或者摄像头，并释放对象。
在操作完成之后需要释放，否则其他程序无法再次获取摄像头或者视频文件。
"""
import cv2

# 创建窗口
cv2.namedWindow('video', cv2.WINDOW_AUTOSIZE)

# 从视频设备/视频文件中读取视频帧
cap = cv2.VideoCapture('./opencv/capvideo.mp4')  # 0

while True:  # 因为是一帧一帧地读取视频，故用循环
    # 从摄像头读视频帧
    ret, frame = cap.read()
    # print(ret)

    # 将视频帧在窗口中显示
    # cv2.imshow('video', frame) # 如果从摄像头中获取视频这一行即可
    if ret == False:
        break
    else:
        cv2.imshow('video', frame)

    #等待键盘事件，如果为q，退出
    key = cv2.waitKey(10)
    if key & 0xFF == ord('q'):
        break

# 释放VideoCapture
cap.release()
cv2.destroyAllWindows()
