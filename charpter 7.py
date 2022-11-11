import cv2
import numpy as np

def empty(a):
    pass

def stackImages(scale,imgArray):  #重叠函数
    rows = len(imgArray)
    cols = len(imgArray[0])
    rowsAvailable = isinstance(imgArray[0], list)
    width = imgArray[0][0].shape[1]
    height = imgArray[0][0].shape[0]
    if rowsAvailable:
        for x in range ( 0, rows):
            for y in range(0, cols):
                if imgArray[x][y].shape[:2] == imgArray[0][0].shape [:2]:
                    imgArray[x][y] = cv2.resize(imgArray[x][y], (0, 0), None, scale, scale)
                else:
                    imgArray[x][y] = cv2.resize(imgArray[x][y], (imgArray[0][0].shape[1], imgArray[0][0].shape[0]), None, scale, scale)
                if len(imgArray[x][y].shape) == 2: imgArray[x][y]= cv2.cvtColor( imgArray[x][y], cv2.COLOR_GRAY2BGR)
        imageBlank = np.zeros((height, width, 3), np.uint8)
        hor = [imageBlank]*rows
        hor_con = [imageBlank]*rows
        for x in range(0, rows):
            hor[x] = np.hstack(imgArray[x])
        ver = np.vstack(hor)
    else:
        for x in range(0, rows):
            if imgArray[x].shape[:2] == imgArray[0].shape[:2]:
                imgArray[x] = cv2.resize(imgArray[x], (0, 0), None, scale, scale)
            else:
                imgArray[x] = cv2.resize(imgArray[x], (imgArray[0].shape[1], imgArray[0].shape[0]), None,scale, scale)
            if len(imgArray[x].shape) == 2: imgArray[x] = cv2.cvtColor(imgArray[x], cv2.COLOR_GRAY2BGR)
        hor= np.hstack(imgArray)
        ver = hor
    return ver

path = 'D:/pycharm/lab/lambo.jpg'
cv2.namedWindow("TrackBars")
cv2.resizeWindow("TrackBars",640,240)
cv2.createTrackbar("Hue Min","TrackBars",0,179,empty)  #创建轨迹栏 色调最小值
cv2.createTrackbar("Hue Max","TrackBars",34,179,empty)  #179，179
cv2.createTrackbar("Sat Min","TrackBars",77,255,empty) #饱和最小值 0，255
cv2.createTrackbar("Sat Max","TrackBars",193,255,empty) #255，255
cv2.createTrackbar("Val Min","TrackBars",9,255,empty) #值最小值 #0，255
cv2.createTrackbar("Val Max","TrackBars",178,255,empty) #255，255

while True:  #读取轨迹栏值 以便应用在图像上
    img = cv2.imread(path)
    imgHSV = cv2.cvtColor(img,cv2.COLOR_BGR2HSV)  #将图片变为HSV
    h_min = cv2.getTrackbarPos("Hue Min","TrackBars")
    h_max = cv2.getTrackbarPos("Hue Max", "TrackBars")
    s_min = cv2.getTrackbarPos("Sat Min", "TrackBars")
    s_max = cv2.getTrackbarPos("Sat Max", "TrackBars")
    v_min = cv2.getTrackbarPos("Val Min", "TrackBars")
    v_max = cv2.getTrackbarPos("Val Max", "TrackBars")
    print(h_min,h_max,s_min,s_max,v_min,v_max)     #提取该范围内特定颜色的特定图像
    lower = np.array([h_min,s_min,v_min])
    upper = np.array([h_max,s_max,v_max])
    mask = cv2.inRange(imgHSV,lower,upper)  #过滤图片的颜色
    imgResult = cv2.bitwise_and(img,img,mask=mask) #通过滑动轨迹栏 获得想要提取颜色部分的轨迹栏 在前面改成相应的数值

    #cv2.imshow("Original",img)
    #cv2.imshow("HSV",imgHSV)
    #cv2.imshow("Mask", mask)
    #cv2.imshow("Result", imgResult)

    imgStack = stackImages(0.6,([img,imgHSV],[mask,imgResult])) #把四张图拼起来
    cv2.imshow("Stacked Images",imgStack)

    cv2.waitKey(0)