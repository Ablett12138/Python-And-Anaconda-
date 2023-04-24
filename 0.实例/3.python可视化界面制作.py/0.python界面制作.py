from tkinter import *
import tkinter.filedialog  # 注意次数要将文件对话框导入
from PIL import Image,ImageTk
import cv2

"""
Showimage()是一个用于在tkinter的canvas控件中显示OpenCV图像的函数。
使用前需要先导入库
import cv2 as cv
from PIL import Image,ImageTktkinter
并注意由于响应函数的需要，本函数定义了一个全局变量 imgTK，请不要在其他地方使用这个变量名!
参数：
imgCV_in：待显示的OpenCV图像变量
canva：用于显示的tkinter canvas画布变量
layout：显示的格式。可选项为：
     "fill"：图像自动适应画布大小，并完全填充，可能会造成画面拉伸
     "fit"：根据画布大小，在不拉伸图像的情况下最大程度显示图像，可能会造成边缘空白
     给定其他参数或者不给参数将按原图像大小显示，可能会显示不全或者留空
"""
def Showimage(imgCV_in,canva,layout="null"):
    global imgTK
    canvawidth = int(canva.winfo_reqwidth())
    canvaheight = int(canva.winfo_reqheight())
    sp = imgCV_in.shape
    cvheight = sp[0]#height(rows) of image
    cvwidth = sp[1]#width(colums) of image
    if (layout == "fill"):
        imgCV = cv2.resize(imgCV_in,(canvawidth,canvaheight), interpolation=cv2.INTER_AREA)
    elif(layout == "fit"):
        if (float(cvwidth/cvheight) > float(canvawidth/canvaheight)):
            imgCV = cv2.resize(imgCV_in,(canvawidth,int(canvawidth*cvheight/cvwidth)), interpolation=cv2.INTER_AREA)
        else:
            imgCV = cv2.resize(imgCV_in,(int(canvaheight*cvwidth/cvheight),canvaheight), interpolation=cv2.INTER_AREA)
    else:
        imgCV = imgCV_in
    imgCV2 = cv2.cvtColor(imgCV, cv2.COLOR_BGR2RGBA)#转换颜色从BGR到RGBA
    current_image = Image.fromarray(imgCV2)   #将图像转换成Image对象
    imgTK = ImageTk.PhotoImage(image=current_image)#将image对象转换为imageTK对象
    canva.create_image(0,0,anchor = NW, image = imgTK)

# 定义一个处理文件的相关函数
def openimgfile():
     global image_show
    # 从本地选择一个文件，并返回文件的目录
     filename = tkinter.filedialog.askopenfilename()
     if filename != '':
          lb.config(text= filename)
     else:
          lb.config(text='您没有选择任何文件')

     # 显示
     image_show = cv2.imread(filename)
     #     Showimage(image_show,canva,"fill")
     Showimage(image_show,canva,"fit")
#     Showimage(image_show,canva,"")

#灰度化
def img_to_gray(): 
    global image_show
    #将图片转为灰度图
    image_show = cv2.cvtColor(image_show,cv2.COLOR_RGB2GRAY)
    Showimage(image_show,canva,"fit")

#阈值分割
def img_thres(): 
    global image_show
    #将图片转为灰度图
    ret,image_show = cv2.threshold(image_show,127,255,cv2.THRESH_BINARY)
    Showimage(image_show,canva,"fit")

#（一）定义界面，陈2023
root = Tk()
root.title("我的图像处理界面")
root.geometry("640x580")   #w,h
root.resizable(0,0) #阻止Python GUI的大小调整
canva = Canvas(root, width=640, height=480,bg="gray")
button = Button(root, text="打开图像", width=10,command=openimgfile)
lb = Label(root,text='待打开的图片',bg='#87CEEB')
button_gray = Button(root, text="灰度化", width=10,command=img_to_gray)
button_thres = Button(root, text="二值化", width=10,command=img_thres)

#（二）接着布局
canva.grid(row=0,column=0,columnspan=2)
button.grid(row=1, column=0, sticky="w",pady=5)
lb.grid(row=1,column=0,pady=5)
button_gray.grid(row=2, column=0, sticky="w",pady=5)
button_thres.grid(row=2, column=1, sticky="w",pady=5)

root.mainloop()
