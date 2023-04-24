import cv2
import numpy as np
from matplotlib import pyplot as plt
import myfunction as mf

# 任务描述
# （3）霍夫变换（提取直线圆
# o 参数 1：要检测的二值图（一般是阈值分割或边缘检测后的图）
# o 参数 2：距离 r 的精度，值越大，考虑越多的线
# o 参数 3：角度 θ 的精度，值越小，考虑越多的线
# o 参数 4：累加数阈值，值越小，考虑越多的线


# 1.检测直线
# 加载图片，转为二值图
img = cv2.imread('shape.png')
drawing = np.zeros(img.shape[:], dtype=np.uint8)

gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
ret,thresh = cv2.threshold(gray,60,255, cv2.THRESH_BINARY)

# mf.cv_show(thresh)

edges = cv2.Canny(thresh, 50, 70)

# 霍夫直线变换
lines = cv2.HoughLines(edges, 0.8, np.pi / 180, 90)

# 将检测的线画出来（注意是极坐标）
for line in lines:
    rho, theta = line[0]
    a = np.cos(theta)
    b = np.sin(theta)
    x0 = a * rho
    y0 = b * rho
    x1 = int(x0 + 1000 * (-b))
    y1 = int(y0 + 1000 * (a))
    x2 = int(x0 - 1000 * (-b))
    y2 = int(y0 - 1000 * (a))
    cv2.line(drawing, (x1, y1), (x2, y2), (0, 0, 255))
    
mf.cv_show(drawing)
 
# 2.概率霍夫直线变换
drawing = np.zeros(img.shape[:], dtype=np.uint8)
# 3.统计概率霍夫线变换
lines = cv2.HoughLinesP(edges, 0.8, np.pi / 180, 90,
 minLineLength=50, maxLineGap=10)

# 3.将检测的线画出来
for line in lines:
 x1, y1, x2, y2 = line[0]
 cv2.line(drawing, (x1, y1), (x2, y2), (0, 255, 0), 1, lineType=cv2.LINE_AA)
mf.cv_show(drawing)

# 3.霍夫圆变换
# o 参数 2：变换方法，一般使用霍夫梯度法，详情：HoughModes
# o 参数 3 dp=1：表示霍夫梯度法中累加器图像的分辨率与原图一致
# o 参数 4：两个不同圆圆心的最短距离
# o 参数 5：param2 跟霍夫直线变换中的累加数阈值一样

drawing = np.zeros(img.shape[:], dtype=np.uint8)
# 2.霍夫圆变换
# param2=20  ===> 找不到圆就修改击中次数
circles = cv2.HoughCircles(edges, cv2.HOUGH_GRADIENT, 1, 20, param2=20)
circles = np.uint8(circles)
# 将检测的圆画出来
for i in circles[0, :]:
    cv2.circle(drawing, (i[0], i[1]), i[2], (0, 255, 0), 2) # 画出外圆
    cv2.circle(drawing, (i[0], i[1]), 2, (0, 0, 255), 3) # 画出圆心
mf.cv_show(drawing)