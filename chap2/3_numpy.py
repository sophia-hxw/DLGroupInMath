# Numpy基本操作之矩阵的检索与赋值
"""
[y,x]
[y,x,channel]
"""

import numpy as np
import cv2

# 创建一个纯黑色的图片
img = np.zeros((480,640,3), np.uint8)

#从矩阵中读某个元素的值 
print(img[100,100])  # [0 0 0]

count = 0
# 向矩阵中某个元素赋值
while count<200:
    # BGR
    # img[count,100]=255  # 横坐标不变始终是100-->一条白色的竖线 (255,255,255)
    # 赋值方式一
    # img[count,100,0]=255  # 一条蓝色的竖线(255,0,0)
    # img[count,100,1]=255  # 一条绿色的竖线(0,255,0)
    # 赋值方式二
    img[count,100]=[0,0,255]
    count += 1

cv2.imshow('img', img)
key = cv2.waitKey(0)
if key & 0xFF == ord('q'):
    cv2.destroyAllWindows()




