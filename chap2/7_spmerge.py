# 通道的分割与合并

''''
1、split(mat)
参数是图像数据，返回值是B、G、R单通道图像

2、merge((ch1,ch2,...))
将 B、G、R 单通道合并为 三通道 BGR 彩色图像
参数是单通道图像，返回值是BGR彩色图像
'''
import cv2
import numpy as np

# 创建一个全黑的背景图像
img = np.zeros((480,640,3),np.uint8)
# img = cv2.imread('./opencv/chap2/rmb.jpeg')

# 将BGR彩色图形分离成B、G、R单通道图形
b,g,r = cv2.split(img)  

b[10:100,10:100] = 255 #  将b单通道图形一小块区域变成白色
g[10:100,10:100] = 255

# 将B、G、R单通道合并为三通道BGR彩色图像
img2 = cv2.merge((b,g,r))

cv2.imshow('img',img)

cv2.imshow('b',b)
cv2.imshow('g',g)
cv2.imshow('r',r)

# (B,G,R)->(255,255,0)->青色
cv2.imshow('img2',img2) 

cv2.waitKey(0)
cv2.destroyAllWindows()

