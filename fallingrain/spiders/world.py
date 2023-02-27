import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule

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
			allow=r'/world/MO/',
			# unique=True
		), callback='parse_item', follow=True),
	)

	def parse_item(self, response):
		item = {}
		if response.url.endswith('html'):
			d = zip(
				response.xpath('//table[@border="2"]/tr/th/text()').getall(),
				response.xpath('//table[@border="2"]/tr/td/text()').getall()
			)
			item['data'] = dict(d)
		return item
