# -*- coding: utf-8 -*-
import scrapy


class XicidailiSpider(scrapy.Spider):
    name = 'xicidaili'
    allowed_domains = ['xicidail.com']#允许采集的域名
    start_urls = ['http://xicidail.com/nn/1']#开始采集的网站

    def parse(self, response):
        selectors = response.xpath('//tr')
        for selector in selectors:
              ip = selector.xpath('./td[2]/text()').get()
              port = selector.xpath('./td[3]/text()').get()
              print(ip,port)
