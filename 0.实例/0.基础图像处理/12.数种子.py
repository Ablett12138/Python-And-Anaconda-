import cv2,os
import numpy as np
import myfunction as mf
from matplotlib  import pyplot as plt

img_path = 'seed'
fileNames = os.listdir(img_path)  #获取当前文件路径下的文件名，返回list
img_list = []
img_size = np.size(fileNames)
for file in fileNames:
    img_folder = img_path + '\\' + file   #图片路径
    # print(img_folder)
    # 读取图像1
    img=cv2.imread(img_folder)  
    # 灰度化
    gray = cv2.cvtColor(img,code=cv2.COLOR_BGR2GRAY)
    if file=='xiancai.JPG':
     # 阈值分割
        img = cv2.convertScaleAbs(img,alpha=0.5,beta=0)
        # mf.cv_show(img)
        lower_1 = np.array([0, 0, 46])
        upper_1 = np.array([180, 43, 22])
        img_xiancai=mf.HSV_Mask(img,lower_1,upper_1)
        gray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
        ret, thresh = cv2.threshold(gray, 0, 255, cv2.THRESH_BINARY_INV + cv2.THRESH_OTSU)
        # mf.cv_show(thresh)
        # 像素距离计算   
        # dist = cv.distanceTransform(src=gaussian_hsv, distanceType=cv.DIST_L2, maskSize=5)
        distTransform = cv2.distanceTransform(thresh, cv2.DIST_L2, 5)
        # 阈值分割
        ret, fore = cv2.threshold(distTransform, 0.2*distTransform.max(), 255, 0)
        fore = np.uint8(fore)
        count, markets = cv2.connectedComponents(fore)
        print('苋菜数量:',count)
        pass 

    elif file=='damai.JPG':
        count=mf.fenshuiling(gray,0.40)
        print('大麦数量:',count)
        pass
    elif file =='nangua.JPG':
        # 提取黄色区间
        lower_1 = np.array([26, 43, 46])
        upper_1 = np.array([34, 255, 255])
        img_nangua=mf.HSV_Mask(img,lower_1,upper_1)
        gray=cv2.cvtColor(img_nangua,cv2.COLOR_BGR2GRAY)
        count=mf.fenshuiling(gray,0.01)
        print('南瓜的数量:',count)
        pass
    elif file=='caidou.jpg':
        count=mf.fenshuiling(gray,0.40)
        print('菜豆数量:',count)
        pass
    elif file=='lajiao.jpg':
        # 提取黄色区间
        lower_1 = np.array([15, 20, 20])
        upper_1 = np.array([255, 255, 255])
        img_lajiao=mf.HSV_Mask(img,lower_1,upper_1)
        # mf.cv_show(img_lajiao)
        gray=cv2.cvtColor(img_lajiao,cv2.COLOR_BGR2GRAY)
        ret, thresh = cv2.threshold(gray, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)
        # mf.cv_show(thresh)
        # 像素距离计算   
        # dist = cv.distanceTransform(src=gaussian_hsv, distanceType=cv.DIST_L2, maskSize=5)
        distTransform = cv2.distanceTransform(thresh, cv2.DIST_L2, 5)
        # 阈值分割
        ret, fore = cv2.threshold(distTransform, 0.04*distTransform.max(), 255, 0)
        fore = np.uint8(fore)
        count, markets = cv2.connectedComponents(fore)
        print('辣椒的数量:',count)
        pass
    elif file=='xiaomai.JPG':
        # 提取黄色区间
        ret, thresh = cv2.threshold(gray, 210, 255, cv2.THRESH_BINARY)
        # mf.cv_show(thresh)  
        fore = np.uint8(thresh)
        count, markets = cv2.connectedComponents(fore)
        print('小麦的数量:',count)
        pass
    elif file=='xigua.JPG':
         # 提取黄色区间
        lower_1 = np.array([15, 20, 20])
        upper_1 = np.array([255, 255, 255])
        img_xigua=mf.HSV_Mask(img,lower_1,upper_1)
        # mf.cv_show(img_lajiao)
        gray=cv2.cvtColor(img_xigua,cv2.COLOR_BGR2GRAY)
        ret, thresh = cv2.threshold(gray, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)
        # mf.cv_show(thresh)
        # 像素距离计算   
        # dist = cv.distanceTransform(src=gaussian_hsv, distanceType=cv.DIST_L2, maskSize=5)
        distTransform = cv2.distanceTransform(thresh, cv2.DIST_L2, 5)
        # 阈值分割
        ret, fore = cv2.threshold(distTransform, 0.04*distTransform.max(), 255, 0)
        fore = np.uint8(fore)
        count, markets = cv2.connectedComponents(fore)
        print('西瓜的数量:',count)
        pass
    elif file=='yumi1.JPG':
        # 提取黄色区间
        lower_1 = np.array([26, 43, 46])
        upper_1 = np.array([34, 255, 255])
        img_yumi=mf.HSV_Mask(img,lower_1,upper_1)
        gray=cv2.cvtColor(img_yumi,cv2.COLOR_BGR2GRAY)
        count=mf.fenshuiling(gray,0.01)
        print('玉米1的数量:',count)
    elif file=='yumi2.JPG':
        count=mf.fenshuiling(gray,0.01)
        print('玉米2的数量:',count)
        pass
    else:
        break
  
    
    
    

    
    
    
    