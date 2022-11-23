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
    out = cv2.resize(src, (1024,1024))
    cv2.imwrite(dstpath + "1024-" + fname, out)
    print ("create dwn of %s -> %s"%(srcfile, dstpath + "1024-" + fname))

#
# img = cv2.imread("./labels/600DP-1_0_label.png")
#
# image = cv2.bitwise_not(src=img)
#
# cv2.imwrite('600DP-1_0_label.png', image)

# cv2.imshow("mask", image)
# cv2.waitKey()
# cv2.destroyAllWindows()