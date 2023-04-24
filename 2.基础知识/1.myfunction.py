# -*- coding: utf-8 -*-
import cv2 as cv
import numpy as np
from matplotlib import pyplot as plt


#-------   RANCSAC算法匹配  -----#
class stitcher:
    #拼接函数
    def stitch(self,images,ratio=0.75,reprojThresh=4.0,showMatches=False):
       #获取输入图片
        (imageA,imageB) = images
        #检测A、B图片的SIFT关键特征点,并计算特征描述子
        (kpsA, featuresA,grayA) = self.detectAndDescribe(imageA)
        (kpsB, featuresB,grayB) = self.detectAndDescribe(imageB)
        #匹配两张图片的所有特征点,返回匹配结果
        M= self.matchKeypoints(kpsA,kpsB,featuresA,featuresB,grayA,grayB,ratio,reprojThresh)
        #如果返回结果为空,没有匹配成功的特征点,退出算法
        if M is None:
            return None
        #否则,提取匹配结果#H是3x3视角变换矩阵
        (H,good,matchesMask) =M
        #将图片A进行视角变换, result是变换后图片
        result = cv.warpPerspective(imageA,H,(imageA.shape[1] + imageB.shape[1],imageA.shape[0]))
        cv_show(result,cv.WINDOW_NORMAL)
        #将图片B传入result图片最左端
        # print(imageA.shape[1])
        # print(imageB.shape[1])
        # print(result.shape[0],result.shape[1])
        result[0:imageA.shape[0],imageA.shape[1]:imageA.shape[1]+imageB.shape[1]] = imageB
        cv_show(result,cv.WINDOW_NORMAL)
        #检测是否需要显示图片匹配
        if showMatches==True:
            draw_params = dict(matchColor = (0,255,0), # draw matches in green color
            singlePointColor = None,
            matchesMask = matchesMask, # draw only inliers
            flags = 2)
            result = cv.drawMatches(grayA,kpsA,grayB,kpsB,good,None,**draw_params)
            return result

    def detectAndDescribe(self, image) :
        #将彩色图片转换成灰度图
        gray = cv.cvtColor(image,cv.COLOR_BGR2GRAY)
        #建立SIFT生成器
        descriptor = cv.SIFT_create()
        #检测SIFT特征点,并计算描述子
        (kps,features) = descriptor.detectAndCompute(image,None)
        #将结果转换成NumPy数组
        # kps = np.float32([kp.pt for kp in kps])
        #返回特征点集,及对应的描述特征
        return (kps,features,gray)
    
    def matchKeypoints(self,kpsA,kpsB,featuresA,featuresB,imgA,imgB,ratio,reprojThresh):
        MIN_MATCH_COUNT = 10
        FLANN_INDEX_KDTREE = 0
        index_params = dict(algorithm = FLANN_INDEX_KDTREE, trees = 5)
        search_params = dict(checks = 50)
        flann = cv.FlannBasedMatcher(index_params, search_params)
        matches = flann.knnMatch(featuresA,featuresB,k=2)
        # store all the good matches as per Lowe's ratio test.
        good = []
        for m,n in matches:
            if m.distance < ratio*n.distance:
                good.append(m)
        if len(good)>MIN_MATCH_COUNT:
            # 获取关键点的坐标
            src_pts = np.float32([kpsA[m.queryIdx].pt for m in good]).reshape(-1,1,2)
            dst_pts = np.float32([kpsB[m.trainIdx].pt for m in good]).reshape(-1,1,2)
            # 第三个参数 Method used to computed a homography matrix. The following methods are possible:
            #0 - a regular method using all the points
            #CV_RANSAC - RANSAC-based robust method
            #CV_LMEDS - Least-Median robust method
            # 第四个参数取值范围在 1 到 10，拒绝一个点对的阈值。原图像的点经过变换后点与目标图像上对应点的误差
            # 超过误差就认为是 outlier
            # 返回值中 M 为变换矩阵。
            H, mask = cv.findHomography(src_pts, dst_pts, cv.RANSAC,reprojThresh)
            matchesMask = mask.ravel().tolist()
            # # 获得原图像的高和宽
            # h,w = imgA.shape
            # # 使用得到的变换矩阵对原图像的四个角进行变换，获得在目标图像上对应的坐标。
            # pts = np.float32([ [0,0],[0,h-1],[w-1,h-1],[w-1,0] ]).reshape(-1,1,2)
            # dst = cv.perspectiveTransform(pts,M)
            # # 原图像为灰度图
            # cv.polylines(imgB,[np.int32(dst)],True,255,10, cv.LINE_AA)
            return (H,good,matchesMask)
        else:
            print ("Not enough matches are found - %d/%d",(len(good),MIN_MATCH_COUNT))
            matchesMask = None
            return 
        # draw_params = dict(matchColor = (0,255,0), # draw matches in green color
        # singlePointColor = None,
        # matchesMask = matchesMask, # draw only inliers
        # flags = 2)
        # img3 = cv.drawMatches(img1,kp1,img2,kp2,good,None,**draw_params)
        # plt.imshow(img3, 'gray'),plt.show()
        


#k对最佳匹配
def myFeature_matchingK(img1,img2):
    # 创建sift
    sift = cv.SIFT_create()

    #得到关键点
    kp1,des1 = sift.detectAndCompute(img1,None)
    kp2,des2 = sift.detectAndCompute(img2,None)

    #-------------------------   k对最佳匹配   --------------------------#
    bf = cv.BFMatcher()
    matches = bf.knnMatch(des1,des2,k=2)

    good = []
    for m, n in matches:
        if m.distance< 0.75*n.distance:
            good.append([m])

    result = cv.drawMatchesKnn(img1, kp1,img2, kp2,good,None,flags=2)

    return result



#显示图像---name=windowname 
def cv_show(image,mod=cv.WINDOW_NORMAL):
    cv.namedWindow('image',mod)
    cv.imshow('image',image)
    cv.waitKey(0)
    cv.destroyAllWindows()

#图像切片--左上角,右下角   name=windowname 
def cv_cut(name,image,row1,colunm1,row2,colunm2):
    cut=image[row1:row2,colunm1:colunm2]
    cv_show(name,cut)
    return cut

#图像保留三色通道之一   name=windowname 1=b 2=g 3=r
def cv_save_channel(name,image,num):
    cut_img=image.copy()
    if num == 1:
        cut_img[:,:,1]=0
        cut_img[:,:,2]=0
    elif num == 2:
        cut_img[:,:,0]=0
        cut_img[:,:,2]=0
    elif num == 3:
        cut_img[:,:,0]=0
        cut_img[:,:,1]=0
    else:
        print ("wrong!!!")
    cv_show(name,cut_img)
    return cut_img
#最多同时显示6张        
def cv_show_multiple_imgs(images,titles,num):
    for i in range(num):
        plt.subplot(1,2,i+1),plt.imshow(images[i],'gray')
        plt.title(titles[i])
        plt.xticks([]),plt.yticks([])
    plt.show()

def cv_gray_image (image):
    w,h,c=image.shape
    my_gray=np.zeros(image.shape[:2],np.uint8)
    for i in range(w):
        for j in range(h):
            my_gray[i,j]=image[i,j,0]*0.299+image[i,j,1]*0.587+image[i,j,2]*0.114;
    return my_gray


def cv_gray_histogram (image):
    w,h=image.shape
    my_gray_histo=np.zeros((256,1),np.uint8)
    my_gray_value=0
    for i in range(w):
        for j in range(h):
            my_gray_value=image[i,j]
            my_gray_histo[my_gray_value,0]=my_gray_histo[my_gray_value,0]+1
    return my_gray_histo

#设置同比例高
def cv_image_resize(image,width=None,height=None,inter=cv.INTER_AREA):
    dim = None
    (h, w) = image.shape[ :2]
    if width is None and height is None:
        return image
    if width is None:
        r = height / float(h)
        dim = (int(w * r), height)
    else:
        r = width / float(w)
        dim = (width,int(h * r))
    resized = cv.resize( image, dim,interpolation=inter)
    return resized

#提取四个端点
def order_points(pts):
    tl=pts[1]
    tr=pts[0]
    br=pts[3]
    bl=pts[2]
    return tl, tr, br , bl


# def order_pointsk(pts):
#     #一共4个坐标点
#     rect = np.zeros ((4,2),dtype = "float32")
#     #按顺序找到对应坐标0123分别是左上,右上,右下,左下
#     # #计算左上,右下
#     s = pts.sum( axis = 1)
#     rect[0] = pts[np.argmin(s)]
#     rect[2] = pts[np.argmax(s)]
#     #计算右上和左下
#     diff = np.diff(pts,axis = 1)
#     rect[1] - pts[np.argmin(diff)]
#     rect[3] = pts[np.argmax(diff)]
#     return rect


#四个端点透视变换  需要原图和需要变换的区域图
def four_point_transform(image,pts):
    #获取输入坐标
    rect = order_points(pts)
    (tl, tr, br , bl)=rect
    print('rect',rect)
    #计算输入的w和h值
    widthA = np.sqrt(((br[0] - bl[0])** 2) + ((br[1] - bl[1])**2))
    widthB = np.sqrt(((tr[0] - tl[0])** 2) + ((tr[1] - tl[1])**2))
                                                  
    maxWidth= max(int(widthA),int(widthB))
    heightA = np.sqrt(((tr[0] - br[0])**2) + ((tr[1] - br[1]) **2))
    heightB = np.sqrt(((tl[0] - bl[0])** 2) + ((tl[1] - bl[1])** 2))
    maxHeight = max( int(heightA),int(heightB))
    print(maxWidth,maxHeight)
    #变换后对应坐标位置
    dst= np.array([
    [0,0],
    [maxWidth - 1,0],
    [maxWidth - 1, maxHeight - 1],
    [0,maxHeight - 1]],dtype = "float32")

    print(dst,dst.dtype)
    
    # np.reshape(rect,4,2)
    print(np.asarray(rect,dtype = "float32"))
    #计算变换矩阵
    M= cv.getPerspectiveTransform(np.asarray(rect,dtype = "float32"),dst)
    warped = cv.warpPerspective(image,M,(maxWidth,maxHeight))
    #返回变换后结果
    return warped



def yumi_count(img,thre):
    # img = cv.imread(t_)
    font = cv.FONT_HERSHEY_COMPLEX
    kernel = np.ones((5,5), np.uint8)
 
    h,w,c = img.shape
    img = cv.resize(img,(int(1000*(w/h)),1000))#(w,h)
    # cv.imshow('ori', img)
    

    gray_img = cv.cvtColor(img, cv.COLOR_BGR2GRAY)  # 灰度处理
    # cv.imshow('gray_img', gray_img)
    ret, th1 = cv.threshold(gray_img, thre, 255, cv.THRESH_BINARY)
    cv_show(th1)
    # cv.imshow('th1', th1)
    erosion = cv.erode(th1, kernel, iterations=1)  # 腐蚀
    # cv.imshow('erosion', erosion)
    dist_img = cv.distanceTransform(erosion, cv.DIST_L1, cv.DIST_MASK_3)  # 距离变换
    # cv.imshow('ditancechange', dist_img)
    dist_output = cv.normalize(dist_img, 0, 1.0, cv.NORM_MINMAX)  # 归一化  这里的归一化取得了什么效果？
    a = 130 #显示程度
    b = 0.23#腐蚀程度  多次参数调整也无法避免籽粒出现粘连的情况
 
    # cv.imshow('dist_output', dist_output * a)
 
    ret, th2 = cv.threshold(dist_output*a, b, 255, cv.THRESH_BINARY)#这里调整系数 发现a = 120 b = 0.27比较符合正常的籽粒大小
    # cv.imshow('th2', th2)
 
    kernel = np.ones((3,3), np.uint8)
    opening = cv.morphologyEx(th2, cv.MORPH_OPEN, kernel)
 
    # cv.imshow('opening', opening)
    opening = np.array(opening, np.uint8)
    contours, hierarchy = cv.findContours(opening, cv.RETR_TREE, cv.CHAIN_APPROX_SIMPLE)  # 轮廓提取
 
    count_ = 0
    Allarea_circle = 0
 
    for cnt in contours:
        (x, y), radius = cv.minEnclosingCircle(cnt)#画圆
        center = (int(x), int(y))#中心点
        radius = int(radius)#半径
        # circle1_img = cv.circle(opening, center, radius, (128,0,128), 2)
        # cv.imshow('circle1_img',circle1_img)#黑白图的实际结果 测试用
        cv.circle(img, center, radius, (128, 0, 128), 1)#画圆
 
        # circle_img = cv.circle(img, center, radius, (128,0,128), 1)#画圆
        # cv.imshow('circle_img',circle_img)
 
        area_circle=3.14*radius*radius
        Allarea_circle +=area_circle
        count_ += 1
    aver_area_circle = Allarea_circle / count_#计算平均玉米粒外接圆半径
 
    count = 0
    for cnt in contours:#在这里使用外接圆的面积来增加容错率
        (x, y), radius = cv.minEnclosingCircle(cnt)
        center = (int(x), int(y))
        radius = int(radius)
        area_circle=3.14*radius*radius
 
        if area_circle>=2*aver_area_circle:#判断两个籽粒黏连的情况
 
            img = cv.putText(img, str(count)+'  '+str(count+1), center, font, 0.5, (0, 0, 255))
            count += 2#半径过大就算作两个
        else:
            img = cv.putText(img, str(count), center, font, 0.5, (0, 0, 255))
            count += 1
 
    img=cv.putText(img,('Findall='+str(count)),(10,40),font,1,(0,20,255),2)#添加文字到图上 总数
 
    cv.imshow('circle_img',img)
    cv.waitKey(0)
    cv.destroyAllWindows()
 
    return count

def fenshuiling(gray,a):
    # 灰度化
    # 自适应反转阈值分割
    ret, thresh = cv.threshold(gray, 0, 255, cv.THRESH_BINARY_INV + cv.THRESH_OTSU)
    # cv_show(thresh)
    # 开运算
    k = np.ones((6, 6), dtype=np.uint8)
    opening = cv.morphologyEx(thresh, cv.MORPH_OPEN, k, iterations=3)

    # 像素距离计算   
    # dist = cv.distanceTransform(src=gaussian_hsv, distanceType=cv.DIST_L2, maskSize=5)
    distTransform = cv.distanceTransform(opening, cv.DIST_L2, 5)
    # 阈值分割
    ret, fore = cv.threshold(distTransform, a*distTransform.max(), 255, 0)
    # 背景计算
    bg = cv.dilate(opening, k, iterations=3)
    # 连通体计算
    # 前景
    fore = np.uint8(fore)
    num, markets = cv.connectedComponents(fore)

    unknown = cv.subtract(bg, fore)
    markets = markets + 1
    markets[unknown == 255] = 0
    # 分水岭算法
    img=cv.cvtColor(gray,cv.COLOR_GRAY2BGR)
    markets = cv.watershed(img, markets)
    # print(markets)
    img[markets == -1] = [255, 0, 0]
    # cv_show(img)
    return num

def HSV_Mask(img_lenna,lower,upper):
    # 转换到HSV颜色空间
    img_hsv = cv.cvtColor(img_lenna, cv.COLOR_BGR2HSV)
 
    # 设置红色边界 (保留黄色)
    lower_1 = lower
    upper_1 = upper
 
 
    # 获取掩码范围
    mask = cv.inRange(img_hsv, lower_1, upper_1)
 
 
    # 维度扩充并归一化
    mask = cv.merge([mask, mask, mask]) // 255
 
    # 图像掩码处理
    img_red = img_hsv * mask
    
    # 转换为BGR通道
    img_bgr = cv.cvtColor(img_red, cv.COLOR_HSV2BGR)
    return img_bgr