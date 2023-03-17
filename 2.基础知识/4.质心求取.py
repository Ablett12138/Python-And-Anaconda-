import cv2 as cv
import matplotlib.pyplot as plt
 
 
# 封装图片显示函数
def image_show(image):
    if image.ndim == 2:
        plt.imshow(image, cmap='gray')
    else:
        image = cv.cvtColor(image, cv.COLOR_BGR2RGB)
        plt.imshow(image)
    plt.show()
 
 
if __name__ == '__main__':
 
    # 读取原图
    img_desk = cv.imread('desk.png')
 
    # 转换为灰度图
    img_gray = cv.cvtColor(img_desk, cv.COLOR_RGB2GRAY)
 
    # 二值化
    [thresh, img_bin] = cv.threshold(img_gray, -1, 255, cv.THRESH_OTSU)
 
    # 获取轮廓
    [cnt, hir] = cv.findContours(img_bin, cv.RETR_CCOMP, cv.CHAIN_APPROX_NONE)
 
    # 绘制轮廓
    cv.drawContours(img_desk, cnt, 12, (0, 0, 255), 2)
 
    # 计算一阶矩
    Moment = cv.moments(cnt[12])
 
    # 计算质心
    Moment_X = int(Moment['m10'] / Moment['m00'])
    Moment_Y = int(Moment['m01'] / Moment['m00'])
    print("显示图像的质心为：", Moment_X, Moment_Y)
 
    # 计算弧长
    arc = cv.arcLength(cnt[12], True)
    print("显示图像的弧长为：", int(arc))
 
    # 计算面积
    area = cv.contourArea(cnt[12])
    print("显示图像的面积为：", int(area))
 
    # 近似轮廓
    epsilon = 0.1 * arc
    approx = cv.approxPolyDP(cnt[12], epsilon, True)
 
    # 显示图像
    image_show(img_desk)
 
    # 绘制图像的近似轮廓
    cv.drawContours(img_desk, [approx], 0, (255, 0, 0), 3)
 
    # 显示图像
    image_show(img_desk)

————————————————
版权声明：本文为CSDN博主「阿飞_Y」的原创文章，遵循CC 4.0 BY-SA版权协议，转载请附上原文出处链接及本声明。
原文链接：https://blog.csdn.net/weixin_42704093/article/details/124070937