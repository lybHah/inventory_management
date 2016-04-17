# coding=utf-8

from django.db import models
from uuid import uuid1


# 现在django不能用lambda来干着活了
def make_product_key():
    return uuid1().hex[:16]


class Statistics(models.Model):

    product_key = models.CharField(unique=True, max_length=32, default=make_product_key, blank=False)
    name = models.CharField(default='', max_length=128, blank=False, null=False)
    total = models.IntegerField(default=0)
    total_price = models.FloatField(default=0)

    def __unicode__(self):
        return self.product_key


class BaseProduct(models.Model):

    class Meta:
        abstract = True

    product_type = models.CharField(max_length=128, default=make_product_key, blank=False)
    name = models.CharField(max_length=128, default='', blank=False, null=False)
    buy_in = models.IntegerField(default=0)
    price = models.FloatField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)

    def __unicode__(self):
        return self.name


class ElectronicProduct(BaseProduct):

    # 产品型号
    model = models.CharField(max_length=128, default='', blank=True, null=True)


class OfficeProduct(BaseProduct):
    pass
