import glob
import os
import cv2
import numpy as np

if __name__ == "__main__":
    
    w = 11   #根据实际角点个数，9x7格子，角点就是8x6
    h = 12   #正确的数目很重要，否则会报错
    objp = np.zeros((w*h,3), np.float32)
    objp[:,:2] = np.mgrid[0:w, 0:h].T.reshape(-1,2)

    obj_points = []
    img_points = []

    images = glob.glob('calib/*.tif') #该文件夹下棋盘图片
    criteria = (cv2.TERM_CRITERIA_EPS | cv2.TERM_CRITERIA_MAX_ITER, 30, 0.001) # 为角点检测设置终止条件 迭代30次或者是移动0.001 
    for fname in images:
        img = cv2.imread(fname)
        gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
        size = gray.shape[::-1]
        ret, corners = cv2.findChessboardCorners(gray,(w,h),None)
        if ret == True:
            cv2.cornerSubPix(gray, corners, (11,11), (-1,-1), criteria)  # 角点检测
            obj_points.append(objp)
            img_points.append(corners)
            
            cv2.drawChessboardCorners(img,(w,h),corners,ret)
            cv2.imshow('findCorners',img)
            cv2.waitKey(0)#每按一次空格开始标定下一张
    cv2.destroyAllWindows()
    #标定
    ret, mtx, dist, rvecs, tvecs = cv2.calibrateCamera(obj_points, img_points,gray.shape[::-1],None,None)
    # 相机内参矩阵
    print("ret: \n",ret)
    print("mtx: \n",mtx) 