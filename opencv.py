#仅有一个特征的数据 K均值聚类
import numpy as np
import cv2
from matplotlib import pyplot as plt
x=np.random.randint(25,100,25)
y=np.random.randint(175,255,25)
z=np.hstack((x,y))
z=z.reshape((50,1))
z=np.float32(z)
plt.hist(z,256,[0,256]),plt.show()

#精确度1.0 迭代10次
criteria=(cv2.TERM_CRITERIA_EPS +cv2.TERM_CRITERIA_MAX_ITER,10,1.0)
flags = cv2.KMEANS_RANDOM_CENTERS #如何选择起始重心
#紧密度:每个点到相应重心的平方和 标志 中心
compactness,labels,centers = cv2.kmeans(z,2,None,criteria,10,flags)

A=z[labels==0]
B=z[labels==1]
#红色数据表示A 蓝色数据表示B 黄色表示重心
plt.hist(A,256,[0,256],color='r')
plt.hist(B,256,[0,256],color='b')
plt.hist(centers,32,[0,256],color='y')
plt.show()
