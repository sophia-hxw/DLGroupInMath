#掩膜的应用
import cv2
import numpy as np
import matplotlib.pyplot as plt

img = cv2.imread("D:/opencv/cat.jpeg")
imgGray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

mask = np.zeros(img.shape[:2],np.uint8) #创建掩膜
mask[400:650,200:500] = 255  #255为白色 1为黑色
mask_img = cv2.bitwise_and(imgGray,imgGray,mask=mask)

mask_hist = cv2.calcHist([imgGray],[0],mask,[256],[0,256])
#plt.plot(mask_hist)
#plt.show()

dst = cv2.equalizeHist(imgGray) #直方图均衡化

cl = cv2.createCLAHE(2.0,(8,8)) #自适应均衡化
clahe = cl.apply(imgGray)

#cv2.imshow("Img",img)
#cv2.imshow("ImgGray",imgGray)
#cv2.imshow("ImgGray",imgGray)
#cv2.imshow("Mask",mask)
#cv2.imshow("Mask_img",mask_img)
#cv2.imshow("Dst",dst)
cv2.imshow("Clahe",clahe)
cv2.waitKey(0)