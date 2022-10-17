# 导入OS模块
import os

# 待搜索的目录路径
path = input("Please input the folder name:")
# 待搜索的名称
filename = input("Please input the keyword:")
# 定义保存结果的数组
result = []

result = []
for root, dirs, files in os.walk(path):
    # for dir in dirs:
    for file in files:
        if (filename in file.lower()):
            result.append(root + ":" + file)
with open("results.txt", 'a') as res:
    for i, v in enumerate(result):
        res.write(v + "\n")
