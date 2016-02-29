# -*- coding: utf8 -*-
from lxml import etree, html
import requests, json
if __name__ == "__main__":
    result = requests.get("http://axe-level-1.herokuapp.com/")
    result.encoding='utf8'
    root = etree.fromstring(result.content, etree.HTMLParser())
    jsonData = "["
    for row in root.xpath("//table[@class='table']/tr[position()>1]"):
        column = row.xpath("./td/text()")
        tople = '{"name": "%s", "grades": {"國語": %s, "數學": %s, "自然": %s, "社會": %s, "健康教育": %s}},' % (column[0], column[1], column[2], column[3], column[4], column[5])
        jsonData += tople
    print(jsonData[0:-1] + ']')
