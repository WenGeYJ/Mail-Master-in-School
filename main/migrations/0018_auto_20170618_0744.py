# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2017-06-18 07:44
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0017_auto_20170618_0613'),
    ]

    operations = [
        migrations.DeleteModel(
            name='bookList',
        ),
        migrations.DeleteModel(
            name='replyTiezi',
        ),
        migrations.DeleteModel(
            name='tiezi',
        ),
    ]
