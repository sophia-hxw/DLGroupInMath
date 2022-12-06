import numpy as np
import random
#random.rand()
arr = np.random.rand(3,2) #3行2列 (3) 3行1列 (3,2,2) 3个2*2的数组
#print (arr)  #产生0-1随机数

#random.random()
arr2 = np.random.random(3)#产生0-1随机数 不能产生(3,2)
#numpy中的小数
t1 = np.array([random.random() for i in range (10)])
print(t1)
print(t1.dtype)

t2 = np.round(t1,2)  #保留两位小数
print(t2)

#random.randint() #上限，下限，个数，类型
arr3 = np.random.randint(0,10,5)  #生成随机数

#random.randn() #返回一个或一组样本 具有标准正态分布
arr4 = np.random.randn(2,4)

#random.normal() 生成高斯分布的概率密度随机数 浮点型，均值；浮点型，标准差；个数
arr5 = np.random.normal(loc=1,scale=2,size=5)
#print(arr5)

