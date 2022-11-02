import cv2

if __name__ == '__main__':
    img = cv2.imread('./han.jpeg')
    gray = cv2.cvtColor(img, code=cv2.COLOR_BGR2GRAY)
    face_detector = cv2.CascadeClassifier('./haarcascade_frontalface_alt.xml')
    faces = face_detector.detectMultiScale(gray)
    star = cv2.imread('./star.jpeg')  # star2 = cv2.imread('./star2.jpeg') 黑底
    for x, y, w, h in faces:
        cv2.rectangle(img, pt1=(x, y), pt2=(x+w, y+h), color=[0, 0, 250], thickness=2) # 不要矩形了
        # img[y:y + h, x:x + w] = cv2.resize(star, (w, h))  # 将五角星的尺寸调节和人脸一样大
        img[y:y+h//4, x+(3*w)//8+(3*w)%8:x+w//4+(3*w)//8+(3*w)%8] = cv2.resize(star, (w//4, h//4))  # 将五角星图片移到额头正中间

    cv2.imshow('face', img)
    cv2.waitKey()
    cv2.destroyAllWindows()