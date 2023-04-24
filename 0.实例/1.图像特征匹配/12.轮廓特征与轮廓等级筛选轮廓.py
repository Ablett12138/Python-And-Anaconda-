import cv2
import numpy as np
import myfunction as mf
# 任务要求：
# 使用 python 和 opencv 实现寻找绘制轮廓功能

# 图形轮廓绘制
img = cv2.imread('13.png')
img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
ret, thresh = cv2.threshold(img_gray, 0, 255, cv2.THRESH_BINARY_INV + cv2.THRESH_OTSU)
# 寻找二值化图中的轮廓
contours, hierarchy = cv2.findContours(thresh, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
# 图像绘制  --绿色
cv2.drawContours(img, contours, -1, (0, 255, 0), 1)
mf.cv_show(img)

#轮廓层级
# 读入图片
img_hierarchy = cv2.imread('hierarchy.png')
img_hierarchy_gray=cv2.cvtColor(img_hierarchy,cv2.COLOR_BGR2GRAY)
_, thresh = cv2.threshold(img_hierarchy_gray, 0, 255, cv2.THRESH_BINARY+cv2.THRESH_OTSU)
# 1.寻找轮廓---cv2.RETR_TREE
# 它会完整建立轮廓的层级从属关系
contours, hierarchy = cv2.findContours(thresh, cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)
# 绘制轮廓
img_hierarchy1=img_hierarchy.copy()
print(len(contours),hierarchy)  # 8条
cv2.drawContours(img_hierarchy1, contours, -1, (0, 255, 255), 1)
mf.cv_show(img_hierarchy1)

# 2.寻找轮廓---cv2.RETR_LIST
# 这是最简单的一种寻找方式，它不建立轮廓间的子属关系，也就是所有轮廓都属于同一层级。
# 这样的话，hierarchy中的后两个值[First Child, Parent]都为-1。
contours, hierarchy = cv2.findContours(thresh, cv2.RETR_LIST,cv2.CHAIN_APPROX_SIMPLE)
img_hierarchy2=img_hierarchy.copy()
print(len(contours),hierarchy)  # 8条
cv2.drawContours(img_hierarchy2, contours, -1, (255, 255, 0), 1)
mf.cv_show(img_hierarchy2)

# 3.寻找轮廓---cv2.RETR_CCOMP
# 它把所有的轮廓只分为2个层级，不是外层的就是里层的。
contours, hierarchy = cv2.findContours(thresh, cv2.RETR_CCOMP,cv2.CHAIN_APPROX_SIMPLE)
img_hierarchy3=img_hierarchy.copy()
print(len(contours),hierarchy)  # 8条
cv2.drawContours(img_hierarchy3, contours, -1, (0, 255, 0), 1)
mf.cv_show(img_hierarchy3)

# 4.寻找轮廓---cv2.RETR_EXTERNAL
# # 这种方式只寻找最高层级的轮廓，也就是它只会找到前面我们所说的3条0级轮廓：
contours, hierarchy = cv2.findContours(thresh, cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_SIMPLE)
img_hierarchy4=img_hierarchy.copy()
print(len(contours),hierarchy)  # 8条
cv2.drawContours(img_hierarchy4, contours, -1, (255, 0, 255), 1)
mf.cv_show(img_hierarchy4)
