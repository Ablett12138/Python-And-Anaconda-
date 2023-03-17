#------------- 包 ---------------------#
import cv2
import numpy as np
from matplotlib import pyplot as plt
import myfunction as mf

#显示图片
img=cv2.imread('china1.jpg')
gray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

mf.cv_show(img,cv2.WINDOW_NORMAL)

#得到关键点
sift = cv2.SIFT_create() 
kp = sift.detect(gray,None)

#绘制关键点
img1 = cv2.drawKeypoints(gray,kp,img)
mf.cv_show(img1,cv2.WINDOW_NORMAL)

#计算特征
kp, des = sift.compute(gray,kp)
print (np.array(kp).shape)
