import cv2
import numpy as np

# 回调函数，x表示滑块位置
def nothing(x):
    pass

cv2.namedWindow('image',cv2.WINDOW_NORMAL)
# 创建两个滑动条
cv2.createTrackbar('MAX','image',0,255,nothing)

img = cv2.imread('seed//yumi1.JPG', 0)


while(True):
    max = cv2.getTrackbarPos('MAX','image')
    _,thresh = cv2.threshold(img,max,255,cv2.THRESH_BINARY)
    cv2.imshow('image',thresh)
    if cv2.waitKey(1) == ord('q'):
        break
