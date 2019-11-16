import requests
import re
import traceback
from bs4 import BeautifulSoup

def getHTMLText(url,code = 'utf-8'):
    try:
        r = requests.get(url,timeout = 30)
        r.raise_for_status()
        r.encoding = code
        return r.text
    except:
        "程序错误1"
def getStockList(lst,stockURL):
    html = getHTMLText(stockURL,GB2312)
    soup = BeautifulSoup(html,'html.parser')
    a = soup .find_all('a')
    for i in a:
        try:
            herf = i.attrs['herf']
            lst.append(re.findall(r"[s][hz]\d[6]",herf)[0])
        except:
            continue

def getSctockInfo(lst,stockURL,fpath):
    for stock in lst:
        url = stockURl +stock +".html"
        html = getHTMLText(url)
        try:
            if html == "":
                continue
            infoDict ={}
            soup = BeautifulSoup(html,'html.parser')
            stockInfo = soup.find('div',attrs={'class':'stock_bets'})

            name = stockInfo.find_all(attrs={'class':'bets-name'})[0]
            infoDict.update({'股票名称': name.text.split()[0]})

            keyList = stockInfo.find_all('dt')
            valueList = stockInfo.find_all('dd')
            for i in range(len(keyList)):
                key = keyList[i].text
                val = valueList[i].text
                ininfoDict[key] = val

            with open(fpath,'a',encoding='utf-8')as f :
                f.write(str(infoDict)+'\n')
        except:
             ttraceback.print_exc()
             continue

def main():
    stock_list_url = 'http://quote.eastmoney.com/stocklist.html'
    stock_info_url = 'https://gupiao.baidu.com/stock/'
    output_file = 'C://Users/fair yang/Desktop/Baidu.txt'
    slist = []
    getStockList(slist,stock_list_url)
    getStockInfo(slist,stock_info_url,output_file)


if __name__ == '__main__':
    main()