# -*- coding: utf-8 -*-
# Generated by Django 1.11.11 on 2019-04-01 17:53
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('projectM', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='projectlist',
            name='project_type',
            field=models.CharField(choices=[('standard', '内部-标准项目'), ('Non-standard', '内部-非标项目'), ('Outgoing', '外部项目')], default='Internal', max_length=20),
        ),
    ]
