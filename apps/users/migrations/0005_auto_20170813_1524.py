# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2017-08-13 15:24
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0004_auto_20170530_2129'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='birday',
            field=models.DateField(blank=True, null=True, verbose_name='\u751f\u65e5'),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='mobile',
            field=models.CharField(blank=True, max_length=11, null=True),
        ),
    ]
