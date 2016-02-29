# -*- coding: utf8 -*-
from lxml import etree, html
import requests

def main():
    depts = getDepts()
    print(depts)

def getDepts():
    result = requests.get("https://www.mcu.edu.tw/student/new-query/sel-query/query_3_up.asp")
    root = etree.fromstring(result.text, etree.HTMLParser())
    meta = root.xpath("//head/meta")[0]
    charset = meta.get('content').split('=')[-1]
    result.encoding = charset
    depts = root.xpath("//select[@name='dept']/option")
    deptsMap = []
    for dept in depts:
        deptsMap.append({'name': dept.text.strip().split(' - ')[1].encode('latin1').decode('big5'), 'value': dept.get('value')})
    return deptsMap

if __name__ == "__main__":
    main()
