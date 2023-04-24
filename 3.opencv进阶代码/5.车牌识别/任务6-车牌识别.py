import cv2
import pytesseract
import myfunction as mf
import numpy as np

# 灰度处理
def Pre_Processing(img):
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    gray = cv2.bilateralFilter(gray, 11, 17, 17)

    return gray

# 边缘检测
def img_Canny(gray):
    edged_image = cv2.Canny(gray, 30,600)

    contours, res = cv2.findContours(edged_image.copy(), cv2.RETR_LIST, cv2.CHAIN_APPROX_SIMPLE)
    img1 = img.copy()
    cv2.drawContours(img1, contours, -1, (0, 255, 0), 3)
    return contours,res

# 车牌定位
def find_license(img,contours):

    #最小面积30对轮廓进排序选
    contours = sorted(contours, key = cv2.contourArea, reverse = True)[:30]
    
    screenCnt = None
    # img2 = img.copy()
    
    # 画出剩余轮廓
    # cv2.drawContours(img2, contours, -1, (0, 255, 0), 3)

    ##遍历前30个轮廓
    for c in contours:
        # 近似车牌轮廓
        contour_perimeter = cv2.arcLength(c, True)
        approx = cv2.approxPolyDP(c, 0.018 * contour_perimeter, True)
        
        # 寻找具有 4 个角的轮廓
        if len(approx) == 4:
            screenCnt = approx
    
            # 查找车牌轮廓的坐标
            x, y, w, h = cv2.boundingRect(c)
            new_img = img [ y: y + h, x: x + w]
    
            # 存储图片
            cv2.imwrite('./'+str('chepai')+'.png',new_img)
            break
    
    # 在原始图像上绘制车牌轮廓
    cv2.drawContours(img , [screenCnt], -1, (0, 255, 0), 3)
    return img



# 车牌外框去除
def find_chepai(img,contours):

    #最小面积30对轮廓进排序选
    contours = sorted(contours, key = cv2.contourArea, reverse = True)[:30]

    count=0
    ##遍历前30个轮廓
    for c in contours:
        # print(cv2.contourArea(c))
        # 去除边框
        if (cv2.contourArea(c)==511.5) | (cv2.contourArea(c)<220):
            # 查找车牌外部轮廓的坐标
            x, y, w, h = cv2.boundingRect(c)
            # 去除外框
            img [ y: y + h, x: x + w]=0

    return img

if __name__=='__main__':
    img = cv2.imread('chepai/chepai1.jpg')
    gray = Pre_Processing(img)
    contours,_=img_Canny(gray)
    img = find_license(img,contours)

    车牌=cv2.imread('chepai.png',0)
    
    #利用Tesseract OCR进行字符识别
    #对比度增强  
    # img_bright = cv2.convertScaleAbs(车牌,alpha=1.8,beta=0)
    kernel = np.ones((1, 12), np.uint8)
    opening = cv2.morphologyEx(车牌,cv2.MORPH_OPEN, kernel)
    # mf.cv_show(opening) 
    # 阈值分割
    _, thresh = cv2.threshold(车牌, 180, 255, cv2.THRESH_BINARY)
    contours,_ = img_Canny(thresh)
    img = find_license(thresh,contours)
    # mf.cv_show(img)

    kernel = np.ones((3, 3), np.uint8)
    dilation = cv2.dilate(img, kernel)  # 膨胀
    # mf.cv_show(dilation)

    kernel = np.ones((1, 1), np.uint8)
    erosion = cv2.erode(dilation, kernel)  # 腐蚀
    # mf.cv_show(erosion) 

    # # binary==二值,contours==轮廓,hierarchy==层级
    contours,hierarchy = cv2.findContours(erosion, cv2.RETR_TREE, cv2.CHAIN_APPROX_NONE)
    img=find_chepai(erosion,contours)

    #开运算
    kernel = np.ones((2, 3), np.uint8)
    img = cv2.morphologyEx(img,cv2.MORPH_OPEN, kernel)
    # mf.cv_show(img) 
    # 填充范围  ---防止识别不到
    top_size, bottom_size,left_size,right_size = (10,10,10,10)
    # #             常量法，灰度常数值填充。 
    constant = cv2.copyMakeBorder(img,top_size,bottom_size,left_size,right_size, cv2.BORDER_CONSTANT,value=0)
    mf.cv_show(constant)
    text = pytesseract.image_to_string(constant,lang='chi_sim',config='--psm 6')

    print("车牌号是:", text)

