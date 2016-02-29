# -*- coding: utf8 -*-
from lxml import etree, html
import requests

if __name__ == "__main__":
    for i in range(1, 12):
        result = requests.get("http://axe-level-1.herokuapp.com/lv2?page=%s" % str(i))
        result.encoding='utf8'
        root = etree.fromstring(result.text, etree.HTMLParser())
        for row in root.xpath("//table[@class='table']/tr[position()>1]"):
            column = row.xpath("./td/text()")
            print(column)
