#coding:utf-8

import sys
sys.path.append('/home/jason/myproject/JQspider/Jspider')

import json
import requests
import time
import re
from lxml import etree

from celery import task,shared_task
from celery import chain
from celery.utils.log import get_task_logger

from wyyx_spider.models import Good
logger = get_task_logger(__name__)


@task()
def fetch_page(url):
    headers = {
    'Accept':'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
    'Accept-Encoding': 'gzip, deflate',
    'Accept-Language': 'en-US,en;q=0.9,zh-CN;q=0.8,zh;q=0.7',
    'Host': 'you.163.com',
    'Referer': 'http://you.163.com/item/list?categoryId=1005000',
    'Upgrade-Insecure-Requests': 1,
    'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/62.0.3202.94 Safari/537.36'
    }
    res = requests.get(url)
    # print(res.text)
    return res.text


@task()
def parse_page(res):
    page = etree.HTML(res)
    # print(page)
    data = page.xpath('//script[contains(text(),"JSON_DATA_FROMFTL")]')[0].text
    data = data.replace('\n', '')
    pattern = re.compile(r"({.+}).*?其他数据.*?({.+})")
    goods_data = re.search(pattern, data).group(1)
    goods_dict = json.loads(goods_data)
    # print(goods_dict)
    good_item = dict()
    good_item['good_id'] = goods_dict['item']['id']
    good_item['name'] = goods_dict['item']['name']
    good_item['catcory'] = ' '.join([cate['name'] for cate in goods_dict['item']['categoryList']])
    good_item['counter_price'] = goods_dict['item']['counterPrice']
    if goods_dict['item']['gradientPrice']:
        good_item['gradient_price'] = goods_dict['item']['gradientPrice']['limitPrice']
        good_item['price_isActived'] = goods_dict['item']['gradientPrice']['isActived']
        good_item['price_leftTime'] = goods_dict['item']['gradientPrice']['leftTime']
    else:
        good_item['gradient_price'] = ''
        good_item['price_isActived'] = ''
        good_item['price_leftTime'] = ''
    good_item['detail_data'] = json.dumps(goods_dict)
    good_item['crawl_time'] = str(time.time())
    return good_item


@task()
def save_good_info(item):
    good = Good()
    good.good_id = item['good_id']
    good.name = item['name']
    good.catcory = item['catcory']
    good.counter_price = item['counter_price']
    good.gradient_price = item['gradient_price']
    good.price_isActived = item['price_isActived']
    good.price_leftTime = item['price_leftTime']
    good.crawl_time = item['crawl_time']

    good.save()


@task()
def crawl_good():
    url = 'http://you.163.com/item/detail?id=1100000&_stat_area=mod_1_item_22&_stat_id=1005000&_stat_referer=itemList'
    chain = fetch_page.s(url) | parse_page.s() | save_good_info.s()
    chain()


@shared_task
def add(x,y):
    return x+y


