import pdfplumber
import shutil
from os import listdir, chdir, getcwd, system, path, mkdir

chdir("./cvpr2022/")
raw_list = listdir()
print('文件总数：', len(raw_list))

while 1:
    keyword = input("请输入搜索关键字：").strip()
    insure = input("y/n")
    if insure == 'y':
        break

while 1:
    print("请选择检索模式:")
    print("1. 重新检索")
    print("2. 继续上次的检索")
    print("3. 将上次检索的结果存至关键词文件夹")
    choice = input("--->").strip()
    if choice == '1':
        filelist = listdir()
        with open("process.txt", 'w') as pro:
            pro.truncate()
        break
    elif choice == '2':
        with open("../process.txt", 'r') as pro:
            filelist = pro.read().strip().split('\n')
            for f in filelist:
                raw_list.remove(f)
        filelist = raw_list
        break
    elif choice == '3':
        with open("../process.txt", 'r') as pro:
            filelist = pro.read().strip().split('\n')
            for f in filelist:
                raw_list.remove(f)
        filelist = raw_list

        isExists = path.exists(f'../{keyword}')
        if not isExists:
            mkdir(f'../{keyword}')
        for file in filelist:
            shutil.copyfile(file, f'../{keyword}/{file}')
        system("pause")
        exit(f"{keyword}--相关文件已存储至相应文件夹！")
    else:
        print('输入错误，重新输入！')

print("剩余文件数：", len(filelist))

n = 0
ns = len(filelist)
for file in filelist:
    n += 1
    print(f"正在检索({n}/{ns})中是否含有{keyword}：\n" + file)
    with pdfplumber.open(file) as pdf:
        # firstpage = pdf.pages[0]
        # print(type(firstpage.extract_text()))
        sign = 0
        for page in pdf.pages:
            text = page.extract_text().lower()
            if keyword in text:
                with open("../result.txt", 'a+') as res:
                    res.write(keyword + '：\n' + file +
                              '\n页数:' + str(page.page_number) + '\n\n')
                print(keyword + ':\n' + file +
                      '\n页数:' + str(page.page_number) + '\n\n')
                sign = 1
                break
    if sign == 0:
        with open("../process.txt", 'a+') as pro:
            pro.write(file + '\n')
        print("无相关信息！")

system("pause")
