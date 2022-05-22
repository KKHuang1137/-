import scrapy
from wangyiJob.items import WangyijobItem


class WangyiSpider(scrapy.Spider):
    name = 'wangyi'
    allowed_domains = ['hr.163.com']
    start_urls = ['https://hr.163.com/position/list.do?currentPage=1']
    count = 1

    def parse(self, response):
        infos = response.xpath('//tbody/tr[not(@id)]')
        # print(infos)
        # 提取信息
        for info in infos:
            item = WangyijobItem()
            item['name'] = info.xpath('./td[1]/a/text()').extract_first()  # 职位名称
            item['link'] = response.urljoin(info.xpath('./td[1]/a/@href').extract_first().strip())  # URL拼接，职位链接
            item['depart'] = info.xpath('./td[2]/text()').extract_first()  # 所属部门
            item['category'] = info.xpath('./td[3]/text()').extract_first().strip()  # 职位类别
            item['type'] = info.xpath('./td[4]/text()').extract_first().strip()  # 工作类型
            item['address'] = info.xpath('./td[5]/text()').extract_first().strip()  # 工作地点
            item['num'] = info.xpath('./td[6]/text()').extract_first().strip()  # 招聘人数
            item['date'] = info.xpath('./td[7]/text()').extract_first().strip()  # 发布时间

            # print(item)
            # print("="*50)
            yield scrapy.Request(url=item['link'], callback=self.parse_detail_page, meta={'item': item})
            break

        next_page = response.xpath('//div[@class="m-page"]/a/@href').extract()[-1]
        if next_page != "javascript:void(0)":
            # print(next_page)
            next_page = response.urljoin(next_page)
            yield scrapy.Request(url=next_page, callback=self.parse)

    @staticmethod
    def parse_detail_page(response):
        print("enter detail page")
        item = response.meta['item']
        # 学历要求
        item['education'] = response.xpath(
            '//table[@class="job-params"]//tr[2]/td[2]/text()').extract_first()
        # 工作经验
        item['experience'] = response.xpath(
            '//table[@class="job-params"]//tr[2]/td[3]/text()').extract_first()

        # 职责描述
        description = response.xpath(
            '//div[@class="detail-section"][1]/div[@class="section-content"]/text()').extract()
        item['description'] = "，".join(description).replace("\xa0", " ")

        # 岗位要求
        requirement = response.xpath(
            '//div[@class="detail-section"][2]/div[@class="section-content"]/text()').extract()
        item['requirement'] = "，".join(requirement).replace("\xa0", " ")
        print(item)
        print("=" * 50)
        yield item


