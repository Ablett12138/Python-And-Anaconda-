import numpy as np
import cv2
import os
import myfunction as mf

if __name__ == '__main__':
    img_path = 'face'
    fileNames = os.listdir(img_path)  #获取当前文件路径下的文件名，返回list
    img_list = []
    img_size = np.size(fileNames)
    for file in fileNames:
        img_folder = img_path + '\\' + file   #图片路径
        print(img_folder)

        # 读取图像1
        img=cv2.imread(img_folder)  
        # img = cv2.imread('tu1.jpg')
        gray = cv2.cvtColor(img,code=cv2.COLOR_BGR2GRAY)

        # 人脸特征数据 haarcascade_frontalface_alt.xml
        # CascadeClassifier 级联分类器，检测器
        face_detector = cv2.CascadeClassifier('./OpenCV_xml/haarcascade_frontalface_alt.xml')
        eye_cascade = cv2.CascadeClassifier('./OpenCV_xml/haarcascade_eye.xml')
        mouth_cascade = cv2.CascadeClassifier('./OpenCV_xml/haarcascade_mcs_mouth.xml')
        nose_cascade = cv2.CascadeClassifier('./OpenCV_xml/haarcascade_mcs_nose.xml')
    

        faces = face_detector.detectMultiScale(gray,     # 坐标x,y,w,h
                                            scaleFactor=1.05,   # 缩放
                                            minNeighbors=3 )    # 簇的数量 
                                            #    minSize = (60,60)     # 最小大小
        print(faces)

        for (x, y, w, h) in faces:
            img = cv2.rectangle(img, (x,y),(x+w, y+h), (255, 0, 0), 2)
            roi_gray = gray[y:y+h, x:x+w]
            roi_color = img[y:y+h, x:x+w]
            #眼睛
            eyes = eye_cascade.detectMultiScale(roi_gray, 1.3, 10 ,minSize = (30,30))
            for (ex,ey,ew,eh) in eyes:
                cv2.rectangle(roi_color, (ex, ey),(ex+ew, ey+eh), (0, 255, 0), 2)
            #嘴巴
            mouth = mouth_cascade.detectMultiScale(roi_gray, 1.3,20)
            for (mx, my, mw, mh) in mouth:
                cv2.rectangle(roi_color, (mx, my), (mx+mw, my+mh), (0, 0, 255), 2)
            #鼻子
            nose = nose_cascade.detectMultiScale(roi_gray, 1.2, 5)
            for (nx, ny, nw, nh) in nose:
                cv2.rectangle(roi_color, (nx, ny), (nx+nw, ny+nh), (255, 0, 255), 2)
        

                    
        mf.cv_show(img)

