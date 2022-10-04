# -- coding: utf-8 --**
# @Author  : LeeYotta

"""
A Script to realize json2mask.

Step 1: ensure Anaconda3 has been installed in your PC and pip install labelme.
Step 2: change current path to labelme_json_to_dataset.exe in line_22 to yours.
Step 3: drag this Script in the json_file's parent folder.

Then you can use this Script to realize json2mask.

Way1: Open Terminal in the json_file's parent folder then input "python json2mask.py".
Way2: open in IDE then click to run. 
"""
import os
import glob
folder_name = input("Input the folder name: ")
path = os.getcwd()+'\\'+folder_name  # path to json_file
json_file = glob.glob(os.path.join(path, "*.json"))
for file in json_file:
    os.system("D:\Anaconda3\Scripts\labelme_json_to_dataset.exe " + file)