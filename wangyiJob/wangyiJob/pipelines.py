# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter
import json


class WangyijobPipeline:
    def process_item(self, item, spider):
        return item
    
    
# 将⽂件保存为json格式
class WangyijobJsonPipeline(object):

    def __init__(self, fpath="./tmp.json"):
        self.handler = None
        self.fpath = fpath
        
    def open_spider(self, spider):
        self.handler = open(self.fpath, 'w')
        self.handler.write('[')

    def close_spider(self, spider):
        self.handler.write(']')
        self.handler.close()

    def process_item(self, item, spider):
        line = json.dumps(dict(item), ensure_ascii=False)
        self.handler.write(line)
        self.handler.write(',\n')
        return item

