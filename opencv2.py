#仅有多个特征的数据 K均值聚类
import numpy as np
import cv2
from matplotlib import pyplot as plt

X=np.random.randint(25,50,(25,2))
Y=np.random.randint(60,85,(25,2))
Z=np.vstack((X,Y))

Z=np.float32(Z)
criteria=(cv2.TERM_CRITERIA_EPS +cv2.TERM_CRITERIA_MAX_ITER,10,1.0)
ret,labels,center = cv2.kmeans(Z,2,None,criteria,10,cv2.KMEANS_RANDOM_CENTERS)

A=Z[labels.ravel()==0]
B=Z[labels.ravel()==1]
plt.scatter(A[:,0],A[:,1])
plt.scatter(B[:,0],B[:,1],c='r')
plt.scatter(center[:,0],center[:,1],s=80,c='y',marker='s')
plt.xlabel('Height'),plt.ylabel('Weight')
plt.show()