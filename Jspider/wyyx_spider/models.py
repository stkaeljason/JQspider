#coding:utf-8

from django.db import models


class Good(models.Model):
    good_id = models.CharField(max_length=20,null=True)
    name = models.CharField(max_length=30,null=True)
    catcory = models.CharField(max_length=20,null=True)
    counter_price = models.CharField(max_length=20,null=True)
    gradient_price = models.CharField(max_length=20,null=True)
    price_isActived = models.CharField(max_length=20,null=True)
    price_leftTime = models.CharField(max_length=20,null=True)
    detail_data = models.TextField(null=True)
    crawl_time = models.CharField(max_length=20,null=True)
