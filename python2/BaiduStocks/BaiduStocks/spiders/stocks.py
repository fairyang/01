# -*- coding: utf-8 -*-
import scrapy
import re


class StocksSpider(scrapy.Spider):
    name = 'stocks'
    #allowed_domains = ['baidu.com']
    start_urls = ['http://quote.eastmoney.com/stocklist.html']

    def parse(self, response):
        for herf in response.css('a::attr(href)').extract():
            try:
                stock = re.findall(r"[s][hz]\d{6}",herf)[0]
                url = 'http://gupiao.baidu.com/stock/'+stock+'.html'
                yield scrapy.Request(url,callback=self.parse_stock)                
            except:
                continue
    def parse_stock(self,response):
        infoDict = {}
        stockInffo = response.css('.stock-bets')
        name = stockInfo.css('.bets-name').extracts()[0]
        keyList = stockInfo.css('dt').extract()
        valueList = stockInfo.css('dd').extract()
        for i in range(len(keyList)):
            key = re.findall(r'>.*</dt>',keyList[i])[0][1:-5]
            try:
                val = re.findall(r'\d+\.?.*</dd>',valueList[i])[0][0:-5]
            except:
                val = '--'
            infoDict[key]=val

        infoDict.update(
            {'股票名称': re.findall('\s.\*\(',name)[0].split()[0]+\
             e.findall('\>.*\<',name)[0][1:-i]})
        yield infoDict
        
             
                                              
        
        
