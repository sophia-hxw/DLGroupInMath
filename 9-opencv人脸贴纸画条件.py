# 人脸贴纸画
"""
不足：只会抠白底(255,255,255)和黑底(0,0,0)的图片
"""
import numpy as np
import cv2

if __name__ == '__main__':
    img = cv2.imread('./nba.jpeg')
    gray = cv2.cvtColor(img, code = cv2.COLOR_BGR2GRAY)
    face_detector = cv2.CascadeClassifier('./haarcascade_frontalface_alt.xml')
    faces = face_detector.detectMultiScale(gray)
    head = cv2.imread('./head.jpeg')
    for x, y, w, h in faces:
        head2 = cv2.resize(head, (w, h))  # 使图片尺寸与人脸尺寸一样大
        for i in range(h):
            for j in range(w):
                if not (head2[i, j] > 240).all():
                    img[i+y, j+x] = head2[i, j]
    cv2.imshow('head', img)
    cv2.waitKey()
    cv2.destroyAllWindows()



