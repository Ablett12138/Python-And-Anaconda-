#------------- 包 ---------------------#
import cv2
import numpy as np
from matplotlib import pyplot as plt

#------------- 1.OpenCV的顺序为B->G->R  ---------------------#
#------------- 灰度转换 ---------------------#
image = cv2.imread('china.jpg')
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

#------------- 创建一个窗口 ---------------------#
new_window=cv2.namedWindow("myflag")
#------------- 在窗口显示图片
cv2.imshow(new_window,image)

#------------- 保存灰度国旗 ---------------------#
cv2.imwrite("gray_flag.jpg",gray)

#------------- 将图像分割成：r,g,b三张,并显示 ---------------------#
b,g,r=cv2.split(image)
#-------------  融合
cv2.merge([b,g,r])
cv2.imshow(new_window,b)
cv2.waitKey(-1)
cv2.imshow(new_window,g)
cv2.waitKey(-1)
cv2.imshow(new_window,r)


#------------- 将图像分割成：r,g,b三张,融合 ---------------------#
image=cv2.merge((b,g,r))

#------------- 延时 ---------------------#
cv2.waitKey(-1)

#------------- 图像大小 ---------------------#
imge.shape

#------------- 边界填充 ---------------------#
#             填充大小
top_size, bottom_size,left_size,right_size = (50,50,50,50)
#             复制法，也就是复制最边缘像素。
replicate = cv2.copyMakeBorder(image,top_size, bottom_size,left_size,right_size, borderType=cv2.BORDER_REPLICATE)
#             反射法，对感兴趣的图像中的像素在两边进行复制，fedcba|abcdefgh|hgfedcb
reflect = cv2.copyMakeBorder(image,top_size, bottom_size,left_size,right_size, cv2. BORDER_REFLECT)
#             反射法，也就是以最边缘像素为轴，对称， gfedcb|abcdefgh|gfedcba
reflect101 = cv2.copyMakeBorder(image, top_size, bottom_size,left_size,right_size,cv2.BORDER_REFLECT_101)
#             外包装法 cdefgh|abcdefgh|abcdefg
wrap = cv2.copyMakeBorder(image,top_size,bottom_size,left_size,right_size,cv2.BORDER_WRAP)
#             常量法，灰度常数值填充。 
constant = cv2.copyMakeBorder(image,top_size,bottom_size,left_size,right_size, cv2.BORDER_CONSTANT,value=0)
#             显示
mf.cv_show(new_window,replicate)
mf.cv_show(new_window,reflect)
mf.cv_show(new_window,reflect101)
mf.cv_show(new_window,wrap)
mf.cv_show(new_window,constant)

#------------- 改变图像大小   column,row
image_change_size=cv2.resize(image,(1000,400))
print(image_change_size.shape)
mf.cv_show(new_window,image_change_size)


#------------- 改变图像大小   x=column,y=row 倍数版本
image_change_size=cv2.resize(image,(0,0),fx=1,fy=1)
mf.cv_show(new_window,image_change_size)

#------------- 图像按权重叠加   x=column,y=row 
res=cv2.addWeighted(image,0.6,image1,0.4,0)

#------------- 图像阈值处理
# 灰度直方图
# 读取灰度图像
img = cv2.imread('image.jpg', 0)
# 计算灰度直方图
hist = cv2.calcHist([img], [0], None, [256], [0, 256])
# 显示灰度直方图
plt.hist(img.ravel(), 256, [0, 256])
plt.show()


# 超过阈值部分取maxval(最大值),否则取0. 
ret,thresh1 = cv2.threshold(gray,127,255, cv2.THRESH_BINARY)
# THRESH_BINARY的反转  --亮的变暗，暗的变亮
ret,thresh2 = cv2.threshold(gray,127,255, cv2.THRESH_BINARY_INV)
# 大于阈值部分设为阈值,否则不变.
ret,thresh3 = cv2.threshold(gray,127,255, cv2.THRESH_TRUNC)
#大于阈值部分不改变,否则设为0.
ret,thresh4 = cv2.threshold(gray,127,255, cv2.THRESH_TOZERO)
#THRESH_TOZERO的反转
ret,thresh5 = cv2.threshold(gray,127,255, cv2.THRESH_TOZERO_INV)

titles = ['Original Image','BINARY', 'BINARY_INV', 'TRUNC', 'TOZERO','TOZERO_INV']
images = [gray,thresh1,thresh2,thresh3,thresh4,thresh5]

# 1-5  罗列6幅图片
for i in range(6):
    plt.subplot(2,3,i+1),plt.imshow(images[i],'gray')
    plt.title(titles[i])
    plt.xticks([]),plt.yticks([])
plt.show()


#------------- 拼接显示所有图像
#展示所有的     (blur, aussian, median)--图像名称
all_win=cv.namedWindow ('all',cv.WINDOW_NORMAL)
res =np.hstack((blur, aussian, median))
mf.cv_show ('all',res)



#------------- 图像平滑处理
#1.均值滤波
#简单的平均卷积操作   
#选取区域为3X3 与 3X3的全为1的矩阵做卷积
blur = cv.blur(img,(3,3))
# mf.cv_show ('blur',blur)

#方框滤波
#基本和均值一样,可以选择归一化,不容易越界
box = cv.boxFilter(img,-1,(3,3),normalize=True)

#2. 中值滤波
#相当于用中值代替  相当于取5X5的矩阵排序求中值
median = cv.medianBlur(img,5)#中值滤波


#3.高斯滤波
#高斯模糊的卷积核里的数值是满足高斯分布，相当于更重视中间的值
gaussian = cv. GaussianBlur(img,(5,5),2)

#4.腐蚀操作  
# iterations==迭代次数  ones((5,5)--腐蚀图像
kernel = np.ones((5,5) , np.uint8)
erosion = cv.erode(img, kernel,iterations = 1)

#5.膨胀操作  
# iterations==迭代次数  ones((5,5)--腐蚀图像
kernel = np.ones((3,3), np.uint8)
dilate = cv.dilate(img, kernel,iterations = 1)

#6.开运算   先腐蚀后膨胀   
# morphologyEx---形态学函数  
# 去除毛刺
kernel = np.ones ((5,5), np.uint8)
opening = cv.morphologyEx(img,cv.MORPH_OPEN, kernel)

#7.闭运算   先膨胀后腐蚀   
# morphologyEx---形态学函数
# 坑洼图像平滑
kernel = np.ones ((5,5), np.uint8)
closing = cv.morphologyEx(img,cv.MORPH_CLOSE,kernel)

#8.梯度运算  
# 求取边界
gradient = cv.morphologyEx(img,cv.MORPH_GRADIENT,kernel)

#9.顶帽运算
# 顶帽=原始输入-开运算结果
# 只剩下毛刺
tophat = cv.morphologyEx(img,cv.MORPH_TOPHAT,kernel)

#10. 底帽运算
# 底帽=闭运算-原始输入
# 去除毛刺
blackhat = cv.morphologyEx(img, cv.MORPH_BLACKHAT,kernel)

#展示所有的图像     
# (blur, gaussian, median)--图像名称
all_win=cv.namedWindow ('all',cv.WINDOW_NORMAL)
res =np.hstack((blur, gaussian, median,erosion,dilate))
mf.cv_show ('all',res)

res1 =np.hstack((opening,closing,gradient))
mf.cv_show ('all',res1)

res1 =np.hstack((tophat,blackhat))
mf.cv_show ('all',res1)

#------------- 图像梯度
#1.                     图像梯度-Sobel算子
#右减左 下减上   
# cv.CV_64F====能表示负数形式
# . ddepth:图像的深度
# ·dx=1和dy=0分别表示水平和竖直方向
# . ksize是Sobel算子的大小
# 水平方向
sobelx = cv.Sobel(img, cv.CV_64F,1,0,ksize=3)
#对求取的梯度求绝对值
sobelx = cv.convertScaleAbs (sobelx)

# 竖直方向
sobely = cv.Sobel(img, cv.CV_64F,0,1,ksize=3)
#对求取的梯度求绝对值
sobely = cv.convertScaleAbs (sobely)

#求和
#0 为偏置项
sobelxy = cv.addWeighted(sobelx, 0.5,sobely,0.5,0)


#2.                        拉普拉斯算子
laplacian = cv.Laplacian(img, cv.CV_64F)
laplacian = cv.convertScaleAbs (laplacian)


#3.                        scharri算子
scharrx = cv.Scharr (img, cv.CV_64F,1,0)
scharry = cv.Scharr(img, cv.CV_64F,0,1)
scharrx = cv.convertScaleAbs (scharrx)
scharry = cv.convertScaleAbs (scharry)
scharrxy =cv.addWeighted(scharrx,0.5,scharry,0.5,0)


