
#encoding = utf-8
import numpy as np
import cv2
import myfuntion as mf
import matplotlib.pyplot as plt


image = cv2.imread('Japan2.jpg')
image1= cv2.imread('china1.jpg')
image2 = cv2.imread('Japan1.jpg')
image3 = cv2.imread('Vietnam1.jpg')

images=[image,image1,image2,image3]

for i in range(4):
    b,g,r=cv2.split(images[i])
    images[i]=cv2.merge([r,g,b])

# 标题
titles = ['China','Japan', 'Vietnam']
for i in range(3):
    plt.subplot(1,3,i+1),plt.imshow(images[i+1],)
    plt.title(titles[i])
    plt.xticks([]),plt.yticks([])
plt.show()
#化成灰度图像
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
gray1 = cv2.cvtColor(image1, cv2.COLOR_BGR2GRAY)
gray2 = cv2.cvtColor(image2, cv2.COLOR_BGR2GRAY)
gray3 = cv2.cvtColor(image3, cv2.COLOR_BGR2GRAY)

H,W=gray.shape
H1,W1=gray1.shape
H2,W2=gray2.shape
H3,W3=gray3.shape

#创建一个窗口
new_window=cv2.namedWindow("flag")

# #将国旗展示出来
# # 1-3  罗列3幅图片

# titles = ['China','Japan', 'Vietnam']
# images = [gray1,gray2,gray3]
# for i in range(3):
#     plt.subplot(1,3,i+1),plt.imshow(images[i],'gray')
#     plt.title(titles[i])
#     plt.xticks([]),plt.yticks([])
# plt.show()


# THRESH_BINARY的反转   --亮的变暗，暗的变亮
ret,thresh = cv2.threshold(gray,127,255, cv2.THRESH_BINARY_INV)
ret1,thresh1 = cv2.threshold(gray1,127,255, cv2.THRESH_BINARY_INV)
ret2,thresh2 = cv2.threshold(gray2,127,255, cv2.THRESH_BINARY_INV)
ret3,thresh3 = cv2.threshold(gray3,127,255, cv2.THRESH_BINARY_INV)

# images = [thresh1,thresh2,thresh3]

# # 1-3  罗列3幅图片
# for i in range(3):
#     plt.subplot(1,3,i+1),plt.imshow(images[i],'gray')
#     # plt.title(titles[i])
#     plt.xticks([]),plt.yticks([])
# plt.show()

# 计算能量
energy=0
empty=0
for i in range(0,H):
    for j in range(0,W):
        if(thresh[i,j])==255:
            energy=energy+1
        else:
            empty=empty+1
rate=energy/empty

energy=0
empty=0
for i in range(0,H1):
    for j in range(0,W1):
        if(thresh1[i,j])==255:
            energy=energy+1
        else:
            empty=empty+1
rate1=energy/empty

energy=0
empty=0
for i in range(0,H2):
    for j in range(0,W2):
        if(thresh2[i,j])==255:
            energy=energy+1
        else:
            empty=empty+1
rate2=energy/empty


energy=0
empty=0
for i in range(0,H3):
    for j in range(0,W3):
        if(thresh3[i,j])==255:
            energy=energy+1
        else:
            empty=empty+1
rate3=energy/empty


print(rate1 ,rate2 ,rate3)

#计算相关系数求解
if  abs(1-(rate**2+rate1**2)/(2*(rate*rate1)))<0.1:
    plt.subplot(1,1,1),plt.imshow(images[0])
    plt.title(titles[0])
    plt.xticks([]),plt.yticks([])
    plt.show()
    print("china",abs(1-(rate**2+rate1**2)/(2*(rate*rate1))))

elif abs(1-(rate**2+rate2**2)/(2*(rate*rate2)))<0.1:
    plt.subplot(1,1,1),plt.imshow(images[0])
    plt.title(titles[1])
    plt.xticks([]),plt.yticks([])
    plt.show()
    print("japan",abs(1-(rate**2+rate2**2)/(2*(rate*rate2))))

elif abs(1-(rate**2+rate3**2)/(2*(rate*rate3)))<0.1:
    plt.subplot(1,1,1),plt.imshow(images[0])
    plt.title(titles[2])
    plt.xticks([]),plt.yticks([])
    plt.show()
    print("vietnam",abs(1-(rate**2+rate3**2)/(2*(rate*rate3))))
else:
    print("其他国家")
    print("china",abs(1-(rate**2+rate1**2)/(2*(rate*rate1))))
    print("japan",abs(1-(rate**2+rate2**2)/(2*(rate*rate2))))
    print("vietnam",abs(1-(rate**2+rate3**2)/(2*(rate*rate3))))
    

