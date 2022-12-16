#K值据类进行颜色量化 减少图片中颜色数目 减少内存消耗  据类中心替换与其同祖的像素值
import numpy as np
import cv2

img = cv2.imread('wulin.jpeg')
Z=img.reshape((-1,3))
Z=np.float32(Z)
criteria=(cv2.TERM_CRITERIA_EPS +cv2.TERM_CRITERIA_MAX_ITER,10,1.0)  #终止迭代的条件
K=8  #聚类的最终数目
ret,label,center = cv2.kmeans(Z,K,None,criteria,10,cv2.KMEANS_RANDOM_CENTERS)
center=np.uint8(center)
res=center[label.flatten()]
res2=res.reshape((img.shape))
cv2.imshow('res2',res2)
cv2.waitKey(0)
cv2.destroyAllWindows()