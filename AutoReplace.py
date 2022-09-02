# -*- coding=utf-8 -*-
# by taiyang
# https://taiyang.space

import os
import re
import shutil


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
# 作用：判断IP地址合法性
# 参数：ipAddress
# return：合法返回True

def checkIP(ipAddress):
    compile_ip = re.compile(
        '^(1\d{2}|2[0-4]\d|25[0-5]|[1-9]\d|[1-9])\.(1\d{2}|2[0-4]\d|25[0-5]|[1-9]\d|\d)\.(1\d{2}|2[0-4]\d|25[0-5]|[1-9]\d|\d)\.(1\d{2}|2[0-4]\d|25[0-5]|[1-9]\d|\d)$')
    if compile_ip.match(ipAddress):
        return True


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
# 作用：读取当前文件夹下所有文件返回一个文件名列表
# 参数：null
# return：FileList

def readAllCfgFile():
    # 当前文件夹下所有文件名
    fileList = os.listdir('./')

    # 需要修改的配置文件
    FileList = []
    for i in fileList:
        if '.cfg' in i or '.vpc' in i:
            FileList.append(i)
    return FileList


###########################################################################################################
# 作用：删除临时创建的文件
# 参数：fileList
# return：null

def removeTempFile(fileList):
    for j in fileList:
        if 'temp' in j:
            os.remove(j)


###########################################################################################################


def main():
    cfgFileList = readAllCfgFile()  # 读取当前文件夹下所有文件

    try:
        if len(cfgFileList) == 0:
            raise UserWarning

        for i in cfgFileList:
            tempFile = 'temp' + i
            shutil.copyfile(i, tempFile)

            # 对每个配置文件都创建对应的临时文件，测试config.txt中的内容是否有误
            # 如果config.txt中的内容有误，写入前的判断会引发ValueError
            # 例：替换第1个配置文件的IP时，新的IP是合法的，合法就可以写入
            #    假设替换第2个配置的IP时，新的IP是不合法的，不能写入
            #    这时候就会出现：第1个配置文件已经被修改了，而第2个配置文件没有
            # 所以先对tempFile进行替换，如果写入所有tempFile时都没有引发ValueError
            # 那么就会对配置文件进行修改
            # 最后程序退出前调用removeTempFile()，删除所有tempFile
            # 写这段代码的时候自己都笑了，纯纯偷懒行为
            # 我始终坚持两个原则：
            #                1.只有一个中国！
            #                2.代码和我有一个能跑就行❤

            ipList = searchIP(tempFile)

            if ReadConfig():
                # 替换整个IP地址
                for j in range(len(ipList)):
                    oldString = ipList[j]
                    newString = replaceContent.get(ipList[j])
                    # 写入前判断IP是否合法
                    if checkIP(newString):
                        writeFile(tempFile, oldString, newString)
                    else:
                        raise ValueError

            else:
                # 只替换IP地址第2位
                for j in range(len(ipList)):
                    oldString = ipList[j]
                    newString = simpleReplaceIP(oldString, replaceContent)
                    # 写入前判断IP是否合法
                    if checkIP(newString):
                        writeFile(tempFile, oldString, newString)
                    else:
                        raise ValueError

    except UserWarning:
        print('请将AutoReplace.exe和config.txt和配置文件放在同一目录！')

    except ValueError:
        print('config.txt配置有误请重新配置！')

    else:
        for i in cfgFileList:

            ipList = searchIP(i)

            if ReadConfig():
                # 替换整个IP地址
                for j in range(len(ipList)):
                    oldString = ipList[j]
                    newString = replaceContent.get(ipList[j])
                    writeFile(i, oldString, newString)
            else:
                # 只替换IP地址第2位
                for j in range(len(ipList)):
                    oldString = ipList[j]
                    newString = simpleReplaceIP(oldString, replaceContent)
                    writeFile(i, oldString, newString)
        print("替换成功！")

    removeTempFile(readAllCfgFile())
    os.system('pause')


if __name__ == '__main__':
    main()
