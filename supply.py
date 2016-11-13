import time
ISOTIMEFORMAT='%Y-%m-%d %X'

def logger(name = 'crawler', process = None):
    T = time.strftime(ISOTIMEFORMAT, time.localtime())
    file = open(name+'.log', 'a')
    file.write(T+'\n')
    file.write(process+'\n')
    file.close()

def fileCleaner(txt):
    file = open(txt,'r')
    content = file.readlines()
    file.close()
    clean_content = list()
    file = open(txt.split('.')[0]+'_clean.txt','a')
    for i in content:
        if i not in clean_content:
            clean_content.append(i)
            file.write(i)
    file.close()

def textSort(List):
    lenth = len(List)
    while lenth > 0:
        for i in range(lenth - 1):
            crt = eval(''.join(list(filter(str.isdigit,List[i]))))
            nxt = eval(''.join(list(filter(str.isdigit,List[i+1]))))
            if crt > nxt:
                buf = List[i]
                List[i] = List[i+1]
                List[i+1] = buf
        lenth = lenth - 1
    return List

