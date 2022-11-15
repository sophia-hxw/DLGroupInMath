# opencv控制鼠标

"""
设置鼠标回调函数
1、setMouseCallback(winname,callback,userdata)
第一个参数：窗口名字
第二个参数：鼠标事件的回调函数
第三个参数：传递给回调的可选参数

2、callback(event,x,y,flags,userdata)
event:鼠标移动、按下左键……
x,y:鼠标坐标
flags:鼠标键及组合键

np.zeros()返回来一个给定形状和类型的用0填充的数组
"""


import cv2
import numpy as np


# 鼠标回调函数
def mouse_callback(event, x, y, flags, userdata):
    print(event, x, y, flags, userdata)


# 创建窗口
cv2.namedWindow('mouse', cv2.WINDOW_NORMAL)
cv2.resizeWindow('mouse',640,360)

# 设置窗口回调
cv2.setMouseCallback('mouse', mouse_callback,'123')

# 显示窗口和背景
img = np.zeros((360, 640, 3), np.uint8)  # 生成一个黑色窗口，用于在上面绘制绘制图形
while True:
    cv2.imshow('mouse', img)
    key = cv2.waitKey(1)
    if key & 0xFF == ord('q'):
        break
cv2.destroyAllWindows()



