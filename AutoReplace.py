# -*- coding=utf-8 -*-
# by taiyang
# https://taiyang.space

import os
import re


###########################################################################################################
# 作用：读取config.txt的内容，返回一个字典replaceContent；并判断是进行简单替换IP地址还是完全替换IP地址
# 参数：null
# return：返回True即完全替换IP地址

def ReadConfig():
    f = open('config.txt', 'r', encoding='utf-8')
    # 替换的内容
    global content
    content = f.readlines()
    f.close()

    global replaceContent

    if len(content) > 1:
        global tempContent
        tempContent = []
        for i in content:
            tempContent.append((i.strip()).split('->'))

        # 转换成字典
        replaceContent = {}
        for i in range(len(tempContent)):
            replaceContent[tempContent[i][0]] = tempContent[i][1]

        return True
    else:
        replaceContent = '.'.join(content)


###########################################################################################################
# 作用：查找所有文件中所有IP
# 参数：null
# return：列表

def searchIP(fileName):
    with open(fileName, encoding='utf-8') as fh:
        fstring = fh.read()

    # declaring the regex pattern for IP addresses
    pattern = re.compile(
        r'(?<![\.\d])(?:25[0-5]\.|2[0-4]\d\.|[01]?\d\d?\.){3}(?:25[0-5]|2[0-4]\d|[01]?\d\d?)(?![\.\d])')

    match = re.findall(pattern, fstring)
    ipList = []
    # 删除子网掩码
    for i in match:
        if '255' not in i:
            ipList.append(i)

    return ipList


###########################################################################################################
# 作用：简单替换IP地址，只修改IP地址的第二位
# 参数：
# return：替换成功返回1

def simpleReplaceIP(old_str, char):
    temp = old_str.split('.')
    temp[1] = char
    new_str = '.'.join(temp)

    return new_str


###########################################################################################################
# 作用：写入
# 参数：file, old_str, new_str
# return：null

def writeFile(file, old_str, new_str):
    file_data = ""
    with open(file, "r", encoding="utf-8") as f:
        for line in f:
            if old_str in line:
                line = line.replace(old_str, new_str)
            file_data += line
    with open(file, "w", encoding="utf-8") as f:
        f.write(file_data)


###########################################################################################################


def main():
    # 当前文件夹下所有文件名
    fileList = os.listdir('./')

    # 需要修改的配置文件
    cfgFileList = []
    for i in fileList:
        if '.cfg' in i or '.vpc' in i:
            cfgFileList.append(i)

    for i in cfgFileList:
        if ReadConfig():
            # 替换整个IP地址
            ipList = searchIP(i)
            for j in range(len(ipList)):
                oldString = searchIP(i)[j]
                newString = replaceContent.get(ipList[j])
                writeFile(i, oldString, newString)
        else:
            # 只替换IP地址第2位
            for j in range(len(searchIP(i))):
                oldString = searchIP(i)[j]
                newString = simpleReplaceIP(oldString, replaceContent)
                writeFile(i, oldString, newString)

    print("替换成功！")


if __name__ == '__main__':
    main()
