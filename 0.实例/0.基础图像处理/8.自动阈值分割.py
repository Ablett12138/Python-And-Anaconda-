# (2) 阈值分割（阈值分割二值化） 
#+番外篇 4： Otsu 阈值法
#------------- 包 ---------------------#
import cv2
import numpy as np
from matplotlib import pyplot as plt
import myfunction as m

#1.--------------------------      阈值分割（阈值分割二值化） -------------------------------#
# 自适应阈值对比固定阈值
img = cv2.imread('fankuaituduoge.bmp', 0)
# 固定阈值
ret, th1 = cv2.threshold(img, 127, 255, cv2.THRESH_BINARY)
# 自适应阈值
th2 = cv2.adaptiveThreshold(img, 255, cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY, 35, 4)
th3 = cv2.adaptiveThreshold(img, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 35, 6)
titles = ['Original', 'Global(v = 127)', 'Adaptive Mean', 'Adaptive Gaussian']
images = [img, th1, th2, th3]
for i in range(4):
    plt.subplot(2, 2, i + 1), plt.imshow(images[i], 'gray')
    plt.title(titles[i], fontsize=8)
    plt.xticks([]), plt.yticks([])
plt.show()

#1.--------------------------      阈值分割（Otsu 阈值法） -------------------------------#

img=cv2.imread('otus.png',0)
# 固定阈值法
ret1, th1 = cv2.threshold(img, 100, 255, cv2.THRESH_BINARY)
# Otsu 阈值法
ret2, th2 = cv2.threshold(img, 0, 255, cv2.THRESH_BINARY+cv2.THRESH_OTSU)
# 先进行高斯滤波，再使用 Otsu 阈值法
blur = cv2.GaussianBlur(img, (5, 5), 0)
ret3, th3 = cv2.threshold(blur, 0, 255, cv2.THRESH_BINARY+cv2.THRESH_OTSU)

#图像集
images = [img, 0, th1, img, 0, th2, blur, 0, th3]
#标题集
titles = ['Original', 'Histogram', 'Global(v=100)','Original', 'Histogram', "Otsu's",'Gaussian filtered Image', 'Histogram', "Otsu's"]
for i in range(3):
    # 绘制原图
    plt.subplot(3, 3, i*3 + 1)
    plt.imshow(images[i*3], 'gray')
    plt.title(titles[i*3], fontsize=8)
    plt.xticks([]), plt.yticks([])
    # 绘制直方图 plt.hist， ravel 函数将数组降成一维
    plt.subplot(3, 3, i*3 + 2)
    plt.hist(images[i*3].ravel(), 256)
    plt.title(titles[i*3 + 1], fontsize=8)
    plt.xticks([]), plt.yticks([])
    # 绘制阈值图
    plt.subplot(3, 3, i*3 + 3)
    plt.imshow(images[i*3 + 2], 'gray')
    plt.title(titles[i*3 + 2], fontsize=8)
    plt.xticks([]), plt.yticks([])
plt.show()


