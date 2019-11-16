#ClaThreekingdoms.py
import jieba
txt = open("threekingdoms.txt","r",encoding="utf-8").read()
excludes={"将军","却说","荆州","二人","不可","不能","如此","左右","军马",
"大喜","引兵","次日","不敢","天下","今日","东吴","于是","陛下","不知","汉中"
,"城中","天子","大军","一面","何不","忽报","百姓","先生","商议","如何",
"主公","只见","众将","后主","魏兵","一人","军士","蜀兵","上马","大叫","此人",
"夫人","人马","太守","先主","后人","背后","何故","然后","先锋","赶来","原来",
"令人","江东","下马","不如","喊声","正是","徐州","忽然"
          }
words = jieba.lcut(txt)
counts = {}
for word in words:
    if len(word)==1:
        continue
    elif word=="孔明曰"or word=="孔明":
        rword="诸葛亮"
    elif word=="关公"or word=="云长" or word=="云长曰":
        rword="关羽"
    elif word=="玄德曰"or word=="玄德":
        rword="刘备"
    elif word=="孟德"or word=="阿瞒" or word=="丞相":
        rword="曹操"
    elif word=="都督" or word=="公瑾":
        rword="周瑜"
    else :
        rword=word
    counts[rword] = counts.get(rword,0)+1
for word in excludes:
    del counts[word]
items = list(counts.items())
items.sort(key=lambda x:x[1],reverse=True)
for i in range(15):
    word,count= items[i]
    print('{0:<10}{1:>5}'.format(word,count))
