#------------- 包 ---------------------#
import cv2
import numpy as np
from matplotlib import pyplot as plt
import myfunction as mf
#-------------- 宽和高的概念 -------------#
imageA[H,W]
cv2.warpPerspective(imageA,imageB,(W,H))
image.shape=w,h,c

#-------------- 显示文字 -------------#
font=cv2.FONT_HERSHEY_SIMPLEX
cv2.putText(img,'OpenCV',(10,500), font, 4,(255,255,255),2)

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
plt.plot(hist)
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


##------------- 一种显示图像加直方图的方法
#图像集
images = [img, 0, th1, img, 0, th2, blur, 0, th3]
#标题集
titles = ['Original', 'Histogram', 'Global(v=100)','Original', 'Histogram', "Otsu's",'Gaussian filtered Image', 'Histogram', "Otsu's"]
for i in range(3):
    # 绘制原图
    plt.subplot(3, 3, i*3 + 1)
    plt.imshow(images[i*3], 'gray')
    plt.title(titles[i*3], fontsize=8)
    plt.xticks([]), plt.yticks([])
    # 绘制直方图 plt.hist， ravel 函数将数组降成一维
    plt.subplot(3, 3, i*3 + 2)
    plt.hist(images[i*3].ravel(), 256)
    plt.title(titles[i*3 + 1], fontsize=8)
    plt.xticks([]), plt.yticks([])
    # 绘制阈值图
    plt.subplot(3, 3, i*3 + 3)
    plt.imshow(images[i*3 + 2], 'gray')
    plt.title(titles[i*3 + 2], fontsize=8)
    plt.xticks([]), plt.yticks([])
plt.show()





