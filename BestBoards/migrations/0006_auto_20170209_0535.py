# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-02-09 05:35
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('BestBoards', '0005_auto_20170209_0450'),
    ]

    operations = [
        migrations.RenameField(
            model_name='category',
            old_name='category',
            new_name='title',
        ),
    ]
