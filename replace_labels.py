# -- coding: utf-8 --**
# @Author  : LeeYotta

import glob
import json
from tqdm import tqdm

before = input("Please input the name of labels that needs to be replaced:")
after = input("Please input the name of labels that will be replaced with:")
file_folder = input("Please input the folder that json in:") 

file_list = glob.glob(file_folder + '//' + '*.json')
for file in tqdm(file_list):
    
    with open(file, 'r') as f:
        data = json.load(f)
        shapes = data['shapes']
        for shape in shapes:
            if shape['label'] == before:
                shape['label'] = after

    with open(file, 'w') as f:
        json.dump(data, f, indent=2)


