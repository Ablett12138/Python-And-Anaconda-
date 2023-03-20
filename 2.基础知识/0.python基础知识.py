##              编写完文本记得保存
AttributeError: module 'myfuntion' has no attribute 'cv_show'


##              plt图像显示
plt.imshow()是rgb模式,但是cv.imread()是bgr模式

##              矩阵创建                        
np.zeros()---全部值为0的矩阵  np.ones()----全部值是1的矩阵

##              字符串创建
str_fps="fps:{0}".format(Fps)
cv.putText(frame,str_fps, (5, 30), cv.FONT_HERSHEY_COMPLEX_SMALL, 1, (0,0,255), 2)
##              global关键词
在Python中，"global"是一个关键字，用于声明一个变量是全局变量而不是局部变量。
如果在函数内部需要使用全局变量，则需要在函数内部使用"global"关键字声明该变量，否则Python会将该变量视为局部变量