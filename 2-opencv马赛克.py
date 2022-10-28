# 我一定会好好学习，认真对待研究生生涯中的每一个挑战，尽全力完成好每一项科研工作！
# 姓名：胡小格
# 开发时间：2022/10/28 20:27

# 给图片打马赛克
"""
axis=0,axis=1
轴用来为超过一维数组定义的属性，二维数据拥有两个轴：
第0轴沿着行的方向垂直向下，第1轴沿着列的方向水平延伸。
1表示横轴，方向从左到右；
0表示纵轴，方向从上到下。
当axis=1时，数组的变化是横向的，体现出列的增加或者减少。
反之，当axis=0时，数组的变化是纵向的，体现出行的增加或减少。
"""
import cv2
import numpy as np

if __name__ == '__main__':
    img = cv2.imread('./bao.jpeg')
    print(img.shape)  # 高度582，宽度876

    # 马赛克方式二
    img2 = cv2.resize(img, (35, 23))
    img3 = np.repeat(img2, 10, axis=0)  # 重复行  10表示扩大10倍， axis=0 数组的变化是纵向的，行增加或减少
    img4 = np.repeat(img3, 10, axis=1)  # 重复列  axis=1时，数组的变化是横向的，列增加或者减少
    cv2.imshow('bao2', img2)
    cv2.imshow('bao3', img3)
    cv2.imshow('bao4', img4)

    cv2.waitKey()
    cv2.destroyAllWindows()
