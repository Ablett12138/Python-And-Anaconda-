# -*- coding: utf-8 -*-
import cv2 as cv
import numpy as np
from matplotlib import pyplot as plt

#显示图像---name=windowname 
def cv_show(name,image):
    cv.imshow(name,image)
    cv.waitKey(0)
    cv.destroyAllWindows()

#图像切片--左上角，右下角   name=windowname 
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
        plt.subplot(2,3,i+1),plt.imshow(images[i],'gray')
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


