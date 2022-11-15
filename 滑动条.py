import cv2
import numpy as np
img = cv2.imread("leaves.jpeg")
imgResize = cv2.resize(img,(600,400))
hsv = cv2.cvtColor(imgResize,cv2.COLOR_BGR2HSV)

def empty(i): #回调函数
    h_min = cv2.getTrackbarPos("Hue Min", "TrackBars")   #滑动条的数值共6个
    h_max = cv2.getTrackbarPos("Hue Max", "TrackBars")
    s_min = cv2.getTrackbarPos("Sat Min", "TrackBars")
    s_max = cv2.getTrackbarPos("Sat Max", "TrackBars")
    v_min = cv2.getTrackbarPos("Val Min", "TrackBars")
    v_max = cv2.getTrackbarPos("Val Max", "TrackBars")

    lower = np.array([h_min,s_min,v_min]) #颜色空间阈值
    upper = np.array([h_max,s_max,v_max])

    mask = cv2.inRange(hsv,lower,upper) #根据颜色空间阈值生成掩膜
    htich = np.hstack((imgResize, hsv))
    #htich2 = np.hstack((imgResize,mask))
    cv2.imshow("merged", htich)
    #cv2.imshow("merged", htich2)
    cv2.imshow("mask", mask)

cv2.namedWindow("TrackBars") #窗口标题
cv2.resizeWindow("TrackBars",640,240)#设置窗口大小
#滑动条的名字，滑动条被放置窗口的名字，滑动条默认值，滑动条的最大值，回调函数，每次滑动都会调用到回调函数
cv2.createTrackbar("Hue Min","TrackBars",0,179,empty)  #创建轨迹栏 色调最小值
cv2.createTrackbar("Hue Max","TrackBars",34,179,empty)  #179，179
cv2.createTrackbar("Sat Min","TrackBars",77,255,empty) #饱和度最小值 0，255
cv2.createTrackbar("Sat Max","TrackBars",193,255,empty) #255，255
cv2.createTrackbar("Val Min","TrackBars",9,255,empty) #明度最小值 #0，255
cv2.createTrackbar("Val Max","TrackBars",178,255,empty) #255，255

empty(0) #调用函数
cv2.waitKey(0)
