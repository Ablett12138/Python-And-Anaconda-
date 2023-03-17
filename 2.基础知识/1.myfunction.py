# -*- coding: utf-8 -*-
import cv2 as cv
import numpy as np
from matplotlib import pyplot as plt

#显示图像---name=windowname 
def cv_show(image,mod):
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


