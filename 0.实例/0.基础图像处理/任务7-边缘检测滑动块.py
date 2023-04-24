import cv2
import numpy as np

# 回调函数，x表示滑块位置
def nothing(x):
    pass

cv2.namedWindow('image')
# 创建两个滑动条
cv2.createTrackbar('MAX','image',0,1500,nothing)
cv2.createTrackbar('MIN','image',0,1500,nothing)

img = cv2.imread('shudu.png', 0)
#对比度增强  
img_bright = cv2.convertScaleAbs(img,alpha=2.7,beta=0)

while(True):
    max = cv2.getTrackbarPos('MAX','image')
    min = cv2.getTrackbarPos('MIN','image')
    _,thresh = cv2.threshold(img_bright,0,255,cv2.THRESH_BINARY + cv2.THRESH_OTSU)
    edges = cv2.Canny(thresh,min,max)
    cv2.imshow('image',edges)
    if cv2.waitKey(1) == ord('q'):
        break




