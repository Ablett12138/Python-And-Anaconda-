#------------- 暴力匹配 ---------------#
#------------- 包 ---------------------#
import cv2
import numpy as np
from matplotlib import pyplot as plt
import myfunction as mf

#图像读取
img1=cv2.imread('feature_matching.png')
img2=cv2.imread('feature_matchings.png')

# #灰度化处理
# gray1=cv2.cvtColor(img1,cv2.COLOR_BGR2GRAY)
# gray2=cv2.cvtColor(img2,cv2.COLOR_BGR2GRAY)

# 创建sift
sift = cv2.SIFT_create()

#得到关键点
kp1,des1 = sift.detectAndCompute(img1,None)
kp2,des2 = sift.detectAndCompute(img2,None)

# crossCheck表示两个特征点要互相匹,
# 例如A中的第i个特征点与B中的第j个特征点最近的,并且B中的第j个特征点到A中的第i个特征点也是
# #NORM_L2:归一化数组的(欧几里德距离),如果其他特征计算方法需要考虑不同的匹配计算方式
# 暴力匹配
bf = cv2.BFMatcher(crossCheck=True)

#-------------------------   1对1匹配   --------------------------#
matches = bf.match(des1,des2)
matches = sorted (matches,key=lambda x: x.distance)

# 获得匹配图像
img3 = cv2.drawMatches(img1,kp1,img2,kp2,matches[: 10],None,flags=2)
mf.cv_show(img3,cv2.WINDOW_NORMAL)

#-------------------------   k对最佳匹配   --------------------------#
bf = cv2.BFMatcher()
matches = bf.knnMatch(des1,des2,k=2)

good = []
for m, n in matches:
    if m.distance< 0.75*n.distance:
        good.append([m])

img4 = cv2.drawMatchesKnn(img1, kp1,img2, kp2,good,None,flags=2)
mf.cv_show(img4,cv2.WINDOW_NORMAL)