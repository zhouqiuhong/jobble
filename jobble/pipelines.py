# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
from .db import Article, ArticleContent, session


class JobblePipeline(object):
    def process_item(self, item, spider):
        print(len(item['title']))
        item_title_length = len(item['title'])

        # session.query(Article).all()
        # session.add(article)
        for i in range(item_title_length):
            article = Article(name=item['title'][i], link=item['article_url'][i], category=item['category'][i],
                              add_time=item['article_time'][i])
            session.add(article)
            session.commit()
        session.close()


        return item
