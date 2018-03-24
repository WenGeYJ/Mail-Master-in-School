# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.
from django.db import models


class Test(models.Model):
    name = models.CharField(max_length=20)

class subscribeBooks(models.Model): #书单
    user_id=models.BigIntegerField() #每一本书的用户id
    book_id=models.BigIntegerField() #每一本书对应的id

class favor(models.Model): #收藏
    user_id=models.BigIntegerField()
    book_id=models.BigIntegerField()

class student_users(models.Model):
    user_id=models.BigIntegerField(unique=True) #用户id
    user_name=models.CharField(max_length=20) #用户昵称
    name=models.CharField(max_length=20) #用户真实姓名
    phone_number=models.CharField(max_length=15) #用户手机号
    mail=models.EmailField() #用户邮箱

class message(models.Model):
    time=models.TimeField() #时间
    date=models.DateField(auto_now_add=True) #日期
    book_id=models.CharField(max_length=20) #信息

class allBook(models.Model):
    book_id = models.BigIntegerField()  # 每一本书对应的id
    ISBN=models.CharField(max_length=20) #ISBN号？ 还是什么其他的编号。。
    name=models.CharField(max_length=20) #书名
    price=models.IntegerField() #价钱
