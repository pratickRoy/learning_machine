# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-10-10 11:53
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('learning_machine', '0003_auto_20171010_1152'),
    ]

    operations = [
        migrations.AlterField(
            model_name='page',
            name='body',
            field=models.CharField(max_length=30),
        ),
        migrations.AlterField(
            model_name='page',
            name='title',
            field=models.CharField(max_length=30),
        ),
    ]