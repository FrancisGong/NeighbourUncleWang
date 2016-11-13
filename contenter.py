import time
from spider import spider
from supply import logger
from file_generator import *

def contenter(BigworkName, tag4pat, class4pat, tag4doc, class4doc, volume):
    folder = BigworkName + '_linker'
    workName = BigworkName + '_content'
    position = [0,0]
    logs = None

    try:
        file = open(workName+'.log', 'r')
        logs = file.readlines()
        file.close()
        logs = logs[-1]
        if '-------Programme Finished!-------' in logs:
            logs = 'end'
        else:
            logs = logs.split(' ')       # current finished position: file # line #
            logs = [int(logs[4]) - 1,int(logs[6]) - 1]
    except:
        pass

    if logs == None:
        logger(workName, "-------Start Programme!-------")
    elif logs == 'end':
        print("The program is finished!")
        return None
    else:
        logger(workName, "-------Restart Programme!-------")
        position = logs

    while True:
        link = filePicker(BigworkName, folder, position)
        if link == None:
            break
        else:
            link = link.replace('\n','')
        crawler = spider(link,workName)
        logger(workName, 'Current finished position: file ' + str(position[0] + 1) + ' line ' + str(position[1] + 1))
        text_patiant = crawler.getText(tag4pat, class4pat)[0]
        if text_patiant != None:
            text_doctor = crawler.getText(tag4doc, class4doc)[0]
            if text_doctor != None:
                textGenerator(workName, text_patiant, 'pat', position, volume, 1)
                textGenerator(workName, text_doctor, 'doc', position, volume)
        if position[1] == volume - 1:
            position[0] += 1
            position[1] = 0
        else:
            position[1] += 1
        time.sleep(1)

#contenter('test', 'div','h_s_info_cons', 'div','h_s_cons_docs', 5)
