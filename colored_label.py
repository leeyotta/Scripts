# -- coding: utf-8 --**
# @Author  : LeeYotta
import os
import cv2
import numpy as np
import matplotlib.pyplot as plt
from skimage import measure, color, io


def cv_show(img, name):
    cv2.imshow(name, img)
    cv2.waitKey()
    cv2.destroyAllWindows()


path = input("Please input the folder:") # "./"
form = input("Please input the image formate:") # ".png"

# cv_show(thresh, 'thresh')


data_names = os.listdir(path)
for i in data_names:
    # print(os.path.splitext(i))
    name = os.path.splitext(i)[0]
    if os.path.splitext(i)[1] == form:
        img = cv2.imread(path+i)
        img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        # labelme生成的label.png的红色转灰度后为38所以这里值设为30
        ret, thresh = cv2.threshold(img_gray, 30, 255, cv2.THRESH_BINARY)
        labels = measure.label(thresh)  # 8连通区域标记
        dst = color.label2rgb(labels, bg_label=0)  # 根据不同的标记显示不同的颜色
        # print('regions number:', labels.max() + 1)  # 显示连通区域块数(从0开始标记)
        cv_show(dst, 'dst')
        io.imsave(path+i, dst)
