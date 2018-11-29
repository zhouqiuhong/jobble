# -*- coding: utf-8 -*-
import re
import scrapy
from scrapy.loader import ItemLoader
from jobble.items import JobbleItem


class JobbleSpider(scrapy.Spider):
    name = 'Jobble'
    allowed_domains = ['blog.jobble.com']

    start_urls = ["http://blog.jobbole.com/all-posts/"]

    def parse(self, response):
        item_loader = ItemLoader(item=JobbleItem(), response=response)
        item_loader.add_xpath("title", "//div[@id='archive']//div[@class='post-meta']/p/a[1]/@title")
        item_loader.add_xpath("name", "")
        # return item_loader.load_item()

        item = JobbleItem()
        title = response.xpath("//div[@id='archive']//div[@class='post-meta']/p/a[1]/@title").extract()
        item['title'] = title
        article_url = response.xpath("//div[@id='archive']//div[@class='post-meta']/p/a[1]/@href").extract()
        item['article_url'] = article_url
        add_time = response.xpath("//div[@id='archive']//div[@class='post-meta']/p/text()").extract()
        article_time = [re.sub(r"[\r\n\t\s·, ]+", "", i) for i in add_time]
        article_time = [j for j in article_time if j != ""]
        item['article_time'] = article_time
        category = response.xpath("//div[@id='archive']//div[@class='post-meta']/p/a[@rel='category tag']/text()").extract()
        item['category'] = category
        next_num = response.xpath("//span[@class='page-numbers current']/text()").extract()
        # print(next_num)
        current_num = int(next_num[0])
        next_nums = current_num+1
        next_url = "http://blog.jobbole.com/all-posts/page/" + str(next_nums)
        yield scrapy.Request(next_url, dont_filter=True, callback=self.parse)
        yield item
        # for url in article_url:
        #     yield scrapy.Request(url=url, dont_filter=True, callback=self.parse_article, meta={"item": item})

    @staticmethod
    def parse_article(self, response):
        # print(response.meta['item'])
        items = JobbleItem()
        items['title'] = response.meta['item']['title']
        items['article_url'] = response.meta['item']['article_url']
        items['article_time'] = response.meta['item']['article_time']
        items['category'] = response.meta['item']['category']
        content = response.xpath("//div[@class='grid-8']//div[@class='entry']/p/text()").extract()
        items['content'] = "".join(content)
        print(items['content'])
        # yield items