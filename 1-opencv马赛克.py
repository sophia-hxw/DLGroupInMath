# 我一定会好好学习，认真对待研究生生涯中的每一个挑战，尽全力完成好每一项科研工作！
# 姓名：胡小格
# 开发时间：2022/10/28 16:18

# 给图片打马赛克
import cv2
import numpy as np

if __name__ == '__main__':
    img = cv2.imread('./bao.jpeg')
    print(img.shape)  # 高度582，宽度876

    # 马赛克方式一  先压缩，再放大
    img2 = cv2.resize(img, (35, 23))  # 缩小尺寸
    img3 = cv2.resize(img2, (876, 582))  # 放大尺寸  这写数字指的是图片的尺寸
    cv2.imshow('bao2', img2)
    cv2.imshow('bao3', img3)

    cv2.waitKey()
    cv2.destroyAllWindows()



