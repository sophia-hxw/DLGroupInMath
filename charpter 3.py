import cv2
import numpy as np

img = cv2.imread("D:/pycharm/lab/lambo.jpg")
print(img.shape) #显示图像大小 (高，宽)

imgResize = cv2.resize(img,(300,200)) # 调整图片大小 (宽，高)

imgCropped = img[0:200,200:500]  #裁剪图像 (高，宽)

cv2.imshow("Image",img)
#cv2.imshow("Image Resize",imgResize)
cv2.imshow("Image Cropped",imgCropped)  
cv2.waitKey(0)

