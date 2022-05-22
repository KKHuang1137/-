# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class WangyijobItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    name = scrapy.Field()  # 职位名称
    link = scrapy.Field()  # 详情链接
    depart = scrapy.Field()  # 所属部门
    category = scrapy.Field()  # 职位类别
    type = scrapy.Field()  # 工作类型
    address = scrapy.Field()  # 工作地点
    num = scrapy.Field()  # 招聘人数
    date = scrapy.Field()  # 发布时间
    education = scrapy.Field()  # 学历
    experience = scrapy.Field()  # 工作年限
    description = scrapy.Field()  # 岗位描述
    requirement = scrapy.Field()  # 岗位要求

