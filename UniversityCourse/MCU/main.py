# -*- coding: utf8 -*-
from lxml import etree, html
import requests, json
from time import sleep

def main():
    depts = getDepts()
    rawData = []

    for dept in depts:
        course = getCourse(dept['value'])
        deptData = {}
        deptData['科系'] = dept['name']
        if course != "no data":
            deptData['課程'] = course
        rawData.append(deptData)
    print(json.dumps(rawData, ensure_ascii=False))

def getCharset(root):
    meta = root.xpath("//head/meta")[0]
    return meta.get('content').split('=')[-1]

def getDepts():
    result = requests.get("http://www.mcu.edu.tw/student/new-query/sel-query/qslist.asp")
    root = etree.fromstring(result.text, etree.HTMLParser())
    result.encoding = getCharset(root)
    depts = root.xpath("//select[@name='dept1']/option")
    deptsMap = []
    for dept in depts[1:]:
        deptsMap.append({'name': latinToBig5(dept.text.strip().split(' - ')[1]), 'value': dept.get('value').strip()})
    return deptsMap

def getCourse(dept):
    courses = []
    result = requests.get("http://www.mcu.edu.tw/student/new-query/sel-query/qslist_1.asp", data={'dept1': dept})
    root = etree.fromstring(result.text, etree.HTMLParser())
    result.encoding = getCharset(root)
    table = root.xpath("//table/tr")
    if len(table) == 0:
        return 'no data'
    headers = table[0].xpath("./td/font")
    for row in table[1:]:
        columns = row.xpath("./td/font | ./td/a/font")
        tmp = {}
        for i in range(len(columns)):
            if type(columns[i].text).__name__ == "NoneType":
                tmp[latinToBig5(headers[i].text)] = ""
            else:
                tmp[latinToBig5(headers[i].text)] = latinToBig5(columns[i].text.strip())
        courses.append(tmp)
    sleep(1)
    return courses

def latinToBig5(s):
    return s.encode('latin1', 'ignore').decode('big5', 'ignore')
        
if __name__ == "__main__":
    main()
