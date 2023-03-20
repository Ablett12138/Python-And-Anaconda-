# cv2.getTrackbarPos() 函数的一个参数是滑动条的名字，第二个参数
# 是滑动条被放置窗口的名字，第三个参数是滑动条的默认位置。第四个参数是
# 滑动条的最大值，第五个函数是回调函数，每次滑动条的滑动都会调用回调函
# 数。回调函数通常都会含有一个默认参数，就是滑动条的位置。

# -*- coding: utf-8 -*-
"""
Created on Sun Jan 5 13:51:34 2014
@author: duan
"""
import cv2
import numpy as np
def default(x):
    print(x)
    
# 创建一副黑色图像
img=np.zeros((300,512,3),np.uint8)
cv2.namedWindow('image',cv2.WINDOW_NORMAL)
cv2.createTrackbar('R','image',128,255,default)
cv2.createTrackbar('G','image',128,255,default)
cv2.createTrackbar('B','image',128,255,default)

while(1):
    r=cv2.getTrackbarPos('R','image')
    g=cv2.getTrackbarPos('G','image')
    b=cv2.getTrackbarPos('B','image')
    if cv2.waitKey(1) & 0xFF == ord('q'):
        print(" keybroads interrupted!!!")
        break

while(1):
    cv2.imshow('image',img)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        print(" keybroads interrupted!!!")
        break
    r=cv2.getTrackbarPos('R','image')
    g=cv2.getTrackbarPos('G','image')
    b=cv2.getTrackbarPos('B','image')
    img[:]=[b,g,r]

cv2.destroyAllWindows()