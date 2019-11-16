
#爬取网页通用框架
import requests
def getHTMLText(url):
    try:
        kv = {'User-Agent':'Mozilla/5.0'}
        r = requests.get(url,params=kv,timeout = 30)
        r.raise_for_status()
        r.encoding = r.apparent_encoding
        return r.text
    except:
        return "产生异常"
if __name__ ==  '__main__' :
    url = "http://www.zuihaodaxue.cn/zuihaodaxuepaiming2016.html"
    print(getHTMLText(url))