# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-10-10 11:16
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('learning_machine', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='page',
            old_name='name',
            new_name='body',
        ),
        migrations.AddField(
            model_name='page',
            name='title',
            field=models.CharField(default='ad', max_length=30),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='page',
            name='id',
            field=models.CharField(max_length=30, primary_key=True, serialize=False),
        ),
    ]
