# 图像的多种属性

import cv2
import numpy as np

img = cv2.imread('./opencv/chap2/rmb.jpeg')

# shape属性中包含了三个信息 高度，宽度，通道数
print(img.shape)

# 图像占用多大的内存空间 高度*宽度*通道数
print(img.size)

print(img.dtype)

