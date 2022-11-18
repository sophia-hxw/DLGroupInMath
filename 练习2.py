import cv2
import numpy as np
blank_image = np.zeros((400,532,3), np.uint8)
blank_image.fill(255)
img = cv2.imread('wulin.jpeg')
x1,y1 = img.shape[:2]
print(img.shape)
print(blank_image.shape)
x0,y0 = blank_image.shape[:2]
if x1>400 and y1<=532:
    y2 = 400/img.shape[0]
    dim1 = (int(img.shape[1]*y2),400)
    img2 = cv2.resize(img,dim1)
    print(img2.shape)
    x2,y2 = img2.shape[:2]
    yoff2 = ((x0 - x2) // 2)
    xoff2 = ((y0 - y2) // 2)
    result = blank_image.copy()
    result[yoff2:yoff2 + x2, xoff2:xoff2 + y2] = img2
elif x1<=400 and y1>532:
    x3 = 532/img.shape[1]
    dim2 = (532,int(img.shape[0]*x3))
    img3 = cv2.resize(img,dim2)
    print(img3.shape)
    x3,y3 = img3.shape[:2]
    yoff3 = ((x0 - x3) // 2)
    xoff3 = ((y0 - y3) // 2)
    result = blank_image.copy()
    result[yoff3:yoff3 + x3, xoff3:xoff3 + y3] = img3
elif x1 > 400 and y1 > 532:
    x4 = 532 / img.shape[1]
    dim2 = (532, int(img.shape[0] * x4))
    img4 = cv2.resize(img, dim2)
    print(img4.shape)
    x4, y4 = img4.shape[:2]
    yoff4 = ((x0 - x4) // 2)
    xoff4 = ((y0 - y4) // 2)
    result = blank_image.copy()
    result[yoff4:yoff4 + x4, xoff4:xoff4 + y4] = img4
else:
    yoff1 = ((x0 - x1) // 2)
    xoff1 = ((y0 - y1) // 2)
    result = blank_image.copy()
    result[yoff1:yoff1 + x1, xoff1:xoff1 + y1] = img
#cv2.imshow('i', blank_image)
cv2.imshow('result',result)
cv2.imshow('img', img)
cv2.waitKey(0)