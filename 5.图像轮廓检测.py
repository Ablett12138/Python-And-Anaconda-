#------------- 图像轮廓检测
#1.图像轮廓检测
#   读取图像,转化为灰度值
gray=cv.imread('defect1.webp', cv.IMREAD_GRAYSCALE)
#    阈值分割
ret,thresh = cv.threshold (gray,120,255, cv.THRESH_BINARY)
mf.cv_show( 'thresh',thresh)

#寻找轮廓  
# binary==二值,contours==轮廓,hierarchy==层级
contours,hierarchy = cv.findContours(thresh, cv.RETR_TREE, cv.CHAIN_APPROX_NONE)

#传入绘制图像,轮廓,轮廓索引,颜色模式,线条厚度
# #注意需要copy,要不原图会变。。。
## -1==所有  0~.. 按照顺序选择图像
# (0,0,255)==颜色模式
draw_img = gray.copy()
res = cv.drawContours (draw_img,contours,-1,(0,0,255),2)
mf.cv_show( 'res',res)

draw_img = gray.copy()
res = cv.drawContours (draw_img,contours,3,(0,0,255),2)
mf.cv_show( 'res',res)


#2.图像轮廓特征
cnt=contours[1]
#轮廓面积
print(cv.contourArea(cnt))
#轮廓周长
#周长,True表示闭合的
print(cv.arcLength(cnt, True))

#3.1图像外接图像   -- 外接矩形
#读曲线
img = cv.imread('1.png')
gray=cv.cvtColor(img,cv.COLOR_RGB2GRAY)
#阈值分割
ret,thresh = cv.threshold (gray,127,255,cv.THRESH_BINARY)
mf.cv_show('res',thresh)

#寻找轮廓
contours,hierarchy = cv.findContours(thresh,cv.RETR_TREE,cv.CHAIN_APPROX_NONE)
draw_img = img.copy()
res_1 = cv.drawContours (draw_img,contours, -1,(0,0,255),2)
mf.cv_show('res_1',res_1)

# 取1号轮廓
cnt = contours[1]

x,y,w,h = cv.boundingRect(cnt)
img1 = cv.rectangle(img, (x, y),(x+w, y+h),(0,255,0),2)
mf.cv_show('img',img1)

#3.2 图像轮廓   -- 外接圆
#获取最小外接圆参数
(x, y) , radius = cv.minEnclosingCircle(cnt)
center = (int (x), int(y))
radius = int (radius)
img2 = cv.circle(img, center, radius,(255,0,0), 2)
mf.cv_show( 'img',img2)

#4.图像轮廓近似   -- 用直线近似曲线
#读曲线
img = cv.imread('1.png')
gray=cv.cvtColor(img,cv.COLOR_RGB2GRAY)
#阈值分割
ret,thresh = cv.threshold (gray,127,255,cv.THRESH_BINARY)
mf.cv_show('res',thresh)

#寻找轮廓
contours,hierarchy = cv.findContours(thresh,cv.RETR_TREE,cv.CHAIN_APPROX_NONE)
draw_img = img.copy()
res_1 = cv.drawContours (draw_img,contours, -1,(0,0,255),2)
mf.cv_show('res_1',res_1)

# 取1号轮廓
cnt = contours[1]
draw_img = img.copy()
#传入绘制图像,轮廓,轮廓索引,颜色模式==红色,线条厚度   -1表示所有轮廓
res_1 = cv.drawContours (draw_img,[cnt], -1,(0,0,255),2)
mf.cv_show('res_1',res_1)

# 越小越接近原图
epsilon = 0.01*cv.arcLength(cnt, True)
#近似轮廓函数  cnt--待近似的轮廓 epsilon--按照周长的百分比设置
approx = cv.approxPolyDP(cnt, epsilon,True)

draw_img = img.copy ()
res_2 = cv.drawContours(draw_img,[approx],-1,(0,0,255),2)
mf.cv_show('res_2',res_2)