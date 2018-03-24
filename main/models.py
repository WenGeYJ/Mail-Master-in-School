# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.
from django.db import models
import django.utils.timezone as timezone


class Book(models.Model):
    bookID = models.BigIntegerField()
    bookName = models.CharField(max_length=100)
    pictureUrl=models.URLField()
    pricePerMonth = models.FloatField()  # IntegerField()
    priceHalfYear = models.FloatField()
    pricePerYear = models.FloatField()
    cBussiness = models.CharField(max_length=20)  # 发行刊局
    standNumber = models.CharField(max_length=20)
    mailNumber = models.CharField(max_length=20)
    bookType = models.CharField(max_length=10)  # 报刊类别
    bookKind1 = models.CharField(max_length=20)  # 报刊种类1: 报纸/杂志
    bookKind2 = models.CharField(max_length=20)  # 报刊种类2: 人文科学/...
    bookKind3 = models.CharField(max_length=20)  # 报刊种类3: 教辅类报刊/...
    introduction = models.TextField()  # 简介

class StudentUser(models.Model):
    userName = models.CharField(max_length=20)
    name = models.CharField(max_length=20)
    mailBox = models.EmailField()
    phoneNumber = models.CharField(max_length=20)
    studentClass = models.CharField(max_length=20)
    studentNumber = models.CharField(max_length=20)


class SubscribedBook(models.Model): #书单
    bookID = models.BigIntegerField()
    userName = models.CharField(max_length=20)


class FavoredBook(models.Model):
    userName = models.CharField(max_length=20)
    bookID = models.BigIntegerField()


class ArrivalMessage(models.Model):
    time = models.DateField(default=timezone.now)
    classID = models.CharField(max_length=20)
    bookID = models.BigIntegerField()


class Temp(models.Model):
    classid=models.CharField(max_length=20)