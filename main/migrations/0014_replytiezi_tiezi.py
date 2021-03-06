# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2017-06-08 11:23
from __future__ import unicode_literals

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0013_auto_20170522_1323'),
    ]

    operations = [
        migrations.CreateModel(
            name='replyTiezi',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tieziID', models.IntegerField()),
                ('userID', models.IntegerField()),
                ('text', models.TextField()),
                ('time', models.DateField(default=django.utils.timezone.now)),
            ],
        ),
        migrations.CreateModel(
            name='tiezi',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('userID', models.IntegerField()),
                ('head', models.CharField(max_length=50)),
                ('text', models.TextField()),
                ('time', models.DateField(default=django.utils.timezone.now)),
            ],
        ),
    ]
