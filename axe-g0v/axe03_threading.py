# -*- coding: utf8 -*-
from lxml import etree, html
import requests, threading

class axe(threading.Thread):
    def __init__(self):
        threading.Thread.__init__(self)
    def run(self):
        pass
    
def main():
    jsonData = '['
    result = requests.get("http://axe-level-1.herokuapp.com/lv3/")
    result.encoding='utf-8'
    cookies = result.cookies
    jsonData += retriveToJson(result)
    for i in range(1, 76):
        result = requests.post("http://axe-level-1.herokuapp.com/lv3/?page=next", cookies=cookies)
        result.encoding = 'utf-8'
        jsonData += retriveToJson(result)
    print(jsonData[0:-1] + "]")

def retriveToJson(result):
    root = etree.fromstring(result.text, etree.HTMLParser())
    tmp = ""
    for row in root.xpath("//table[@class='table']/tr[position()>1]"):
        column = row.xpath("./td/text()")
        tmp += '{"town": "%s", "village": "%s", "name": "%s"},' % (column[0], column[1], column[2])
    return tmp

if __name__ == "__main__":
    main()

