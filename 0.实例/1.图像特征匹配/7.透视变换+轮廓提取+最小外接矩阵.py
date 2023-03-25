import cv2 as cv
import numpy as np
from matplotlib import pyplot as plt
import myfunction as mf
import math
#图片读取
img=cv.imread('distance.jpg')
#   读取图像,转化为灰度值
gray=cv.imread('distance.jpg', cv.IMREAD_GRAYSCALE)
# 计算灰度直方图
hist = cv.calcHist([gray], [0], None, [256], [0, 256])

titles=['gray','histogram']

# # #罗列2幅图片
# plt.subplot(1,2,1),plt.imshow(gray,'gray')
# plt.title(titles[0])
# plt.xticks([]),plt.yticks([])

# plt.subplot(1,2,2),plt.hist(hist.ravel(), 256, [0, 256])
# plt.title(titles[1])
# plt.xticks([]),plt.yticks([])
# plt.show()

#滤波处理
gray = cv.boxFilter(gray,-1,(3,3),normalize=True)
#    阈值分割
ret,thresh = cv.threshold (gray,110,255, cv.THRESH_BINARY)

titles=['filtering','threshold']

# # #罗列2幅图片
# plt.subplot(1,2,1),plt.imshow(gray,'gray')
# plt.title(titles[0])
# plt.xticks([]),plt.yticks([])

# plt.subplot(1,2,2),plt.imshow(thresh,'gray')
# plt.title(titles[1])
# plt.xticks([]),plt.yticks([])
# plt.show()

#寻找轮廓  
# binary==二值,contours==轮廓,hierarchy==层级
contours,hierarchy = cv.findContours(thresh, cv.RETR_TREE, cv.CHAIN_APPROX_NONE)

#传入绘制图像,轮廓,轮廓索引,颜色模式,线条厚度
# #注意需要copy,要不原图会变。。。
## -1==所有  0~.. 按照顺序选择图像
# (0,0,255)==颜色模式

draw_img1 = img.copy()
res = cv.drawContours (draw_img1,contours,-1,(0,0,255),1)

# mf.cv_show(res,mod=None)
hole_contours=[]

extern_contour=[]
#2.图像轮廓特征
for i in range(0,len(contours)):
    cnt=contours[i]
    #轮廓面积
    # print("缺陷1的第",i+1,"个缺陷面积:",cv.contourArea(cnt),'pixel')
    print("第{}个轮廓的面积为：{:.2f}，周长为：{:.2f}".format(i+1,cv.contourArea(cnt),cv.arcLength(cnt,True)))
    if cv.contourArea(cnt)<550:
        hole_contours.append(cnt)
    elif cv.contourArea(cnt)>30000:
        extern_contour=cnt

center=[]
#获取最小外接圆参数
for i in range(0,len(hole_contours)):
    (x, y) , radius = cv.minEnclosingCircle(hole_contours[i])
    center.append((int (x), int(y)))

x1,y1=center[0]
x2,y2=center[1]

disrance=math.sqrt((x1-x2)**2+(y1-y2)**2)
print('<======================================    原图小孔距离    ===============================>')
print("小孔距离为：{:.2f} piexl".format(disrance))

# 画一条线宽为5的蓝色直线，参数2：起点，参数3：终点
cv.line(res, (x1,y1), (x2,y2), (255, 0, 0), 5)
str_distance="distance:{:.2f} piexl".format(disrance)
# 添加文字
font = cv.FONT_HERSHEY_SIMPLEX
cv.putText(res, str_distance, (int((x1+x2)/2), int((y1+y2)/2)), font,
            0.5, (0, 255, 0), 1, lineType=cv.LINE_AA)

mf.cv_show(res,mod=None)

rotRect = cv.minAreaRect(extern_contour) # 返回值 (center(x,y), (width, height), angle of rotation )
# print(rotRect)
rect = cv.boxPoints(rotRect).astype(np.int32)

draw_img2 = img.copy()
warped = mf.four_point_transform(draw_img2,rect.reshape(4,2))
res1=warped.copy()
# mf.cv_show(warped,mod=None)
warped=cv.cvtColor(warped,cv.COLOR_BGR2GRAY)
#滤波处理
warped = cv.boxFilter(warped,-1,(3,3),normalize=True)

#    阈值分割
ret,thresh = cv.threshold (warped,110,255, cv.THRESH_BINARY)

# titles=['filtering','threshold']

# # #罗列2幅图片
# plt.subplot(1,2,1),plt.imshow(warped,'gray')
# plt.title(titles[0])
# plt.xticks([]),plt.yticks([])

# plt.subplot(1,2,2),plt.imshow(thresh,'gray')
# plt.title(titles[1])
# plt.xticks([]),plt.yticks([])
# plt.show()

contours,hierarchy = cv.findContours(thresh, cv.RETR_TREE, cv.CHAIN_APPROX_NONE)
#对找到的轮廓进行排序的操作  -- 取前五个
cnts = sorted(contours, key = cv.contourArea , reverse = True)[:4]
center=[]
#获取最小外接圆参数
for i in range(2,len(cnts)):
    (x, y) , radius = cv.minEnclosingCircle(cnts[i])
    center.append((int (x), int(y)))

x1,y1=center[0]
x2,y2=center[1]

disrance=math.sqrt((x1-x2)**2+(y1-y2)**2)
print('<======================================    透视变换后    ===============================>')
print("透视变换后小孔距离为：{:.2f} piexl".format(disrance))

# 画一条线宽为5的蓝色直线，参数2：起点，参数3：终点
cv.line(res1, (x1,y1), (x2,y2), (255, 0, 0), 5)
str_distance="d:{:.2f} piexl".format(disrance)
# 添加文字
font = cv.FONT_HERSHEY_SIMPLEX
cv.putText(res1, str_distance, (x2-10, int((y1+y2)/2)), font,
            0.4, (0, 255, 0), 1, lineType=cv.LINE_AA)
mf.cv_show(res1,mod=None)