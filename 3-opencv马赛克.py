# 我一定会好好学习，认真对待研究生生涯中的每一个挑战，尽全力完成好每一项科研工作！
# 姓名：胡小格
# 开发时间：2022/10/28 20:46

# 给图片打马赛克
import cv2
import numpy as np

if __name__ == '__main__':
    img = cv2.imread('./bao.jpeg')
    print(img.shape)  # 高度582，宽度876

    # 马赛克方式三
    img2 = img[::10, ::10]  # 每10个中取出一个像素，细节被剥离
    cv2.namedWindow('bao', flags=cv2.WINDOW_NORMAL)  # namedWindow新建一个显示窗口  WINDOW_NORMAL 用户可以改变这个窗口大小
    cv2.resizeWindow('bao', 600, 450)  # 该数字指的是窗口的尺寸而不是图片的尺寸
    cv2.imshow('bao', img2)

    cv2.waitKey()
    cv2.destroyAllWindows()

