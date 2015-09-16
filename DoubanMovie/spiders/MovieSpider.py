# -*- coding: utf-8 -*-

import scrapy
from scrapy.selector import Selector
from DoubanMovie.items import DoubanmovieItem
from scrapy.http import Request

class MyTest(scrapy.Spider):
    name="mytest"
    redis_key = 'douban:start_urls'
    start_urls = ['http://movie.douban.com/top250']
    url = 'http://movie.douban.com/top250'

    def parse(self, response):
        item = DoubanmovieItem()
        selector = Selector(response)
        Movies = selector.xpath('//div[@class="info"]')
        for eachMoive in Movies:
            title = eachMoive.xpath('div[@class="hd"]/a/span/text()').extract()
            fullTitle = ''
            for each in title:
                fullTitle += each
            movieInfo = eachMoive.xpath('div[@class="bd"]/p/text()').extract()
            star = eachMoive.xpath('div[@class="bd"]/div[@class="star"]/span/em/text()').extract()[0]
            quote = eachMoive.xpath('div[@class="bd"]/p[@class="quote"]/span/text()').extract()
            if quote:
                quote = quote[0]
            else:
                quote = ''
            item['title'] = fullTitle
            item['movieInfo'] = ';'.join(movieInfo)
            item['star'] = star
            item['quote'] = quote
            yield item
        nextLink = selector.xpath('//span[@class="next"]/link/@href').extract()
        if nextLink:
            nextLink = nextLink[0]
            print nextLink
            yield Request(self.url + nextLink,callback=self.parse)

