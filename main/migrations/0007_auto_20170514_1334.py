# -*- coding: utf-8 -*-
# Generated by Django 1.11a1 on 2017-05-14 13:34
from __future__ import unicode_literals

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0006_auto_20170514_1133'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='arrivalmessage',
            name='userID',
        ),
        migrations.AddField(
            model_name='arrivalmessage',
            name='classID',
            field=models.CharField(default=1, max_length=20),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='arrivalmessage',
            name='time',
            field=models.DateField(default=django.utils.timezone.now),
        ),
    ]
