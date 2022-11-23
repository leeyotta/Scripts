import glob
import os
import shutil
import cv2

src_dir = './labels/'
dstpath = './'
src_file_list = glob.glob(src_dir +'*.png')
for srcfile in src_file_list:
    fpath, fname=os.path.split(srcfile)             # 分离文件名和路径
    src = cv2.imread(srcfile)
    bwn = cv2.bitwise_not(src=src)
    cv2.imwrite(dstpath + fname, bwn)
    print ("create dwn of %s -> %s"%(srcfile, dstpath + fname))

#
# img = cv2.imread("./labels/600DP-1_0_label.png")
#
# image = cv2.bitwise_not(src=img)
#
# cv2.imwrite('600DP-1_0_label.png', image)

# cv2.imshow("mask", image)
# cv2.waitKey()
# cv2.destroyAllWindows()