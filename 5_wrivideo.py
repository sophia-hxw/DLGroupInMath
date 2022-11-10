# 如何将视频数据录制成多媒体文件
"""
1、VideoWrite
参数一为输出文件
参数二为多媒体文件编码格式(VideoWrier_fourcc)
fourcc所用编码器，Windows系统采用DIVX编码器
参数三为帧率(一秒多少帧)
参数四为分辨率 (宽度，高度)
分辨率大小，要为摄像头/视频文件的实际分辨率
2、write
3、release
"""


import cv2

# 创建VideoWrite为写多媒体文件
fourcc = cv2.VideoWriter_fourcc(*'DIVX')
vw = cv2.VideoWriter('./opencv/out.avi',fourcc, 25, (720,1280))

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

    # 写数据到多媒体文件
    # vw.write(frame)
    if ret == False:
        break
    else:
        cv2.imshow('video', frame)
        vw.write(frame)


    #等待键盘事件，如果为q，退出
    key = cv2.waitKey(10)
    if key & 0xFF == ord('q'):
        break

# 释放VideoCapture
cap.release()

# 释放VideoWrite
vw.release()

cv2.destroyAllWindows()
