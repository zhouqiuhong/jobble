# -*- coding:utf-8 -*-
"""
@author:zhouqiuhong
@file:db.py
@time:2018/10/26 00269:56
"""
import sqlalchemy
from sqlalchemy import create_engine, Column, String, Integer, ForeignKey, Text, DateTime
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

engine = create_engine("mysql+pymysql://root:123456@172.16.1.144:3306/test?charset=utf8")
Base = declarative_base()
Session = sessionmaker(bind=engine)
session = Session()


class Article(Base):
    __tablename__ = "tb_article"
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(100), nullable=False)
    link = Column(String(300), unique=True)
    category = Column(String(30), nullable=False)
    add_time = Column(DateTime)

    def __str__(self):
        return self.name


class ArticleContent(Base):
    __tablename__ = "tb_article_content"
    id = Column(Integer, primary_key=True, autoincrement=True)
    article_id = Column(ForeignKey("tb_article.id"))
    content = Column(Text)
    name = Column(String(200))


"""
创建数据表
"""
# Base.metadata.create_all(engine)


