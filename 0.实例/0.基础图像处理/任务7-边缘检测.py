import cv2
import numpy as np
import myfunction as mf

#  边缘检测（CannySobel）
# sobel
img2 = cv2.imread('13.png', 0)
edges = cv2.Canny(img2, 30, 50)  # canny边缘检测
mf.cv_show(edges)

# canny
_, thresh = cv2.threshold(img2, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)
edges = cv2.Canny(thresh, 10, 200)
mf.cv_show(edges)

