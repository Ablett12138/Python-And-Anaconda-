#-------------    1.OpenCV的顺序为B->G->R  ---------------------#
#------------- 灰度转换 ---------------------#
image = cv2.imread('china.jpg')
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

#------------- 创建一个窗口 ---------------------#
new_window=cv2.namedWindow("myflag")
#------------- 在窗口显示图片
cv2.imshow(new_window,image)

#------------- 保存灰度国旗 ---------------------#
cv2.imwrite("gray_flag.jpg",gray)

#------------- 将图像分割成：r,g,b三张,并显示 ---------------------#
b,g,r=cv2.split(image)
cv2.merge([b,g,r])
cv2.imshow(new_window,b)
cv2.waitKey(-1)
cv2.imshow(new_window,g)
cv2.waitKey(-1)
cv2.imshow(new_window,r)

#------------- 延时 ---------------------#
cv2.waitKey(-1)





