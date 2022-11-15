# 图像操作的基石Numpy
'''
opencv中用到的矩阵都要转化成Numpy数组
Numpy是一个经高度优化的python数值库

创建矩阵:
创建数组 array()
创建全0数组zeros()/全1数组ones()
创建全值数组 full()
创建单位矩阵 identity()/eye()

检索与赋值[y,x]
获取子数组[:,:]

图像的处理其实就是矩阵的处理
'''

import numpy as np

# 通过array定义矩阵
print('----------a----------')
a = np.array([1, 2, 3])  # 一维数组
print(a)

print('----------b----------') # 二维数组
b = np.array([[1, 2, 3],[4, 5, 6]])
print(b)

print('----------b1----------') # 三维数组
b1= np.array([[[1, 2, 3],[4, 5, 6]]])  
print(b1)

# 定义zeros矩阵   行的个数-->高，列的个数-->宽，通道数
print('-----------c---------')
c = np.zeros((4,5,3), np.uint8) 
print(c)

# 定义ones矩阵
print('-----------d----------')
d = np.ones((4,5,3), np.uint8)
print(d)

# 定义full()矩阵
print('--------e---------')
e = np.full((4,5,3),255,np.uint8)
print(e)

# 定义单位矩阵
print('------------f-----------')
f = np.identity(4)
print(f)

print('-----------g--------')
g = np.eye(5,7,k=1)  # 可以是长方形
print(g)
