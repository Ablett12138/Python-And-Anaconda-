#------------- 包 ---------------------#
import cv2
import numpy as np
from matplotlib import pyplot as plt
import myfunction as mf

# 任务描述
# （1）计算绘制直方图均衡化

# 1.OpenCV 中直方图计算
# 图像读取
img = cv2.imread('hist.png', 0)
# 绘制方框图
hist = cv2.calcHist([img], [0], None, [256], [0, 256]) 

# 2.Numpy 中直方图计算
hist, bins = np.histogram(img.ravel(), 256, [0, 256]) 
hist = np.bincount(img.ravel(), minlength=256)

# 直方图绘制
plt.hist(img.ravel(), 256, [0, 256])
plt.show()

#plt.plot(hist); plt.show()

# 直方图均衡化
equ=cv2.equalizeHist(img)
cv2.imshow('equalization', np.hstack((img, equ))) # 并排显示
cv2.waitKey(0)


# 自适应均衡化，参数可选
clahe = cv2.createCLAHE(clipLimit=2.0, tileGridSize=(8, 8))
cl1 = clahe.apply(img)
cv2.imshow('equalization', np.hstack((img, cl1))) # 并排显示
cv2.waitKey(0)

# 采用掩码的方式-获取部分直方图
 # 掩码和原始图像具有相同的大小，但是只有俩种像素值：0（背景忽略）、255（前景保留）
mask = np.zeros(img.shape[:2], dtype="uint8")
cv2.rectangle(mask, (0, 0), (200, 200), 255, -1)
# 应用掩码图像
masked = cv2.bitwise_and(img, img, mask=mask)

mf.cv_show(np.hstack((img, masked)))

# 掩码后的直方图
hist = cv2.calcHist([img], [0], mask, [256], [0, 256]) 
plt.plot(hist) 
plt.show()