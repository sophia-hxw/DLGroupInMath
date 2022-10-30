# 我一定会好好学习，认真对待研究生生涯中的每一个挑战，尽全力完成好每一项科研工作！
# 姓名：胡小格
# 开发时间：2022/10/29 18:15
"""
for循环遍历整张图片，一个区域一个区域进行排查！
找到符合人脸的区域
检测人脸，左上角给定区域，扫描，向右移动区域
"""

import numpy as np
import cv2

if __name__ == '__main__':
    img = cv2.imread('./nvpai.jpeg')
    # haarcascade_frontalface_alt.xml 人脸特征详细说明，24350行，计算机根据这些特征，进行人脸检测
    # 符合其中一部分，算作人脸
    # CascadeClassifier：级联分类器（检测器）
    face_detector = cv2.CascadeClassifier('./haarcascade_frontalface_alt.xml')
    faces = face_detector.detectMultiScale(img)  # 调用级联分类器检测人脸，返回坐标x,y,w,h 左上角的坐标以及宽和高
    print(faces)  # 输出人脸坐标数据
    for x, y, w, h in faces:  # for循环可以进行数组遍历
        cv2.rectangle(img,
                      pt1=(x, y),  # 左上角坐标
                      pt2=(x+w, h+y),  # 右下角坐标
                      color=[0, 0, 250],  # 给红色的画线
                      thickness=2  # 给画线一个宽度
                      )  # rectangle 画矩形

    cv2.imshow('face', img)
    cv2.waitKey()
    cv2.destroyAllWindows()
