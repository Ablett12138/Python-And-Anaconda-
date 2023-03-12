#------------- 图像金字塔   多层特征提取
 #图片显示
img=cv.imread('1.jpeg')
#1.------- 高斯金字塔
#向上采样
# 像素个数扩大为原来的二倍
up=cv.pyrUp(img)
mf.cv_show(' up',up )
print (up.shape)

#向下采样
# 像素个数缩小为原来的0.5
down=cv.pyrDown(img)
mf.cv_show(' down',down )
print (down.shape)


#2.------- 拉普拉斯金字塔
#先向上取样，再向下取样
#用上一步的结果减去原图
up=cv.pyrUp(img)
up_down=cv.pyrDown(up)
laplace=up_down-img
mf.cv_show('laplac',laplace)