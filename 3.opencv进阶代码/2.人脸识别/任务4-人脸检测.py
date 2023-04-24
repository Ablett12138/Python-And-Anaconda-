import numpy as np
import cv2
import myfunction as mf

img=cv2.imread('face.jpg')  
# img = cv2.imread('tu1.jpg')
gray = cv2.cvtColor(img,code=cv2.COLOR_BGR2GRAY)

# 人脸特征数据 haarcascade_frontalface_alt.xml
# CascadeClassifier 级联分类器，检测器
face_detector = cv2.CascadeClassifier('./OpenCV_xml/haarcascade_frontalface_alt.xml')


faces = face_detector.detectMultiScale(gray,     # 坐标x,y,w,h
                                scaleFactor=1.05,   # 缩放
                                minNeighbors=3 )    # 簇的数量 
                                #    minSize = (60,60)     # 最小大小
print(faces)

for (x, y, w, h) in faces:
    img = cv2.rectangle(img, (x,y),(x+w, y+h), (255, 0, 0), 2)
    mf.cv_show(img)

