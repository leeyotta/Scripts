from PIL import Image
import os
import img2pdf
 
flag = False
while not flag:
    dirname = input("请输入图片文件夹所在路径(例如d:/test)：")
    flag = os.path.exists(dirname)
    if not flag:
        print("图片文件夹所在路径不存在！")
saveflag = False
while not saveflag:
    savedirname = input("请输入目标图片文件夹所在路径(例如d:/test)：")
    saveflag = os.path.exists(savedirname)
    if not saveflag:
        print("图片文件夹所在路径不存在！")
        automakedir = input("是否自动创建对应文件夹？(是Y/否N):")
        if automakedir.strip().upper() == "Y":
            os.makedirs(savedirname)
            saveflag = True
files = os.listdir(dirname)
reductionFactor = int(input("请输入长宽压缩比(例如3):"))
if reductionFactor <= 0:
    reductionFactor = 3
isConvertBlack = input("是否输出黑白版本？(是Y/否N):").strip().upper() == "Y"
for fname in files:
    if not fname.endswith(".jpg"):
        continue
    path = os.path.join(dirname, fname)
    savePath = os.path.join(savedirname, fname)
    if os.path.isdir(path):
        continue
    img = Image.open(path)    
    if img.size[0] > img.size[1]:
        im_rotate = img.rotate(90, expand=True)
        size = (int(im_rotate.size[0] / reductionFactor), int(im_rotate.size[1] / reductionFactor))
        im_rotate = im_rotate.resize(size)
        if isConvertBlack:
            im_rotate = im_rotate.convert("L")
        im_rotate.save(savePath, quality=95)
    else:
        size = (int(img.size[0] / reductionFactor), int(img.size[1] / reductionFactor))
        img = img.resize(size)
        if isConvertBlack:
            img = img.convert("L")
        img.save(savePath, quality=95)
filename = input("请输入输出文件名：")
with open(filename + ".pdf", "wb") as f:
    imgs = []
    files = os.listdir(savedirname)
    for fname in files:
        if not fname.endswith(".jpg"):
            continue
        path = os.path.join(savedirname, fname)
        if os.path.isdir(path):
            continue
        imgs.append(path)
    f.write(img2pdf.convert(imgs))