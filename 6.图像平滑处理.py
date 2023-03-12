

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
