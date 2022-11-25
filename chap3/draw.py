# opencv绘制直线/矩形/圆/椭圆/多边形
"""
1、line(img,起始点,结束点,颜色,线宽，线型)
img:在那个图像上画线
开始点、结束点：指定线的开始位置与结束位置
颜色，线宽，线型
缩放比例

2、rectangle(img,p1,p2,color,[,thickness,linetype])
img:在那个图像上画线
p1,p2:矩形对角线的顶点
color:颜色 
thickness:线宽 取负值时函数绘制填充了色彩的矩形。


3、circle(img, center, radius, color[,thickness[,lineType])
center:圆心坐标
redius:半径
thickness:线宽 取负值时函数绘制填充了色彩的矩形。

4、ellipse(img, center, axes, angle, startAngle, endAngle, color[,thickness[,lineType]) 
center:中心点坐标
axes:长宽的一半
angle:长方体旋转角度
startAngle：开始角度
endAngle:结束角度

5、cv.polylines(img,pts,isClosed,color[,thickness[,lineType])
pts:点的集合
isClosed:是否闭合，True闭合，False不闭合

fillPoly(img, pts, color)
"""

import cv2 
import numpy as np

# (y,x,通道数)
img = np.zeros((480,640,3),np.uint8)

# 画线，坐标点为(x,y)
cv2.line(img,(10,20),(10,400),(0,0,255),5)

# 画矩形
cv2.rectangle(img,(10,10),(100,100),(0,0,255),-1)

# 画圆
cv2.circle(img,(320,240),100,(0,0,255))

# 画椭圆
# 角度是从右边开始按顺时针计算的
# 画布、中心、椭圆半径、旋转角度、开始角度、结束角度、颜色、线宽
cv2.ellipse(img,(320,240),(100,50),90,0,360,(0,0,255),-1)

# 画多边形
pts = np.array([(300,10),(150,100),(450,100)])
cv2.polylines(img,[pts],True,(0,0,255))
# 填充多边形
cv2.fillPoly(img,[pts],(255,255,0))

cv2.imshow('draw',img)
cv2.waitKey()
cv2.destroyAllWindows()