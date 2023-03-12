#-----------         模板匹配          ---------#
#1.匹配单个对象
#读曲线
img = cv.imread('1.png')
gray=cv.cvtColor(img,cv.COLOR_RGB2GRAY)
#阈值分割
ret,thresh = cv.threshold (gray,127,255,cv.THRESH_BINARY)
# mf.cv_show('res',thresh)

#寻找轮廓
contours,hierarchy = cv.findContours(thresh,cv.RETR_TREE,cv.CHAIN_APPROX_NONE)
draw_img = img.copy()
res_1 = cv.drawContours (draw_img,contours, -1,(0,0,255),2)
mf.cv_show('res_1',res_1)

# 取1号轮廓
cnt = contours[1]
cv.namedWindow("part",cv.WINDOW_NORMAL)
x,y,w,h = cv.boundingRect(cnt)
#先取行数再取列数
img_temp = gray[y:y+h,x:x+w]
mf.cv_show("part",img_temp)

# 1==cv.TM_CCOEFF   
# 建议采用最后3种归一化系数
methods = ['cv.TM_CCOEFF', 'cv.TM_CCOEFF_NORMED', 'cv.TM_CCORR','cv.TM_CCORR_NORMED', 'cv.TM_SQDIFF', 'cv.TM_SQDIFF_NORMED']
for meth in methods:
    img_copy=gray.copy()

    #匹配方法的真值  == 字符串转化为真值
    method = eval(meth)
    print (method)

    #模板匹配
    res = cv.matchTemplate(img_copy,img_temp,method)
    # min_val==模板匹配最小值,
    # max_val==模板匹配最大值,
    # min_loc==模板匹配最小值位置-左上角点,
    # max_loc==模板匹配最大值位置-左上角点
    min_val,max_val,min_loc,max_loc = cv.minMaxLoc(res)

    #如果是平方差匹配TM_SQDIFF或归一化平方差匹配TM_SQDIFF_NORMED,取最小值
    if method in [cv.TM_SQDIFF,cv.TM_SQDIFF_NORMED]:
        top_left = min_loc
    else:
        top_left = max_loc
    bottom_right = (top_left[0] + w, top_left[1] + h)
    # 画矩形
    cv.rectangle(img_copy,top_left,bottom_right,(0,0,255),2)
    plt.subplot(121), plt.imshow(res,cmap='gray')
    #隐藏坐标轴
    plt.xticks([]),plt.yticks([])
    plt.subplot (122),plt.imshow(img_copy,cmap='gray')
    plt.xticks([]), plt.yticks([])
    plt.suptitle (meth)
    plt.show()

# 2.匹配多个对象
#1.匹配单个对象
#读曲线
img = cv.imread('1.png')
gray=cv.cvtColor(img,cv.COLOR_RGB2GRAY)
#阈值分割
ret,thresh = cv.threshold (gray,127,255,cv.THRESH_BINARY)
# mf.cv_show('res',thresh)

#寻找轮廓
contours,hierarchy = cv.findContours(thresh,cv.RETR_TREE,cv.CHAIN_APPROX_NONE)
draw_img = img.copy()
res_1 = cv.drawContours (draw_img,contours, -1,(0,0,255),2)
mf.cv_show('res_1',res_1)

# 取1号轮廓
cnt = contours[1]
cv.namedWindow("part",cv.WINDOW_NORMAL)
x,y,w,h = cv.boundingRect(cnt)
#先取行数再取列数
img_temp = gray[y:y+h,x:x+w]
mf.cv_show("part",img_temp)

res = cv.matchTemplate(gray,img_temp,cv.TM_CCOEFF_NORMED)
threshold = 0.97
#取匹配程度大于%97的坐标
loc = np.where(res >= threshold)
#*号表示可选参数
for pt in zip(*loc[: :-1]):
    bottom_right = (pt[0] + w, pt[1] + h)
    cv.rectangle(img,pt,bottom_right,(0,0, 255),2)
    cv.imshow(' img_rgb', img)
    cv.waitKey(0)