# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2017-02-11 07:52
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('daily', '0005_auto_20170211_0728'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='head_portrait',
            field=models.ImageField(default='daily/static/daily/default_user_head.ipg', upload_to='daily/static/daily', verbose_name='用户头像'),
        ),
    ]