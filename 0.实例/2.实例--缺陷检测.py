
import cv2 as cv
import numpy as np
from matplotlib import pyplot as plt
import myfunction as mf

#1.图像轮廓检测
img1=cv.imread('defect1.png')
img2=cv.imread('defect2.png')
#   读取图像,转化为灰度值
gray1=cv.imread('defect1.png', cv.IMREAD_GRAYSCALE)
gray2=cv.imread('defect2.png', cv.IMREAD_GRAYSCALE)

# cv.namedWindow("defect1",cv.WINDOW_NORMAL)
titles=['defct1','defect2']
#罗列2幅图片
plt.subplot(1,2,1),plt.imshow(gray1,'gray')
plt.title(titles[0])
plt.xticks([]),plt.yticks([])

plt.subplot(1,2,2),plt.imshow(gray2,'gray')
plt.title(titles[1])
plt.xticks([]),plt.yticks([])

plt.show()

#绘制灰度直方图
# 计算灰度直方图
hist1 = cv.calcHist([gray1], [0], None, [256], [0, 256])
hist2 = cv.calcHist([gray2], [0], None, [256], [0, 256])

#罗列2幅图片
plt.subplot(1,2,1),plt.hist(gray1.ravel(), 256, [0, 256])
plt.title(titles[0])
plt.xticks([]),plt.yticks([])

plt.subplot(1,2,2),plt.hist(gray2.ravel(), 256, [0, 256])
plt.title(titles[1])
plt.xticks([]),plt.yticks([])
plt.show()

#滤波处理
gray1 = cv.boxFilter(gray1,-1,(3,3),normalize=True)

gray2 = cv.boxFilter(gray2,-1,(3,3),normalize=True)


# #图像处理
kernel1 = np.ones ((5,5), np.uint8)
gray1 = cv.dilate(gray1, kernel1,iterations = 1)
kernel1 = np.ones ((5,5), np.uint8)
erosion1 = cv.erode(gray1, kernel1,iterations = 1)


kernel2 = np.ones ((5,5), np.uint8)
opening2 = cv.morphologyEx(gray2,cv.MORPH_OPEN, kernel2)

#    阈值分割
ret1,thresh1 = cv.threshold (erosion1,147,255, cv.THRESH_BINARY)
ret2,thresh2 = cv.threshold (opening2,138,255, cv.THRESH_BINARY)


#罗列2幅图片
plt.subplot(1,2,1),plt.imshow(thresh1,'gray')
plt.title(titles[0])
plt.xticks([]),plt.yticks([])

plt.subplot(1,2,2),plt.imshow(thresh2,'gray')
plt.title(titles[1])
plt.xticks([]),plt.yticks([])
plt.show()

#寻找轮廓  
# binary==二值,contours==轮廓,hierarchy==层级
contours1,hierarchy1 = cv.findContours(thresh1, cv.RETR_TREE, cv.CHAIN_APPROX_NONE)
contours2,hierarchy2 = cv.findContours(thresh2, cv.RETR_TREE, cv.CHAIN_APPROX_NONE)


#传入绘制图像,轮廓,轮廓索引,颜色模式,线条厚度
# #注意需要copy,要不原图会变。。。
## -1==所有  0~.. 按照顺序选择图像
# (0,0,255)==颜色模式

draw_img1 = img1.copy()
res = cv.drawContours (draw_img1,contours1,0,(0,0,255),1)
res = cv.drawContours (draw_img1,contours1,1,(255,0,0),1)



draw_img2 = img2.copy()
res = cv.drawContours (draw_img2,contours2,1,(0,0,255),1)
res = cv.drawContours (draw_img2,contours2,2,(255,0,0),1)

#罗列2幅图片
plt.subplot(1,2,1),plt.imshow(draw_img1,'gray')
plt.title(titles[0])
plt.xticks([]),plt.yticks([])

plt.subplot(1,2,2),plt.imshow(draw_img2,'gray')
plt.title(titles[1])
plt.xticks([]),plt.yticks([])
plt.show()
print("<========================= 缺陷1 ============================>")
#2.图像轮廓特征
for i in range(0,2):
    cnt=contours1[i]
    #轮廓面积
    print("缺陷1的第",i+1,"个缺陷面积:",cv.contourArea(cnt),'pixel')
    #轮廓周长
    #周长,True表示闭合的
    print("缺陷1的第",i+1,"个缺陷周长:",cv.arcLength(cnt, True))
print("<========================= 缺陷2 ============================>")

for i in range(1,3):
    cnt=contours2[i]
    #轮廓面积
    print("缺陷2的第",i,"个缺陷面积:",cv.contourArea(cnt),'pixel')
    #轮廓周长
    #周长,True表示闭合的
    print("缺陷2的第",i,"个缺陷周长:",cv.arcLength(cnt, True))