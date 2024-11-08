import scrapy
import logging

logging.getLogger('scrapy').setLevel(logging.WARNING)


class spider1(scrapy.Spider):
    name = 'Wikipedia'
    start_urls = ['https://en.wikipedia.org/wiki/Electric_battery']

    def parse(self, response):
        print(response.css('h1#firstHeading::text').extract())
