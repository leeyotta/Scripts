# -- coding: utf-8 --**
# @Author  : LeeYotta
import os
import cv2
read_path = input("Please input the original image path:") # "./test"
save_path = input("Please input the splitted image path:") # "./test_result"
if not os.path.exists(save_path):
    os.makedirs(save_path)
sub_image_num = int(input("Please input the sub_image_num(a square num):")) # 4
split_num = int(pow(sub_image_num,0.5))
datanames = os.listdir(read_path)
for i in datanames:
    # print(os.path.splitext(i))
    name = os.path.splitext(i)[0]
    if os.path.splitext(i)[1] == ".JPG":
        src = cv2.imread(read_path + "//" + i, 0)
        src_height, src_width = src.shape[0], src.shape[1]
        sub_height = src_height // split_num
        sub_width = src_width // split_num
        sub_images = []
        for j in range(split_num):
            for i in range(split_num):
                if j < split_num - 1 and i < split_num - 1:
                    image_roi = src[j * sub_height: (j + 1) * sub_height, i * sub_width: (i + 1) * sub_width]
                elif j < split_num - 1:
                    image_roi = src[j * sub_height: (j + 1) * sub_height, i * sub_width:]
                elif i < split_num - 1:
                    image_roi = src[j * sub_height:, i * sub_width: (i + 1) * sub_width]
                else:
                    image_roi = src[j * sub_height:, i * sub_width:]
                sub_images.append(image_roi)
        for k, img in enumerate(sub_images):
            cv2.imwrite(save_path + "//" + name + "_"+ str(k) + '.png', img)
            # print(save_path + name + "_"+ str(k) + '.png has been compeleted!')