##1.----------------------- 
error: (-215:Assertion failed) src.checkVector(2, CV_32F) = = 4 && dst.checkVector(2, CV_32F) == 4
points和这个需要是相同的shape并且类型都要是float32,不是float32就报错这个

##2.----------------------- 
cv2.error: OpenCV(4.7.0) D:\a\opencv-python\opencv-python\opencv\modules\imgproc\src\thresh.cpp:1555: error: (-2:Unspecified error) in function 'double __cdecl cv::threshold(const class cv::_InputArray &,const class cv::_OutputArray &,double,double,int)'
> THRESH_OTSU mode:
>     'src_type == CV_8UC1 || src_type == CV_16UC1'
> where
>     'src_type' is 16 (CV_8UC3)
要求输入图像为为单通道图像