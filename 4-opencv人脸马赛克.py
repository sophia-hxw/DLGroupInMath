# 我一定会好好学习，认真对待研究生生涯中的每一个挑战，尽全力完成好每一项科研工作！
# 姓名：胡小格
# 开发时间：2022/10/29 16:37

import cv2
import numpy as np
if __name__ == '__main__':
    img = cv2.imread('./bao.jpeg')  # ./ 表示当前路径
    # 1、人为人脸定位（获取人脸坐标数据）
    # 人脸坐标左上角坐标(320,80),右下角(620,430) 在电脑自带的画图工具中查看 (x,y)-->(宽度,高度)
    # 2、切片获取人脸
    face = img[80:430, 320:620]  # opencv里(高度，宽度) 与画图工具中坐标显示不一样  把脸取下来
    # img[80:430, 320:620] = face[:, :, ::-1]  # 将人脸颜色翻转
    # 间隔切片，重复，赋值
    face = face[::10, ::10]  # 每10个中取出一个像素-->马赛克
    face = np.repeat(face, 10, axis=0)  # 行方向上重复10次
    face = np.repeat(face, 10, axis=1)  # 列方向上取出10次 这两行代码为了与原图尺寸一致
    img[80:430, 320:620] = face  # 将打了马赛克的脸放回到图中 尺寸一致
    # cv2.imshow('bao_face', face)
    # 显示
    cv2.imshow('bao', img)
    cv2.waitKey()
    cv2.destroyAllWindows()
