# 如何通过opencv保存图片
'''
imwrite(name,img)
name,要保存的文件名
img,是Mat(矩阵)类型
'''
import cv2
cv2.namedWindow('img', cv2.WINDOW_NORMAL)
img = cv2.imread('D:\\VScode\\opencv\\test.jpeg')
while True:
    cv2.imshow('img', img)

    key = cv2.waitKey(0)

    if(key & 0xFF == ord('q')):  # 获取q的ASSCI值
        break
    elif(key & 0xFF == ord('s')):
        cv2.imwrite('D:\\VScode\\opencv\\123.png',img)
    else:
        print(key)
cv2.destroyAllWindows()

