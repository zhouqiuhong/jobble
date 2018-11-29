# -*- coding:utf-8 -*-
"""
@author:zhouqiuhong
@file:douban.py
@time:2018/10/26 002611:05
"""
import scrapy


class DoubanSpider(scrapy.Spider):
    name = "douban"
    allowed_domains = "www.douban.com"
    start_urls = []

    def start_requests(self):
        yield scrapy.FormRequest()
