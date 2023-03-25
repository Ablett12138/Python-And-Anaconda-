import cv2
import numpy as np
import matplotlib.pyplot as plt
import myfunction as mf

#任务9 使用 python 实现绘图功能（画线画圆画矩形添加文字）

#1.======================   创建一副黑色的图片  =============================#
# 创建一副黑色的图片
img = np.zeros((512, 512, 3), np.uint8)
# 画一条线宽为5的蓝色直线，参数2：起点，参数3：终点
cv2.line(img, (0, 0), (512, 512), (255, 0, 0), 5)
# 画一个绿色边框的矩形，参数2：左上角坐标，参数3：右下角坐标
cv2.rectangle(img, (384, 0), (510, 128), (0, 255, 0), 3)

# 画圆需要指定圆心和半径，注意下面的例子中线宽=-1代表填充
# 画一个填充红色的圆，参数2：圆心坐标，参数3：半径
cv2.circle(img, (447, 63), 63, (0, 0, 255), -1)

# 在图中心画一个填充的半圆
cv2.ellipse(img, (256, 256), (100, 50), 0, 0, 180, (255, 0, 0), -1)

# OpenCV中需要先将多边形的顶点坐标需要变成顶点数×1×2维的矩阵，再来绘制：
# 定义四个顶点坐标
pts = np.array([[10, 5],  [50, 10], [70, 20], [20, 30]], np.int32)
# 顶点个数：4，矩阵变成4*1*2维
pts = pts.reshape((-1, 1, 2))
cv2.polylines(img, [pts], True, (0, 255, 255))


# 使用cv2.polylines()画多条直线
line1 = np.array([[100, 20],  [150, 20]], np.int32).reshape((-1, 1, 2))
line2 = np.array([[100, 60],  [150, 60]], np.int32).reshape((-1, 1, 2))
line3 = np.array([[100, 100],  [200, 100]], np.int32).reshape((-1, 1, 2))
cv2.polylines(img, [line1, line2, line3], True, (0, 255, 255))


# o	参数2：要添加的文本
# o	参数3：文字的起始坐标（左下角为起点）
# o	参数4：字体
# o	参数5：文字大小（缩放比例）

# 添加文字
font = cv2.FONT_HERSHEY_SIMPLEX
cv2.putText(img, 'Ablett', (10, 500), font,
            4, (255, 255, 255), 2, lineType=cv2.LINE_AA)

mf.cv_show(img)