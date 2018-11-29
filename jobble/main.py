# -*- coding:utf-8 -*-
"""
@author:zhouqiuhong
@file:main.py
@time:2018/10/25 002515:04
"""
import os
import sys
from scrapy.cmdline import execute


sys.path.append(os.path.dirname(os.path.abspath(__file__)))
if __name__ == "__main__":
    execute(["scrapy", "crawl", "Jobble"])