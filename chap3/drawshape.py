#opencv实现鼠标绘制基本图形
"""
基本功能：
可以通过鼠标进行基本图形绘制
1.可以画线：当用户按下L键，即选择了画线，此时滑动鼠标即可画线
2.可以画矩形：当用户按下R键，即选择了画线，此时滑动鼠标即可画线
3.可以画圆：当用户按下C键，即选择了画线，此时滑动鼠标即可画线
"""


import cv2
import numpy as np

# 全局变量
curhshape = 0
startpos = (0,0)

# 显示窗口和背景
img = np.zeros((480, 640, 3), np.uint8)  # 生成一个黑色窗口，用于在上面绘制绘制图形

# 鼠标回调函数
def mouse_callback(event, x, y, flags, userdata):
    # print(event, x, y, flags, userdata)

    # 声明全局变量
    global curhshape, startpos

    
    if event & cv2.EVENT_LBUTTONDOWN == cv2.EVENT_LBUTTONDOWN:# 按下左键
        startpos = (x,y)  # 起始点
    elif event & cv2.EVENT_LBUTTONUP == cv2.EVENT_LBUTTONUP: # 抬起左键
        if curhshape == 0:  # drawline
            cv2.line(img, startpos, (x,y), (0,0,255))
        elif curhshape == 1:  # drawrectangle
            cv2.rectangle(img, startpos, (x,y), (0,255,0))
        elif curhshape == 2:  # drawcircle
            a = x - startpos[0]
            b = y - startpos[1]
            r = int((a**2+b**2)**0.5)
            cv2.circle(img, startpos, r, (255,0,0))
        else:
            print('error:no shape')


# 创建窗口
cv2.namedWindow('drawshape', cv2.WINDOW_NORMAL)

# 设置窗口回调
cv2.setMouseCallback('drawshape', mouse_callback)

while True:
    cv2.imshow('drawshape', img)
    key = cv2.waitKey(1) & 0xFF
    if key == ord('q'):
        break
    elif key == ord('l'):  # line
        curhshape = 0
    elif key == ord('r'):  # recatangle
        curhshape = 1
    elif key == ord('c'):  # circle
        curhshape = 2
cv2.destroyAllWindows()