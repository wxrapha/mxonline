# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2017-08-13 14:40
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('organization', '0010_auto_20170811_2257'),
    ]

    operations = [
        migrations.AlterField(
            model_name='teacher',
            name='org',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='organization.CourseOrg', verbose_name='\u6240\u5c5e\u673a\u6784'),
        ),
    ]
