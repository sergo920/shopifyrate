# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-07-06 21:11
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shopifyrate_app', '0002_auto_20170624_1414'),
    ]

    operations = [
        migrations.AddField(
            model_name='authappshopuser',
            name='facebook_token',
            field=models.CharField(default=None, max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='authappshopuser',
            name='facebook_user_id',
            field=models.CharField(default=None, max_length=255, null=True),
        ),
    ]