# 如何通过opencv加载显示图片
'''
1、imread()
Mat imread(filename, int flags = IMREAD_COLOR );
第一个参数，指需要载入图片的路径
第二个参数，int类型的flags，为载入标识，指定一个加载图像的颜色类型，默认值为1
flags=0返回灰度图像
返回值是一个矩阵

疑问：key & 0xFF == ord('q') 中0xFF怎么理解？
'''
import cv2
cv2.namedWindow('img', cv2.WINDOW_NORMAL)
img = cv2.imread('./opencv/test.jpeg')
cv2.imshow('img', img)
key = cv2.waitKey(0)
# print(key)   # 获取的是key的ASCII码值
# print(ord('q'))
if key & 0xFF == ord('q'):  # 获取q的ASCII值
    cv2.destroyAllWindows()