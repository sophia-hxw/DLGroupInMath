# opencv中的TrackBar控件

"""
1、createTrackbar
参数：
trackbarname,winname
value:trackbar当前值
count:最小值为0，最大值为count
callback,userdata

2、getTrackbarPos
输入参数：trackbarname、winname
输出：当前值（tracckbar滑块所在的位置）

uint8是专门用于存储各种图像的（包括RGB，灰度图像等），范围是从0–255
"""

import cv2
import numpy as np

def callback():
    pass

#创建窗口
cv2.namedWindow('trackbar', cv2.WINDOW_NORMAL)

# 创建trackbar  名字、窗口名字、默认当前值、最大值、回调方法
cv2.createTrackbar('R', 'trackbar', 0, 255, callback)
cv2.createTrackbar('G', 'trackbar', 0, 255, callback)
cv2.createTrackbar('B', 'trackbar', 0, 255, callback)

# 创建一个纯黑色背景图
img = np.zeros((480, 640, 3), np.uint8)  # 每一个像素都是uint8类型

while True:

    # 获取当前Trackbar的值
    r = cv2.getTrackbarPos('R', 'trackbar')
    g = cv2.getTrackbarPos('G', 'trackbar')
    b = cv2.getTrackbarPos('B', 'trackbar')

    # 改变背景图片颜色
    img[:] = [b, g, r]  

    cv2.imshow('trackbar', img)
    
    key = cv2.waitKey(10)
    if key & 0xFF == ord('q'):
        break

cv2.destroyAllWindows()


