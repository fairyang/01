import re
import requests
  
def getHTMLText(url,header):
    try:
        r = requests.get(url,headers=header,timeout=30)
        r.raise_for_status()
        r.encoding = r.apparent_encoding
        return r.text
    except:
        return ""
  
  
      
def parsePage(ilt,html):
    try:
        plt = re.findall(r'\"view_price\"\:\"[\d\.]*\"',html)
        tlt = re.findall(r'\"raw_title\"\:\".*?\"',html)
        for i in range(len(plt)):
            price = eval(plt[i].split(":")[1])
            title = eval(tlt[i].split(":")[1])
              
            ilt.append([price,title])
    except:
        print("爬取失败")
def printGoodsList(ilt):
    tplt = "{:4}\t{:8}\t{:16}"
    print(tplt.format("序号","价格","商品名称"))
    count = 0
    for g in ilt:
        count =count+1
        print(tplt.format(count,g[0],g[1]))

  
def main():
    goods = "书包"
    depth= 2
    header =  {"Cookie":'thw=cn; miid=1520094106408897885; t=68aa69839a1b355f1cce6e0ebea36132; cna=vJowFvn97gcCAXSy7701zrM9; l=dBPlGuBgq6UzwmpEBOCZcuIRHo_TTIOYYuPRwJTBi_5Zc68wiVQOkGVdRFJ6csWftuLB4IqguYp9-etkihX_Ju--g3fPdxDc.; isg=BHZ2nk3KN2rbesOMvHMqedzqxKy4P5D1snOPNuBfOdn9Ixa9SCbV4NrRPz_qkLLp; _m_h5_tk=09040589c3a13f5e7e2a3d6e9819082a_1571468352901; _m_h5_tk_enc=3882fd8ce12c699347f6ea7b5b08a566; cookie2=19450729718afca44a62f7b3c5f6f543; v=0; _tb_token_=ee7915eb77e8e; unb=4215913327; uc1=cookie15=U%2BGCWk%2F75gdr5Q%3D%3D&cookie14=UoTbnKZXOBa4dA%3D%3D; uc3=lg2=UtASsssmOIJ0bQ%3D%3D&id2=Vy65VYYkyL3J6w%3D%3D&nk2=F5RFgtC0yJl3sQ%3D%3D&vt3=F8dByucnLdQZe3oBKMg%3D; csg=25f851f5; lgc=tb02201579; cookie17=Vy65VYYkyL3J6w%3D%3D; dnk=tb02201579; skt=458366b9522e4503; existShop=MTU3MTU0NjEwOQ%3D%3D; uc4=nk4=0%40FY4O63f9q4myohs1ytrCTfQYNH3V&id4=0%40VXkeq1qb9HyEgEaQPk5nHjO5MVWx; tracknick=tb02201579; _cc_=W5iHLLyFfA%3D%3D; tg=0; _l_g_=Ug%3D%3D; sg=975; _nk_=tb02201579; cookie1=AC4EomjsoGwbphP1PVein5%2BiLYP3dDN9cPJsK0zThik%3D; enc=pG7AQVbpS20ZZMFdb17QBi04cdXse7apU1VnG4jRaoiZfWNBZdqyoDVZRuZ8kUCJj1VZfhgmKlWS4br%2FcBWAyA%3D%3D; JSESSIONID=038DCEC0AA6831D21C9A44D5A3D28F05; mt=ci=6_1; hng=CN%7Czh-CN%7CCNY%7C156; x=e%3D1%26p%3D*%26s%3D0%26c%3D0%26f%3D0%26g%3D0%26t%3D0; swfstore=6769; alitrackid=www.taobao.com; lastalitrackid=www.taobao.com; whl=-1%260%260%260',
        "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:69.0) Gecko/20100101 Firefox/69.0"
    }
    start_url = "https://s.taobao.com/search?q="+goods
    infoList = []
    for i in range(depth):
        try:
            url = start_url +"&s=" +str(44*i)
            html = getHTMLText(url,header)
            print(html)
            parsePage(infoList,html)
        except:
            continue
    printGoodsList(infoList)           

main()