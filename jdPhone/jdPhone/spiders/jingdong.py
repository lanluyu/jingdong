# -*- coding: utf-8 -*-
from scrapy import Request,Spider
from jdPhone.items import JdphoneItem

class JingdongSpider(Spider):
    name = 'jingdong'
    # allowed_domains = ['www.jingdong.com']
    base_url = 'https://search.jd.com/Search?keyword=手机&enc=utf-8'

    def start_requests(self):    
        for page in range(1, 101):
            yield Request(url = self.base_url,callback=self.parse,meta={'page':page},dont_filter=True)

    def parse(self, response):
        print('Begin parse',response.url)
        products = response.xpath('.//ul[@class="gl-warp clearfix"]/li')
        for product in products:
            item = JdphoneItem()
            item['name'] =''.join(product.xpath('.//div[@class="p-name p-name-type-2"]/a/em/text()').extract()).strip()
            item['price'] = ''.join(product.xpath('.//div[@class="p-price"]/strong/*/text()').extract()).strip()
            item['store'] = ''.join(product.xpath('.//div[@class="p-shop"]/span/a/text()').extract()).strip()
            item['evaluate_num'] = ''.join(product.xpath('.//div[@class="p-commit"]/strong/a/text()').extract()).strip()+''.join(product.xpath('.//div[@class="p-commit"]/strong/text()').extract()).strip()
            yield item
            print(item)

