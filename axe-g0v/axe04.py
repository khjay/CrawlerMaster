# -*- coding:utf8 -*-
import requests
from lxml import etree, html

if __name__ == "__main__":
    headers = {
        "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8", 
        "User-Agent": "Mozilla/5.0 (Windows NT 6.3; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/48.0.2564.116 Safari/537.36",
        "Referer": "http://axe-level-4.herokuapp.com/lv4/"
    }
    jsonData = '['
    for i in range(1,25):
        result = requests.get("http://axe-level-4.herokuapp.com/lv4/?page=%d" % i, headers=headers)
        result.encoding='utf8'
        root = etree.fromstring(result.text, etree.HTMLParser())
        for row in root.xpath("//table[@class='table']/tr[position()>1]"):
            column = row.xpath("./td/text()")
            tople = '{"town": "%s", "village": "%s", "name": "%s"},' % (column[0], column[1], column[2])
            jsonData += tople
    print(jsonData[0:-1] + ']')
