#------------- 包 ---------------------#
import cv2
import numpy as np
from matplotlib import pyplot as plt
import myfunction as mf


# 任务描述
# 用 python 实现如下功能
# （2）模板匹配（大图中找小图）

# 1.最佳模板匹配---只能匹配一个对象
# 模板匹配
img = cv2.imread('lenargb.bmp', 0)
template = cv2.imread('face.png', 0)
h, w = template.shape[:2] # rows->h, cols->w

# 相关系数匹配方法：cv2.TM_CCOEFF
res = cv2.matchTemplate(img, template, cv2.TM_CCOEFF)
min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(res)
left_top = max_loc # 左上角
right_bottom = (left_top[0] + w, left_top[1] + h) # 右下角
cv2.rectangle(img, left_top, right_bottom, 255, 2) # 画出矩形位置
mf.cv_show(img)


# 2.多个模板匹配
# 读入原图和模板
img_rgb = cv2.imread('mario.png')
img_gray = cv2.cvtColor(img_rgb, cv2.COLOR_BGR2GRAY)
template = cv2.imread('mario_coin.png', 0)
h, w = template.shape[:2]
# 标准相关模板匹配
res = cv2.matchTemplate(img_gray, template, cv2.TM_CCOEFF_NORMED)
threshold = 0.8
# 这边是 Python/Numpy 的知识，后面解释
loc = np.where(res >= threshold) # 匹配程度大于%80 的坐标 y,x
for pt in zip(*loc[::-1]): # *号表示可选参数
 right_bottom = (pt[0] + w, pt[1] + h)
 cv2.rectangle(img_rgb, pt, right_bottom, (0, 0, 255), 2)
mf.cv_show(img_rgb)