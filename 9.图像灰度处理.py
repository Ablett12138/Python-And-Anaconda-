#1.=======   mask操作  --- 灰度直方图
#读图像
img = cv.imread('1.png',0)

#创建mask
mask = np. zeros(img.shape[:2],np.uint8)
print(mask.shape)
mask[100:300,100:400] = 255

cv.namedWindow("img",cv.WINDOW_NORMAL)
mf.cv_show( 'img',mask)
mf.cv_show( 'img',img)

#与操作
masked_img = cv.bitwise_and(img,img,mask=mask)
mf.cv_show( 'masked_img',masked_img)

#统计灰度直方图
hist_full = cv.calcHist([img],[0],None,[256],[0,256])
hist_mask = cv.calcHist([img],[0],mask,[256],[0,256])

#显示图像
plt.subplot (221), plt.imshow(img, 'gray')
plt.subplot (222), plt.imshow(mask,'gray')
plt.subplot (223), plt.imshow (masked_img,'gray')
plt.subplot (224),plt.plot(hist_full), plt.plot(hist_mask)
plt.xlim([0,256])
plt.show ()


# 2.====== 图像灰度均衡化  ======灰度均衡化
#0表示灰度图 --绘制灰度直方图
img = cv.imread('1.png', 0)
# plt.hist(img.ravel(),256)
plt.show ()

#图像均衡化
equ = cv.equalizeHist(img)
# plt.hist(equ.ravel(),256)

#显示灰度直方图
plt.subplot (121), plt.hist(img.ravel(),256)
plt.subplot (122), plt.hist(equ.ravel(),256)
plt.show()

#显示图像
plt.subplot (121), plt.imshow(img, 'gray')
plt.subplot (122), plt.imshow(equ,'gray')
plt.show ()