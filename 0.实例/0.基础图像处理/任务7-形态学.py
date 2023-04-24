
import cv2
import numpy as np
import myfunction as mf

# 任务描述
# (1) 边缘检测（CannySobel）
# (2) 腐蚀与膨胀（形态学操作腐蚀膨胀开运算闭运算）

# 腐蚀与膨胀（形态学操作腐蚀膨胀开运算闭运算）
#  腐蚀
img = cv2.imread('pic.png', 0)
kernel = np.ones((5, 5), np.uint8)
erosion = cv2.erode(img, kernel)  # 腐蚀
mf.cv_show(erosion)

# 膨胀
dilation = cv2.dilate(img, kernel)  # 膨胀
mf.cv_show(dilation)

#开运算
kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (5, 5))  # 定义结构元素
opening = cv2.morphologyEx(img, cv2.MORPH_OPEN, kernel)  # 开运算
mf.cv_show(opening)

#闭运算
closing = cv2.morphologyEx(img, cv2.MORPH_CLOSE, kernel)  # 闭运算
mf.cv_show(closing)

#形态学梯度
img1=cv2.imread('pic1.png')
gradient = cv2.morphologyEx(img1, cv2.MORPH_GRADIENT, kernel)
mf.cv_show(gradient)

##顶帽运算
tophat = cv2.morphologyEx(img1, cv2.MORPH_TOPHAT, kernel)
mf.cv_show(tophat)

## 底帽运算
blackhat = cv2.morphologyEx(img1, cv2.MORPH_BLACKHAT, kernel)
mf.cv_show(blackhat)

