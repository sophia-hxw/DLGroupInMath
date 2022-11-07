import cv2
import numpy as np

img =np.zeros((512,512,3),np.uint8)
#print(img.shape)
#img[:] = 255,0,0  #给图片上色 [:]给全图

cv2.line(img,(0,0),(img.shape[1],img.shape[0]),(0,255,0),3) #绘制线条 对角线
cv2.rectangle(img,(0,0),(250,350),(0,0,255),cv2.FILLED)  #绘制矩阵 cv2.FILLED填充整个矩阵
cv2.circle(img,(400,50),30,(255,255,0),5) #绘制圆形
cv2.putText(img," OPENCV ",(300,200),cv2.FONT_HERSHEY_COMPLEX,1,(0,150,0),1)  #在图像上放置文本 第一个1为字号 第二个1为粗细程度

cv2.imshow("Image",img)

cv2.waitKey(0)