from bs4 import BeautifulSoup
from supply import logger
import requests

def getAbsoluteURL(baseUrl, source):
    if source.startswith("http://"):
        url = source
    elif source.startswith("www."):
        url = "http://"+source
    else:
        url = baseUrl+source
    return url

class spider:
    def __init__(self, url, workName):
        self.baseUrl = 'http://'+ url.replace('http://','').split('/')[0]
        self.url = getAbsoluteURL(self.baseUrl, url)
        self.workName = workName
        headers = {
            'Connection': 'Keep-Alive',
            'Accept': 'text/html, application/xhtml+xml, */*',
            'Accept-Language': 'en-US,en;q=0.8,zh-Hans-CN;q=0.5,zh-Hans;q=0.3',
            'User-Agent': 'Mozilla/5.0 (Windows NT 6.3; WOW64; Trident/7.0; rv:11.0) like Gecko'                }
        try:
            response = requests.get(self.url,headers=headers,timeout=2)
            self.bsObj = BeautifulSoup(response.text,'lxml')
            logger(self.workName, "Crawl:  " + self.url + ' Done.')
        except:
            try:
                response = requests.get(self.url,headers=headers,timeout=10)
                self.bsObj = BeautifulSoup(response.text,'lxml')
                logger(self.workName, "Crawl:  " + self.url + ' Done.')
            except:
                self.bsObj = None
                logger(self.workName, "Crawl:  " + self.url + ' Failed.')

    def getLinks(self, tag, Class):
        links = list()
        if self.bsObj == None:
            return None
        target_list = self.bsObj.findAll(tag, {'class':Class})
        if len(target_list) != 0:
            for i in target_list:
                a_list = i.findAll('a')
                if len(a_list) != 0:
                    for j in a_list:
                        try:
                            if 'href' in j.attrs:
                                link = getAbsoluteURL(self.baseUrl, j.attrs['href'])
                                links.append(link)
                        except:
                            continue
        if len(links) == 0:
            return None
        else:
            return links

    def nextPage(self, tag, Class):
        Next = None
        if self.bsObj == None:
            return None
        target_list = self.bsObj.findAll(tag, {'class':Class})
        if len(target_list) != 0:
            for i in target_list:
                a_list = i.findAll('a')
                if len(a_list) != 0:
                    for j in a_list:
                        try:
                            if '下一页' in j.get_text():
                                Next = getAbsoluteURL(self.baseUrl, j.attrs['href'])
                        except:
                            continue
        return Next
    def getText(self,tag,Class):
        text_links = list()
        if self.bsObj == None:
            return None
        target_list = self.bsObj.findAll(tag, {'class':Class})
        if len(target_list) != 0:
            for i in target_list:
                try:
                    text_links.append(i.get_text())
                except:
                    continue
        if len(text_links) == 0:
            return None
        else:
            return text_links

    def write(self, name):
        file = open(name+'.html','w')
        file.write(str(self.bsObj))
        file.close()

