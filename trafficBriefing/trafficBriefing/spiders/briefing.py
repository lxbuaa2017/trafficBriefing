# -*- coding: utf-8 -*-
import scrapy
from scrapy import Request
from scrapy.selector import Selector

from trafficBriefing.items import TrafficbriefingItem


class BriefingSpider(scrapy.Spider):
    name = 'briefing'
    allowed_domains = ['www.nmc.cn']
    start_urls = ['http://www.nmc.cn/publish/traffic.html']

    def start_requests(self):
        yield Request(self.start_urls[0], callback=self.parse)


    def parse(self, response):
        sel = Selector(response)
        urls = sel.xpath("//*[@id=\"text\"]/div[3]/div/img/@src").extract()
        strs = sel.xpath(
            "/html/body/div[@class='container']/div[@class='row']/div[@class='col-xs-10']/div[@class='bgwhite'][2]/div[@id='text']/div[@class='writing']/p//text()").extract()

        strs = strs[2:]
        flag = 0
        index = 0
        snow = strs[0]
        for i, str in enumerate(strs):
            if str[0] == "受":
                flag = flag + 1
                continue
            if flag > 1:
                strs = strs[i - 1:]
                break
            snow += str + '\n'
        fog = strs[0] + '\n'
        flag = 0
        for i, str in enumerate(strs):
            if str[0] == "受":
                flag = flag + 1
                continue
            if flag > 1:
                strs = strs[i - 1:]
                break
            fog += str + '\n'
        thunder = strs[0] + '\n'
        for i, str in enumerate(strs):
            if str[0] == "受":
                continue
            thunder += str + '\n'
        print(snow)
        print(fog)
        print(thunder)
        # 生成item
        item = TrafficbriefingItem()
        item['influence_snow'] = snow
        item['influence_fog'] = fog
        item['influence_thunder'] = thunder
        item['img_urls'] = urls

        yield item