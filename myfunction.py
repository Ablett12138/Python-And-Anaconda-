# -*- coding: utf-8 -*-
import cv2

#显示图像---name=windowname 
def cv_show(name,image):
    cv2.imshow(name,image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

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
        
        




