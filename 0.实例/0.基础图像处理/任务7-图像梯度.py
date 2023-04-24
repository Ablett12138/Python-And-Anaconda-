import cv2
import numpy as np
import myfunction as mf


img = cv2.imread('shudu.png', 0)
# 自己进行垂直边缘提取
kernel = np.array([[-1, 0, 1],
                   [-2, 0, 2],
                   [-1, 0, 1]], dtype=np.float32)
dst_v = cv2.filter2D(img, -1, kernel)
# 自己进行水平边缘提取
dst_h = cv2.filter2D(img, -1, kernel.T)
# 横向并排对比显示
mf.cv_show(np.hstack((img, dst_v, dst_h)))


# 分别使用sobel对x,y方向进行梯度提取
sobelx = cv2.Sobel(img, -1, 1, 0, ksize=3)  # 只计算x方向
sobely = cv2.Sobel(img, -1, 0, 1, ksize=3)  # 只计算y方向

sobel=cv2.add(sobelx,sobely)
mf.cv_show(sobel)

#拉普拉斯算子
laplacian = cv2.Laplacian(img, -1)  # 使用Laplacian算子

# 两种算法比较
mf.cv_show(np.hstack((img, sobel, laplacian)))