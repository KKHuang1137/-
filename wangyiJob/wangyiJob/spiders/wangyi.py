import scrapy


class WangyiSpider(scrapy.Spider):
    name = 'wangyi'
    allowed_domains = ['hr.163.com']
    start_urls = ['https://hr.163.com/']

    def parse(self, response):
        # print(response.body)
        print(response.headers)
        print(response.url)
