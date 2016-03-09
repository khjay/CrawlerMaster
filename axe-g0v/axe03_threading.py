# -*- coding: utf8 -*-
from lxml import etree, html
import requests, threading, uuid, time

class axe(threading.Thread):
    jsonData = ""
    def __init__(self, url, cookies):
        self.url = url
        self.cookies = cookies
        threading.Thread.__init__(self)
    def run(self):
        result = requests.post(self.url, cookies=self.cookies)
        result.encoding = 'utf-8'
        self.jsonData = retriveToJson(result)
#         print(self.jsonData)
    
def main():
    cookies = {'PHPSESSID': str(uuid.uuid4())}
    print("loading page 1")    
    axeList = []
    worker = axe("http://axe-level-1.herokuapp.com/lv3/", cookies)
    worker.start()
    axeList.append(worker)
    for i in range(1, 76):
        print("loading page %d" % (i+1))
        worker = axe("http://axe-level-1.herokuapp.com/lv3/?page=next", cookies=cookies)
        worker.start()
        axeList.append(worker)
        time.sleep(0.3)
    
    allData = '['
    for i in range(len(axeList)):
        axeList[i].join()
        allData += axeList[i].jsonData
    print(allData[0: -1] + "]")
        
        
def retriveToJson(result):
    root = etree.fromstring(result.text, etree.HTMLParser())
    tmp = ""
    for row in root.xpath("//table[@class='table']/tr[position()>1]"):
        column = row.xpath("./td/text()")
        tmp += '{"town": "%s", "village": "%s", "name": "%s"},' % (column[0], column[1], column[2])
    return tmp

if __name__ == "__main__":
    main()

