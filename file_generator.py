import os
import time
from supply import textSort

def fileGenerator(workName, data, volume = 2000):
    d = os.getcwd() + '/' + workName
    if not os.path.exists(d):
        os.mkdir(d)
    fileList = os.listdir(d)
    fileList = list(filter(lambda x: workName in x,fileList))
    fileList = textSort(fileList)
    if len(fileList) == 0:
        file = open(d + '/' + workName + '1.txt','a')
    else:
        filename = fileList[-1]
        file = open(d + '/' + filename,'r')
        content = file.readlines()
        file.close()
        if len(content) < volume:
            file = open(d + '/' + filename,'a')
            file.write(data + '\n')
            file.close()
        else:
            number = len(fileList) + 1
            file = open(d + '/' + workName + str(number) + '.txt','a')
            file.write(data + '\n')
            file.close()

def filePicker(BigworkName, folder, position):
    d = os.getcwd() + '/' + folder
    while True:
        if os.path.exists(d):
            break
        else:
            time.sleep(1)

    fileList = os.listdir(d)
    fileList = list(filter(lambda x: BigworkName in x,fileList))
    fileList = textSort(fileList)
    while True:
        if len(fileList) > position[0]:
            break
        else:
            file = open(folder+'.log','r')
            logs = file.readlines()[-1]
            file.close()
            if '-------Programme Finished!-------' in logs:
                return None
            time.sleep(20)
    while True:
        file = open(d + '/' + fileList[position[0]], 'r')
        content = file.readlines()
        file.close()
        if len(content) > position[1]:
            target = content[position[1]]
            break
        else:
            file = open(folder+'.log','r')
            logs = file.readlines()[-1]
            file.close()
            if '-------Programme Finished!-------' in logs:
                return None
            time.sleep(20)
    return target

def textGenerator(workName, data, type, position, volume, number = 0):
    d = os.getcwd() + '/' + workName
    if not os.path.exists(d):
        os.mkdir(d)
    file = open(d + '/' + workName + str(position[0]+1) + '.txt', 'a')
    if position[1] == 0 and number == 1:
        file.write('<?xml version="1.0" encoding="UTF-8"?>\n'+
                   '<plist version="1.0">\n'+
                    '<dict>\n')
    file.write('<' + type + '>\n')
    file.write(data)
    file.write('</' + type + '>\n')
    if position[1] == volume - 1:
        file.write('</dict>\n'+'</plist>')
    file.close()
