# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2017-02-11 07:28
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('daily', '0004_auto_20170210_1409'),
    ]

    operations = [
        migrations.AlterField(
            model_name='daily',
            name='status',
            field=models.IntegerField(choices=[(0, '可修改'), (1, '已提交'), (2, '已锁定')], default=0, verbose_name='日报状态'),
        ),
    ]
