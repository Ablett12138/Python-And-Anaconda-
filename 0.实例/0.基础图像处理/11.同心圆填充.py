import cv2
import numpy as np
import myfunction as mf

#任务描述：
# 找到3个圆环的内环，然后填充成(180,215,215)这种颜色：

# 图形轮廓绘制
img = cv2.imread('txy.png')
img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
ret, thresh = cv2.threshold(img_gray, 0, 255, cv2.THRESH_BINARY_INV + cv2.THRESH_OTSU)
# 寻找二值化图中的轮廓
contours, hierarchy = cv2.findContours(thresh, cv2.RETR_TREE, cv2.CHAIN_APPROX_NONE)
print(len(contours),hierarchy)  # 8条

# 图像绘制  --绿色  cv2.drawContours(img, contours, i, (0, 255, 0), -1) 其中 -1为轮廓填充
# cv2.drawContours(img, contours, -1, (0, 255, 0), 1)

for i in range(len(contours)):
    _,_,next,_=hierarchy[0][i]
    print(next)
    if next==-1:
        cv2.drawContours(img, contours, i, (180,215,215), -1)
mf.cv_show(img)


