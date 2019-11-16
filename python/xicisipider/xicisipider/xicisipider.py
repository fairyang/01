#爬取西刺代理
import requests
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
        tags=soup.find_all("a",attrs={"target":"_self"})
        for tag in tags:
            
            list.append([tag.text])
    except:
        return "程序异常2"

def printInfomation(list):
    tplt = "{0:^5},{1:^10}"
    print(tplt.format("序号","名字"))
    count =0
    for i in range(len(list)):
        count =count+1
        print (count,list[i])

def main():
    list =[]
    url = "https://b.faloo.com/f/642894.html"
    header = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:69.0) Gecko/20100101 Firefox/69.0"
        }
    parsePage(url,header,list)
    printInfomation(list) 

if __name__ == '__main__':
    main()