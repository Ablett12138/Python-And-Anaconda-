#encoding = utf-8
import numpy as np
import cv2
import myfunction as mf
import matplotlib.pyplot as plt

#读取输入
image = cv2.imread("1.jpg")
#坐标也会相同变化  --height变化500倍
ratio = image.shape[0]/ 500.0
orig = image.copy()

image = mf.cv_image_resize(orig, height = 500)


#预处理
gray = cv2.cvtColor ( image,cv2.COLOR_BGR2GRAY)


titles=['orgin','gray']
#罗列2幅图片
plt.subplot(1,2,1),plt.imshow(image,'gray')
plt.title(titles[0])
plt.xticks([]),plt.yticks([])

plt.subplot(1,2,2),plt.imshow(gray,'gray')
plt.title(titles[1])
plt.xticks([]),plt.yticks([])
# plt.show()

#绘制直方图
plt.hist(gray.ravel(), 256, [0, 256])
# plt.show()

#阈值分割
ret1,thresh1 = cv2.threshold (gray,147,255, cv2.THRESH_BINARY)


#滤波
gray =cv2.GaussianBlur(gray,(5,5),0)

#阈值分割
ret1,thresh1 = cv2.threshold (gray,176,255, cv2.THRESH_BINARY)

kernel2 = np.ones ((4,4), np.uint8)
opening2 = cv2.morphologyEx(thresh1,cv2.MORPH_OPEN, kernel2)

mf.cv_show("edge",opening2)

edged = cv2.Canny(opening2,174, 178)


#展示预处理结果
print( "STEP 1:边缘检测")
# cv2.imshow( "Image", image)
# cv2.imshow( "Edged", edged)
# cv2.waitKey(0)
# cv2.destroyAllWindows()
mf.cv_show("edge",edged)



#轮廓检测
#最外面的轮廓最大 
cnts = cv2.findContours(edged.copy(),cv2.RETR_LIST,cv2.CHAIN_APPROX_SIMPLE)[0]
#对找到的轮廓进行排序的操作  -- 取前五个
cnts = sorted(cnts, key = cv2.contourArea , reverse = True)[:5]
print(len(cnts))

#遍历轮廓
for c in cnts:
    #计算轮廓近似
    peri = cv2.arcLength(c,True)
    #C表示输入的点集
    # epsilon表示从原始轮廓到近似轮廓的最大距离,它是一个准确度参数
    # #True表示封闭的
    ## 0.02*peri==》近似轮廓的精度控制---越小越接近原图
    approx = cv2.approxPolyDP(c, 0.02*peri,True)


    #4个点的时候就拿出来
    print(len(approx))
    if len(approx) ==4:
        screenCnt = approx
        break

#展示结果
print( "STEP 2:获取轮廊")
cv2.drawContours( image,[screenCnt],-1,(0,255,0),2)
mf.cv_show("image",image)


#透视变换T   
# screenCnt.reshape(4,2)<======>表示四个点坐标,每个点都是x*y 
# 所以是4*2  
# * ratio进行轮廓还原
print(screenCnt.reshape(4,2))
warped = mf.four_point_transform(orig,screenCnt.reshape(4,2) * ratio)


#二值处理
warped = cv2.cvtColor(warped,cv2.COLOR_BGR2GRAY)
ref = cv2.threshold(warped,180,255,cv2.THRESH_BINARY)[1]
cv2.imwrite( 'scan.jpg ' , ref)
#展示结果
print( "STEP 3:变换")
cv2.namedWindow('image',cv2.WINDOW_NORMAL)
res =np.hstack((mf.cv_image_resize(gray,height=500), mf.cv_image_resize(ref,height=500)))
mf.cv_show ('image',res)




