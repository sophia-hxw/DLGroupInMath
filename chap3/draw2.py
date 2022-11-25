# opencv绘制文本
"""
putText(img,text,org,fontFace,fontScale,color[,thickness[,lineType]])
text:字符串
org:起始点
fontFace:字体
fontScale:字号
"""
import cv2
import numpy as np
img = np.zeros((480,640,3),np.uint8)

cv2.putText(img,"hello world!",(10,400), cv2.FONT_HERSHEY_DUPLEX,3,(255,0,0))

cv2.imshow('draw',img)
cv2.waitKey(0)
cv2.destroyAllWindows()



