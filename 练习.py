import cv2
import numpy as np

img = cv2.imread('wulin.jpeg')
mask = np.zeros(img.shape[:2],np.uint8)
mask[100:200,177:354] = 1
masked_img = cv2.bitwise_and(img,img,mask=mask)
print(masked_img.shape)
area1 = np.array([[0,0],[532,0],[532,100],[0,100]])
area2 = np.array([[0,100],[177,100],[177,200],[0,200]])
area3 = np.array([[0,200],[532,200],[532,300],[0,300]])
area4 = np.array([[354,100],[532,100],[532,200],[354,200]])
cv2.fillPoly(masked_img,[area1,area2,area3,area4],(255,255,255))
cv2.imshow("Img",img)
cv2.imshow("Masked_img",masked_img)
cv2.waitKey(0)
cv2.destroyAllWindows()