# 我一定会好好学习，认真对待研究生生涯中的每一个挑战，尽全力完成好每一项科研工作！
# 姓名：胡小格
# 开发时间：2022/10/30 12:55

# 检测多张人脸时，当有的人脸检测不到时
"""
scaleFactor：表示在前后两次相继的扫描中，搜索窗口的缩放比例
minNeighbors：表示构成检测目标的相邻矩形的最小个数。
默认值为3，表示有3个以上的检测标记存在时，才认为人脸的存在。
如果希望提高检测的准确率，可以将该值设置的更大，但同时可能会让一些人脸无法被检测到
"""
import numpy as np
import cv2

if __name__ == '__main__':
    img = cv2.imread('./nvpai1.jpeg')
    gray = cv2.cvtColor(img, code=cv2.COLOR_BGR2GRAY)  # 彩色变黑白，三维变二维，数据变少
    # haarcascade_frontalface_alt.xml 人脸特征详细说明，24350行，计算机根据这些特征，进行人脸检测
    # 符合其中一部分，算作人脸
    # CascadeClassifier：级联分类器（检测器）
    face_detector = cv2.CascadeClassifier('./haarcascade_frontalface_alt.xml')
    faces = face_detector.detectMultiScale(gray,
                                           scaleFactor=1.05,  # 缩放，默认参数是1.1，把参数调小，可以检测到更多的人脸
                                           minNeighbors=3)  # 调用级联分类器检测人脸，返回坐标x,y,w,h 左上角的坐标以及宽和高
    print(faces)  # 输出人脸坐标数据
    for x, y, w, h in faces:  # for循环可以进行数组遍历
        # cv2.rectangle(img,
        #               pt1=(x, y),  # 左上角坐标
        #               pt2=(x+w, h+y),  # 右下角坐标
        #               color=[0, 0, 250],  # 给红色的画线
        #               thickness=2  # 给画线一个宽度
        #               )  # rectangle 画矩形
        cv2.circle(img,
                   center=(x+w//2, y+h//2),  # 圆心
                   radius=w//2,  # 半径
                   color=[0, 255, 0],  # 绿色
                   thickness=2)  # 画绿色的圆

    cv2.imshow('face', img)
    cv2.waitKey()
    cv2.destroyAllWindows()
