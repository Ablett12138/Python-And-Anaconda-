import cv2
import numpy as np
import myfunction as mf

#任务要求
# 1.对手写字符图片中的数字3和1进行轮廓特征计算
# 2.（选做）用形状匹配比较两个字母或数字


# 1.数字形状特征计算
img = cv2.imread('13.png', 0)
_, thresh = cv2.threshold(img, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)
contours, hierarchy = cv2.findContours(thresh,cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

# 轮廓特征计算
cnt_a, cnt_b = contours[0], contours[1]
print('手写数字1和1的形状匹配:{:.2f}'.format(cv2.matchShapes(cnt_b, cnt_b, 1, 0.0)))  
print('手写数字1和3的形状匹配:{:.2f}'.format(cv2.matchShapes(cnt_b, cnt_a, 1, 0.0))) 


# 2.字母形状特征计算
img = cv2.imread('zm.png', 0)
_, thresh = cv2.threshold(img, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)
contours, hierarchy = cv2.findContours(thresh,cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
img_color = cv2.cvtColor(thresh, cv2.COLOR_GRAY2BGR)  # 用于绘制的彩色图

# 找到字母A和B
for i in range(len(contours)):
    _,_,next,_=hierarchy[0][i]
    # print(hierarchy[0][i])
    if next==1:
        cnt_a=contours[i]
        cv2.drawContours(img_color,contours,i,(0,255,255),3)
    elif next ==4:
        cnt_b=contours[i]
        cv2.drawContours(img_color,contours,i,(255,0,255),3)

# 轮廓特征计算
print('字母A和B的形状匹配:{:.2f}'.format(cv2.matchShapes(cnt_b, cnt_b, 1, 0.0)))  
print('字母A和A的形状匹配:{:.2f}'.format(cv2.matchShapes(cnt_b, cnt_a, 1, 0.0))) 

mf.cv_show(img_color)