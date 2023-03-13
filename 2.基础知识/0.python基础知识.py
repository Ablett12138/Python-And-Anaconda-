##              编写完文本记得保存
AttributeError: module 'myfuntion' has no attribute 'cv_show'


##              plt图像显示
plt.imshow()是rgb模式,但是cv.imread()是bgr模式

##              矩阵创建                        
np.zeros()---全部值为0的矩阵  np.ones()----全部值是1的矩阵

##              字符串创建
str_fps="fps:{0}".format(Fps)