import cv2
import numpy as np
import matplotlib.pyplot as plt
import myfunction as mf

# 任务要求：使用 python 实现图像混合（算数运算混合按位运算）
## 图像混合   ---按照权重混合
img1 = cv2.imread('lenargb.png')
img2 = cv2.imread('opencv.png')

img1 = cv2.resize(img1, (200, 200))
img2 = cv2.resize(img2, (200, 200))

res = cv2.addWeighted(img1, 0.6, img2, 0.4, 0)

mf.cv_show(res)


## 图像混合   ---按位操作包括按位与/或/非/异或操作
# o	cv2.bitwise_and(), cv2.bitwise_not(), cv2.bitwise_or(), cv2.bitwise_xor()
#分别执行按位与/或/非/异或运算。掩膜就是用来对图片进行全局或局部的遮挡


img2 = cv2.resize(img2, (100, 100))
# 把logo放在左上角，所以我们只关心这一块区域
rows, cols = img2.shape[:2]
ROI = img1[:rows, :cols]
# 创建掩膜
img2gray = cv2.cvtColor(img2, cv2.COLOR_BGR2GRAY)
ret, mask = cv2.threshold(img2gray, 250, 255, cv2.THRESH_BINARY)
# mf.cv_show(mask)
# 将掩码取反
mask_inv = cv2.bitwise_not(mask)
# mf.cv_show(mask_inv)

# 保留除logo外的背景
img1_bg = cv2.bitwise_and(ROI, ROI, mask=mask)
# mf.cv_show(img1_bg)

# 将logo切出来
img2 = cv2.bitwise_and(img2,img2,mask=mask_inv)

dst=cv2.add(img2,img1_bg)
# mf.cv_show(dst)
img1[:rows, :cols] = dst  # 融合后放在原图上
mf.cv_show(img1)



## 图像对比度调整   
res1 = np.uint8(np.clip((1.5 * img1 + 10), 0, 255))
tmp = np.hstack((img1, res1))  # 两张图片横向合并（便于对比显示）

mf.cv_show(tmp)