import cv2
import myfunction as mf

#读取拼接图片
imageA = cv2.imread( "feature_matching.png")
imageB = cv2.imread( "feature_matchings.png")

#把图片拼接成全景图
stitcher = mf.stitcher()
result = stitcher.stitch([imageA, imageB],showMatches=True)

#样显示所有图片
mf.cv_show(result,cv2.WINDOW_NORMAL)

