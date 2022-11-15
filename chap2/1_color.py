# opencv色彩空间转换

"""
cv2.cvtColor
参数一:要进行处理的图片
参数二：色彩转换方式
"""

import cv2

def callback():
    pass


cv2.namedWindow('color', cv2.WINDOW_NORMAL)
cv2.resizeWindow('color', 640, 480)

img = cv2.imread('./opencv/chap2/rmb.jpeg')

colorspaces = [cv2.COLOR_BGR2BGRA, cv2.COLOR_BGR2GRAY, 
              cv2.COLOR_BGR2RGBA, cv2.COLOR_BGR2HSV,
              cv2.COLOR_BGR2YUV]

# 创建trackbar  名字、窗口名字、默认当前值、最大值、回调方法
cv2.createTrackbar('curcolor', 'color', 0, len(colorspaces), callback)

while True:
    index = cv2.getTrackbarPos('curcolor', 'color')

    # 颜色空间转换API
    cvt_img = cv2.cvtColor(img,colorspaces[index])
    cv2.imshow('color', cvt_img)
    
    key = cv2.waitKey(10)
    if key & 0xFF == ord('q'):
        break

cv2.destroyAllWindows()
