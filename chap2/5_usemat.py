# opencv中重要的结构体Mat(矩阵)
# Mat的浅拷贝与深拷贝
'''

浅拷贝：拷贝对象和被拷贝对象都指向同一个内存空间，修改任何一个对象的数据都会影响另外一个；
举个例子：小明和小红在沙漠中共用一个水瓶喝水，任何一个人喝了水，另外一个人都会剩下更少的水。

深拷贝：拷贝对象和被拷贝对象指向不同的内容空间，修改数据时互不影响。
举个例子：小明和小红各有一个水瓶，各自喝各自的水对对方不影响。

'''
import cv2
import numpy as np

img = cv2.imread('./opencv/chap2/rmb.jpeg')

# 浅拷贝
img2 = img

# 深拷贝
img3 = img.copy()

img[10:100,10:100]=[0,0,255]

cv2.imshow('img',img)
cv2.imshow('img2',img2)
cv2.imshow('img3',img3)

cv2.waitKey(0)
cv2.destroyAllWindows()


