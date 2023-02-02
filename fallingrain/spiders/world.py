import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule

import json

class WorldSpider(CrawlSpider):
    name = 'world'
    allowed_domains = [
        'www.fallingrain.com',
    ]
    start_urls = [
        'https://www.fallingrain.com/world/'
    ]

    rules = (
        Rule(LinkExtractor(
            allow=r'world/',
            unique=True
        ), callback='parse_item', follow=True),
    )

    def parse_item(self, response):
        item = {}
        d = zip(
            response.xpath('//table[@border="2"]/tr/th/text()').getall(),
            response.xpath('//table[@border="2"]/tr/td/text()').getall()
        )
        print(json.dumps(dict(d), indent=1))
        item['data'] = dict(d)
        #item['description'] = response.xpath('//div[@id="description"]').get()
        return item
