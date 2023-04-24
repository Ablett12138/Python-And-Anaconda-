import cv2
import numpy as np
import myfunction as mf

#任务要求
# o	计算物体的周长、面积、质心、最小外接矩形等
# o	OpenCV函数：cv2.contourArea(), cv2.arcLength(), cv2.approxPolyDP() 等

# 图形轮廓绘制
img = cv2.imread('13.png')
img_color=img.copy()
img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
ret, thresh = cv2.threshold(img_gray, 0, 255, cv2.THRESH_BINARY_INV + cv2.THRESH_OTSU)
# 寻找二值化图中的轮廓
contours, hierarchy = cv2.findContours(thresh, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
# 图像绘制  --绿色
cv2.drawContours(img_color, contours, 0, (0, 255, 0), 1)
# 获取图形面积和周长
print('图像面积为:{:.2f}'.format(cv2.contourArea(contours[0])))
print('图像周长为:{:.2f}'.format(cv2.arcLength(contours[0],True)))


# 图像质心计算
M=cv2.moments(img_gray)
x,y=M['m10'] / M['m00'], M['m01'] / M['m00']
print('图像质心为(x,y):({:.2f} , {:.2f})'.format(x,y))

# 外接拒与最小外接矩
img_color1=img.copy()
x, y, w, h = cv2.boundingRect(contours[0])  # 外接矩形
cv2.rectangle(img_color1, (x, y), (x + w, y + h), (0, 255, 0), 2)

rect = cv2.minAreaRect(contours[0])         # 最小外接矩形

# cv2.boxPoints(rect).astype(np.int_)强制类型转换
box =cv2.boxPoints(rect).astype(np.int_)    # 矩形的四个角点取整

print(box)
cv2.drawContours(img_color1, [box], -1, (255, 0, 0), 2)

mf.cv_show(img_color1)

# 最小外接圆
img_color2=img.copy()
(x, y), radius = cv2.minEnclosingCircle(contours[0])
(x, y, radius) = np.int32((x, y, radius))  # 圆心和半径取整
cv2.circle(img_color2, (x, y), radius, (0, 0, 255), 2)

# 最小外接椭圆
ellipse = cv2.fitEllipse(contours[0])
cv2.ellipse(img_color2, ellipse, (255, 255, 0), 2)
mf.cv_show(img_color2)

img = cv2.imread('xzpp.png', 0)
_, thresh = cv2.threshold(img, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)
contours, hierarchy = cv2.findContours(thresh,cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
img_color = cv2.cvtColor(thresh, cv2.COLOR_GRAY2BGR)  # 用于绘制的彩色图
mf.cv_show(img_color)

# 轮廓特征计算
cnt_a, cnt_b, cnt_c = contours[0], contours[1], contours[2]
print(cv2.matchShapes(cnt_b, cnt_b, 1, 0.0))  
print(cv2.matchShapes(cnt_b, cnt_c, 1, 0.0))  
print(cv2.matchShapes(cnt_b, cnt_a, 1, 0.0)) 