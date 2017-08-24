# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2017-08-23 13:30
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('organization', '0015_auto_20170822_1022'),
    ]

    operations = [
        migrations.AddField(
            model_name='teacher',
            name='teacher_age',
            field=models.IntegerField(default=18, verbose_name='\u5e74\u9f84'),
        ),
        migrations.AlterField(
            model_name='teacher',
            name='org',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='organization.CourseOrg', verbose_name='\u6240\u5c5e\u673a\u6784'),
        ),
    ]
