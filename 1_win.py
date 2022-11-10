# 通过opencv创建显示窗口
"""
创建和显示窗口

1、namedWindow()  创建窗口
第一个参数为窗口名，第二个参数窗口显示方式
cv2.WINDOW_NORMAL 可以手动改变窗口的大小
cv2.WINDOW_AUTOSIZE  不可以改变窗口的大小 默认

2、imshow()  显示窗口
cv.imshow(	winname, mat	)
第一个参数为窗口名，第二个参数为传入的矩阵
可以不写cv2.namedWindow()而直接写imshow()
表示直接创建窗口并显示出来

3、destroyAllWindow() 销毁窗口

4、resizeWindow() 设置窗口大小
三个参数，第一个参数是窗口名字，第二个窗口是宽度，第三个是高度

5、waitKey()
def waitKey(delay=None)
waitKey() 函数的功能是不断刷新图像 , 频率时间为delay , 单位为ms 
返回值为当前键盘按键的ASSCI值
waitKey()–是在一个给定的时间内(单位ms)等待用户按键触发
设置 waitKey(0) , 则表示程序会无限制的等待用户的按键事件

显示视频时，延迟时间需要设置为 大于0的参数
用于设置在显示完一帧图像后程序等待 ”delay”ms 再显示下一帧视频 
如果使用 waitKey(0) 则只会显示第一帧视频
"""

import cv2
# cv2.namedWindow('new', cv2.WINDOW_AUTOSIZE)
cv2.namedWindow('new', cv2.WINDOW_NORMAL)  # 创建窗口  第一个参数为窗口名，第二个参数窗口显示方式
cv2.resizeWindow('new', 640, 480)  # 设置窗口的大小
cv2.imshow('new', 0)  # 显示窗口 第一个参数为窗口名，第二个参数为传入的矩阵，这里传入0可自动转换成矩阵
key = cv2.waitKey(0)  # 单位：毫秒  1000毫秒=1秒
cv2.destroyAllWindows()  # 销毁窗口，回收内存

