import jieba,wordcloud
f=open("习近平新时代中国特色社会主义.txt","rt",encoding='utf_8')
txt=f.read()
f.close()
w = wordcloud.WordCloud(width=1000,background_color="white",\
    font_path="msyh.ttc",height=700)
w.generate(" ".join(jieba.lcut(txt)))
w.to_file("中国特色社会主义.jpg")
