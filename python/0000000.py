#爬取西刺代理
import requests
import re
from bs4 import BeautifulSoup
import bs4

def getHTMLText(url,header):
    try:
        r = requests.get(url,headers = header,timeout = 30)
        r.raise_for_status()
        r.encoding = r.apparent_encoding
        return r.text
    except:
        return "程序异常1"

def parsePage(url,header,list):
    try:
        html = getHTMLText(url,header)
        soup = BeautifulSoup(html,'html.parser')
        for tr in soup.find('table').children:
            if isinstance(tr,bs4.element.Tag):
                tds = tr('td')
                list.append([tds[1].string,tds[2].string,tds[5]])
    except:
        return "程序异常2"

def printInfomation(list):
    tplt = "{:10}\t{:10}\t{:10}"
    print(tplt.format("IP地址","端口号","类型"))
    for i in range(len(list)):
        t = list[i]
        print(tplt.format(t[1],t[2],t[5]))


def main():
    depth = 3
    list =[]
    start_url = "https://www.xicidaili.com/nn/"
    header = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:69.0) Gecko/20100101 Firefox/69.0"
        }
    for i in range(depth):
        url = start_url+str(i)
    parsePage(url,header,list)
    printInfomation(list)

if __name__ == '__main__':
    main()
