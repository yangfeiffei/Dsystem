# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2017-02-06 14:01
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('daily', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='daily',
            name='upload_date',
            field=models.DateField(verbose_name='日期'),
        ),
    ]
