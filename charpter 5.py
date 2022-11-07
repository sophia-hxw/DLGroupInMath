import cv2
import numpy as np

img = cv2.imread("D:/pycharm/lab/cards.jpg")

width,height = 250,350
pts1 = np.float32([[265,308],[460,358],[166,579],[363,633]]) #提取四个点 四个点的像素用电脑编辑就可以看到
pts2 = np.float32([[0,0],[width,0],[0,height],[width,height]])
matrix = cv2.getPerspectiveTransform(pts1,pts2)  #获得透视变化的矩阵
imgOutput = cv2.warpPerspective(img,matrix,(width,height)) #对图像进行透视变化即变形 斜变成正

cv2.imshow("Image",img)
cv2.imshow("Output",imgOutput)

cv2.waitKey(0)