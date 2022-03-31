#!/usr/bin/python3
##
## Usage : python3 ./extract.py [folder] [filename]
## Example : python3 ./extract.py ./ report_ideal_timing.rpt.sum
##
#############################################
import re,os,sys
from decimal import Decimal
import pandas as pd
# 用input让用户输入目录
diretory = sys.argv[1]
# 用input让用户再输入文件内容
input_content1 = sys.argv[2]
input_content2 = sys.argv[3]
# python获取目录下文件夹名称
dirs = os.listdir(diretory)
#遍历所有文件夹下的文件
def walk_files(path,endpoint=None):
    file_list = []
    for root, dirs, files in os.walk(path):
        for file in files:
            file_path = os.path.join(root,file)
            if file_path.endswith(endpoint):
                file_list.append(file_path)
    return file_list
if __name__ == '__main__':
    # wav_path = diretory
    text_lists = walk_files(diretory, endpoint=".sum")
    #匹配相应文件使用正则表达式
    number1_list = []
    number2_list = []
    for text_list in text_lists:
        with open(text_list) as file:
            r = file.read()
            regex = re.compile(r' +(\*.+?(\S+).+?(\S+)[\s\S]+?)')
            names = regex.findall(r)
            number1 = Decimal(names[1][1])
            number2 = Decimal(names[1][2])
            number1_list.append(number1)
            number2_list.append(number2)
    # 判断提取内容并用Excel表格导出
    if input_content1 == names[1][1] and input_content2 == names[1][2]:
        data = [(dirs[2], number1_list[0], number2_list[0]),
                (dirs[3], number1_list[1], number2_list[1]),
                (dirs[4], number1_list[2], number2_list[2])]
        df = pd.DataFrame(data, columns=['a', 'b', 'c']).to_excel('out.xlsx', )
 