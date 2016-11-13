import time
from spider import spider
from supply import logger
from file_generator import fileGenerator

def orderSort(currentLink, workName,tag4link, class4link, tag4nextPage, class4nextPage,volume):
    link = currentLink
    while True:
        crawler = spider(link,workName)
        furtherLink = crawler.getLinks(tag4link,class4link)
        if furtherLink != None:
            for i in furtherLink:
                fileGenerator(workName,i,volume)
        link = crawler.nextPage(tag4nextPage,class4nextPage)
        if link == None:
            break
        time.sleep(1)

def linker(linkText, BigworkName, tag4link, class4link, tag4nextPage, class4nextPage, volume):
    logs = None
    workName = BigworkName + '_linker'
    file = open(linkText, 'r')
    links = file.readlines()
    file.close()
    try:
        file = open(workName+'.log', 'r')
        logs = file.readlines()
        file.close()
        logs = logs[-1]
        if '-------Programme Finished!-------' in logs:
            logs = 'end'
        else:
            logs = logs.split(' ')[2]
    except:
        pass

    if logs == None:
        logger(workName, "-------Start Programme!-------")
    elif logs == 'end':
        print("The program is finished!")
        return None
    else:
        logger(workName, "-------Restart Programme!-------")
        orderSort(logs, workName, tag4link, class4link, tag4nextPage, class4nextPage, volume)
        info = logs.split('/')[4]
        for i in range(len(links)):
            if info in links[i]:
                if i < len(links) - 1:
                    links = links[i+1:]
                else:
                    links = []
                break

    for link in links:
        link = link[:len(link)-1]
        orderSort(link, workName, tag4link, class4link, tag4nextPage, class4nextPage, volume)

    logger(workName, "-------Programme Finished!-------")

#linker('test_link.txt', 'test','div','advise_box_title','div','page_turn',5)
