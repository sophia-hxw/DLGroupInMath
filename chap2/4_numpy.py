# numpy基本操作 获取子矩阵
"""
[y1:y2,x1:x2]
[:,:]
"""
import numpy as np
import cv2

# 创建一个纯黑色的图片 高，宽，通道
img = np.zeros((480,640,3), np.uint8)

roi = img[100:400, 100:600]
roi[:,:] = [0,0,255]  #[:,:]表示所有像素/矩阵中所有元素点
roi[:,10] = [0,0,0]
roi[10:200,10:200] = [0,255,0]


cv2.imshow('img', roi)
key = cv2.waitKey(0)
if key & 0xFF == ord('q'):
    cv2.destroyAllWindows()



