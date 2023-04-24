import cv2
import numpy as np
import matplotlib.pyplot as plt
import myfunction as mf


#任务要求：使用 python 实现平滑图像（卷积滤波模糊降噪）

#--------------------------    滤波小技巧    ----------------------#
# 在不知道用什么滤波器好的时候，优先高斯滤波cv2.GaussianBlur()，然后均值滤波cv2.blur()。
# 斑点和椒盐噪声优先使用中值滤波cv2.medianBlur()。
# 要去除噪点的同时尽可能保留更多的边缘信息，使用双边滤波cv2.bilateralFilter()。
# 线性滤波方式：均值滤波、方框滤波、高斯滤波（速度相对快）。
# 非线性滤波方式：中值滤波、双边滤波（速度相对慢）。

#1. 均值滤波
img = cv2.imread('lenargb.png')
blur = cv2.blur(img, (3, 3))  # 均值模糊
tmp = np.hstack((img, blur))


#2. 方框滤波实现：normalize=True
box = cv2.boxFilter(img, -1, (3, 3), normalize=True)
tmp = np.hstack((tmp, box))

# 3.高斯滤波
# 参数 3 σx 值越大，模糊效果越明显。
# 高斯滤波相比均值滤波效率要慢，但可以有效消除高斯噪声，能保留更多的图像细节，所以经常被称为最有用的滤波器。
# 均值滤波与高斯滤波的对比结果如下（均值滤波丢失的细节更多）：
blur = cv2.blur(img, (5, 5))  # 均值滤波
gaussian = cv2.GaussianBlur(img, (5, 5), 3)  # 高斯滤波
tmp = np.hstack((tmp, gaussian))
mf.cv_show(tmp)

# 4.中值滤波
img = cv2.imread('salt_noise.png', 0)
# 均值滤波 vs 中值滤波
blur = cv2.blur(img, (5, 5))  # 均值滤波
median = cv2.medianBlur(img, 5)  # 中值滤波
tmp = np.hstack((img,blur, median))
mf.cv_show(tmp)

# 5.双边滤波
# 模糊操作基本都会损失掉图像细节信息，尤其前面介绍的线性滤波器，图像的边缘信息很难保留下来。
# 然而，边缘（edge）信息是图像中很重要的一个特征，所以这才有了双边滤波。
# 用cv2.bilateralFilter()函数实现：
img = cv2.imread('lenargb.png')
# 双边滤波 vs 高斯滤波
gau = cv2.GaussianBlur(img, (5, 5), 0)  # 高斯滤波
blur = cv2.bilateralFilter(img, 9, 75, 75)  # 双边滤波
tmp = np.hstack((img,gau, blur))
mf.cv_show(tmp)


# 6. 卷积基础与图像边框
    # 1.固定零边框
img = cv2.imread('opencv.png', 0)
print(img)
# 固定值边框，统一都填充 0 也称为 zero padding
cons = cv2.copyMakeBorder(img, 1, 1, 1, 1, cv2.BORDER_CONSTANT, value=0)
print(cons)
# mf.cv_show(cons)

    # 2.默认对称边框
# 一般情况下默认方式更加合理，因为边界的像素值更加接近。具体应视场合而定。
default = cv2.copyMakeBorder(img, 1, 1, 1, 1, cv2.BORDER_DEFAULT)
print(default)
# mf.cv_show(default)
    # 3.图像卷积
# 定义卷积核
kernel = np.ones((3, 3), np.float32) / 10
# 卷积操作，-1 表示通道数与原图相同
dst1 = cv2.filter2D(default, -1, kernel)

dst2 = cv2.filter2D(cons, -1, kernel)


dst1=cv2.cvtColor(dst1,cv2.COLOR_BGR2RGB)
dst2=cv2.cvtColor(dst2,cv2.COLOR_BGR2RGB)
img=cv2.cvtColor(img,cv2.COLOR_BGR2RGB)

imgs=[img,dst1,dst2]

titles=['origin','constant','symmetrical']
mf.cv_show_multiple_imgs(imgs,titles)

