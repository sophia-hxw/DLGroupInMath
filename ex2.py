import cv2
import numpy as np

kids = cv2.imread("D:/opencv/kids.jpg")

# 绝对尺寸
rows,cols = kids.shape[:2]
res = cv2.resize(kids,(2*cols,2*rows)) #扩大两倍
#res1 = cv2.resize(kids,None,fx=0.5,fy=0.5)

#M = np.float32([[1,0,100],[0,1,50]]) #图像平移
#res2 = cv2.warpAffine(kids,M,(2*cols,2*rows))

M = cv2.getRotationMatrix2D((cols/2,rows/2),45,0.5)  #图像旋转
res3 = cv2.warpAffine(kids,M,(cols,rows))

#pts1 = np.float32([[50,50],[200,50],[50,200]]) #仿射变换
#pts2 = np.float32([[100,100],[200,50],[100,250]])
#M = cv2.getAffineTransform(pts1,pts2)
#res4 = cv2.warpAffine(kids,M,(cols,rows))

pst1 = np.float32([[56,65],[368,52],[28,387],[389,390]])  #投射变换
pst2 = np.float32([[100,145],[300,100],[80,290],[310,300]])
T = cv2.getPerspectiveTransform(pst1,pst2)
res5 = cv2.warpPerspective(kids,T,(cols,rows))

#imgup = cv2.pyrUp(kids)  #图像金字塔
#imgup2 = cv2.pyrUp(imgup)
#imgdown = cv2.pyrDown(kids)

cv2.imshow("Image",kids)
#cv2.imshow("Res",res)
#cv2.imshow("Res1",res1)
#cv2.imshow("Res2",res2)
cv2.imshow("Res3",res3)
#cv2.imshow("Res4",res4)
#cv2.imshow("Res5",res5)
#cv2.imshow("Imgup",imgup)
#cv2.imshow("Imgup2",imgup2)
#cv2.imshow("Imgdown",imgdown)
cv2.waitKey(0)