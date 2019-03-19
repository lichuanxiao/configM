# -*- coding: utf-8 -*-
# Generated by Django 1.11.11 on 2019-03-18 11:06
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('repoM', '0003_systemconfig'),
    ]

    operations = [
        migrations.AddField(
            model_name='systemconfig',
            name='sys_api_url',
            field=models.URLField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='systemconfig',
            name='sys_privatetoken',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='systemconfig',
            name='sys_description',
            field=models.TextField(max_length=200),
        ),
        migrations.AlterField(
            model_name='systemconfig',
            name='sys_type',
            field=models.CharField(choices=[('git', 'Git 源码管理系统'), ('svn', 'SVN 源码管理系统'), ('jenkins', 'Jenkins 构建服务'), ('nexus', 'Nexus 依赖管理系统'), ('others', '其他项目管理系统')], max_length=20),
        ),
    ]
