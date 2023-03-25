import cv2
import numpy as np
import matplotlib.pyplot as plt
import myfunction as mf

#任务8.使用 python 实现图像几何变换（旋转平移缩放仿射变换透视变换）

#1.======================   图像缩放  =============================#

img=cv2.imread('lenargb.bmp')

# 按照指定的宽度、高度缩放图片
res1 = cv2.resize(img, (200, 200))
# 按照比例缩放，如x,y轴均放大一倍
res2 = cv2.resize(img, None, fx=1, fy=1, interpolation=cv2.INTER_LINEAR)

mf.cv_show(res1,mod=None)
mf.cv_show(res2,mod=None)

#仿射变换
#2.======================   图像平移  =============================#
# 平移图片
rows, cols = img.shape[:2]
# 定义平移矩阵，需要是numpy的float32类型
# x轴平移100，y轴平移50
M = np.float32([[1, 0, rows/2], [0, 1, cols/2]])
# 用仿射变换实现平移
dst = cv2.warpAffine(img, M, (rows, cols))
mf.cv_show(dst,mod=None)


#2.======================   图像旋转  =============================#
# 45°旋转图片并缩小一半
# (cols/2 , rows/2 )=旋转中心 45, 0.5=角度，倍数
M = cv2.getRotationMatrix2D((cols/2 , rows/2 ), 45, 0.5)
dst = cv2.warpAffine(img, M, (cols, rows))
mf.cv_show(dst,mod=None)

#图像翻转
# 其中参数2 = 0：垂直翻转(沿x轴)，参数2 > 0: 水平翻转(沿y轴)，参数2 < 0: 水平垂直翻转
dst = cv2.flip(img, 1)
mf.cv_show(dst,mod=None)

#2.======================   图像任意变换  =============================#
# 变换前的三个点
pts1 = np.float32([[100, 65], [150, 65], [210, 210]])
# 变换后的三个点
pts2 = np.float32([[50, 100], [150, 65], [100, 250]])
# 生成变换矩阵
M = cv2.getAffineTransform(pts1, pts2)
img1=cv2.cvtColor(img,cv2.COLOR_BGR2RGB)
dst = cv2.warpAffine(img1, M, (cols, rows))
plt.subplot(121), plt.imshow(img1), plt.title('input')
plt.xticks([]),plt.yticks([])
plt.subplot(122), plt.imshow(dst), plt.title('output')
plt.xticks([]),plt.yticks([])
plt.show()

