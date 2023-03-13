import cv2 as cv

'''                      定义一个捕获视频的类                          '''
capture = cv.VideoCapture(0)
# 获取捕获的分辨率
# propId 可以直接写数字,也可以用 OpenCV 的符号表示
width, height = int(capture.get(3)), int(capture.get(4))
print(width, height)

# 定义编码方式并创建 VideoWriter 对象
fourcc = cv.VideoWriter_fourcc(*'mp4v')

#设置保存路径以及保存参数
outfile = cv.VideoWriter('output.mp4', fourcc, 30, (width , height))


while(True):
    #开启相机捕获
    ret, frame = capture.read()
    if ret:
        outfile.write(frame) # 写入文件
        #显示捕获图片
        cv.imshow('frame', frame)
        #按‘q’退出
        if cv.waitKey(1) & 0xFF == ord('q'):
            print(" keybroads interrupted!!!")
            break
    else:
        break
# 完成所有操作后,释放捕获器
capture.release()
outfile.release()
cv.destroyAllWindows()

'''                      定义一个视频播放的类                         '''

capture=cv.VideoCapture('output.mp4')
cv.namedWindow("Video") 

#滑动块变化时的调用的处理函数,x为滑动块的值
def slide_change(x):
       print(x)
       #设置播放的帧数
       capture.set(cv.CAP_PROP_POS_FRAMES, x)

#获取视频的总帧数,视频太短可能会出现0帧的情况（导致报错）
frame_count=int(capture.get(cv.CAP_PROP_FRAME_COUNT))
#创建滑动条
cv.createTrackbar("Position","Video",0,frame_count,slide_change)

#获取视频的fps
Fps = int(capture.get(cv.CAP_PROP_FPS))
print("fps:",Fps,frame_count)

while(capture.isOpened()):
   
    framePos = int(capture.get(cv.CAP_PROP_POS_FRAMES))
    cv.setTrackbarPos("Position","Video",int(framePos))
    ret,frame=capture.read()
    if ret==True:

        #创建fps字符串显示
        str_fps="fps:{0}".format(Fps)
        
        #在视频上显示fps  --红色
        cv.putText(frame,str_fps, (5, 30), cv.FONT_HERSHEY_COMPLEX_SMALL, 1, (0,0,255), 2)
        cv.imshow("Video",frame)
        if cv.waitKey(int(1000/Fps)) & 0xFF == ord('q'):
            print(" keybroads interrupted!!!")
            break
        
    else:
        break
print("--------------------------   finish  !!!!!  destroyAllWindows ~~~   --------------------------")
capture.release()
cv.destroyAllWindows()
