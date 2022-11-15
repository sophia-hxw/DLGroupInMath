# 如何将视频数据录制成多媒体文件

'''
优化：
显示窗口为什么变大了？
窗口会随着视频内容而撑大，要在显示窗口时重新设置一次

使用isOpened()判断摄像头是否已打开
采集数据时要判断数据是否获取到了
'''

import cv2

# 创建VideoWrite为写多媒体文件
fourcc = cv2.VideoWriter_fourcc(*'DIVX')  # 指定DIVX编码格式 
vw = cv2.VideoWriter('./opencv/out.avi',fourcc, 25, (720,1280))

# 创建窗口
cv2.namedWindow('video', cv2.WINDOW_NORMAL)
cv2.resizeWindow('video', 360, 480)

# 从视频设备/视频文件中读取视频帧
cap = cv2.VideoCapture('./opencv/capvideo.mp4')  # 0

# 判断摄像头是否为打开状态
while cap.isOpened():  # 因为是一帧一帧地读取视频，故用循环
    # 从摄像头读视频帧
    ret, frame = cap.read()
    # print(ret)

    # 将视频帧在窗口中显示
    # cv2.imshow('video', frame) # 如果从摄像头中获取视频这一行即可

    # 写数据到多媒体文件
    # vw.write(frame)
    if ret == True:
        cv2.imshow('video', frame)

        # 重新将窗口设置为指定大小
        cv2.resizeWindow('video', 360, 480)

        vw.write(frame)

    #等待键盘事件，如果为q，退出
        key = cv2.waitKey(10)
        if key & 0xFF == ord('q'):
            break
    else:
        break

# 释放VideoCapture
cap.release()

# 释放VideoWrite
vw.release()

cv2.destroyAllWindows()