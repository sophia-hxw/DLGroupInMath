import cv2
import numpy as np
import matplotlib.pyplot as plt

img = cv2.imread("D:/opencv/cat.jpeg")
imgGray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
hist = cv2.calcHist([imgGray],[0],None,[256],[0,256])  #图像直方图

plt.figure(figsize=(10,8))
plt.plot(hist)
plt.show()
cv2.imshow("ImgGray",imgGray)
cv2.waitKey(0)