# -*- coding: utf-8 -*-
# Generated by Django 1.11.11 on 2019-03-26 17:32
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('repoM', '0007_auto_20190326_1442'),
    ]

    operations = [
        migrations.RenameField(
            model_name='coderepo',
            old_name='rpeo_description',
            new_name='repo_description',
        ),
    ]
