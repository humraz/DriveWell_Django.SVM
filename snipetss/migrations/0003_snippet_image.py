# -*- coding: utf-8 -*-
# Generated by Django 1.11.10 on 2018-02-14 12:34
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('snipetss', '0002_auto_20180214_0849'),
    ]

    operations = [
        migrations.AddField(
            model_name='snippet',
            name='image',
            field=models.ImageField(max_length=255, null=True, upload_to='myphoto/%Y/%m/%d/'),
        ),
    ]
