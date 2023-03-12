#------------- 图像梯度
#1.                     图像梯度-Sobel算子
#右减左 下减上   
# cv.CV_64F====能表示负数形式
# . ddepth:图像的深度
# ·dx=1和dy=0分别表示水平和竖直方向
# . ksize是Sobel算子的大小
# 水平方向
sobelx = cv.Sobel(img, cv.CV_64F,1,0,ksize=3)
#对求取的梯度求绝对值
sobelx = cv.convertScaleAbs (sobelx)

# 竖直方向
sobely = cv.Sobel(img, cv.CV_64F,0,1,ksize=3)
#对求取的梯度求绝对值
sobely = cv.convertScaleAbs (sobely)

#求和
#0 为偏置项
sobelxy = cv.addWeighted(sobelx, 0.5,sobely,0.5,0)


#2.                        拉普拉斯算子
laplacian = cv.Laplacian(img, cv.CV_64F)
laplacian = cv.convertScaleAbs (laplacian)


#3.                        scharri算子
scharrx = cv.Scharr (img, cv.CV_64F,1,0)
scharry = cv.Scharr(img, cv.CV_64F,0,1)
scharrx = cv.convertScaleAbs (scharrx)
scharry = cv.convertScaleAbs (scharry)
scharrxy =cv.addWeighted(scharrx,0.5,scharry,0.5,0)

#------------- 边缘检测
# Canny边缘检测
# 1)使用高斯滤波器，以平滑图像，滤除噪声。
# 2)计算图像中每个像素点的梯度强度和方向。
# 3)应用非极大值(Non-Maximum Suppression）抑制，以消除边缘检测带来的杂散响应。 --- 当前像素点与前后两点的梯度幅值之前的大小比较，保留做大的点。
# 4)应用双阈值(Double-Threshold）检测来确定真实的和潜在的边缘。
# 5)通过抑制孤立的弱边缘最终完成边缘检测。
import myfuntion as mf
import cv2 as cv
import numpy as np
from matplotlib import pyplot as plt

#1.基于canny算子
 
#   80--minvalue   150 --maxvalue 边界的上下限
img=cv.imread('defect1.webp', cv.IMREAD_GRAYSCALE)
v1=cv.Canny(img,80,150)
v2=cv.Canny(img,50,100)
res = np.hstack((v1, v2))
mf.cv_show('res',res)

