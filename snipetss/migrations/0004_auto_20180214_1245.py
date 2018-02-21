# -*- coding: utf-8 -*-
# Generated by Django 1.11.10 on 2018-02-14 12:45
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('snipetss', '0003_snippet_image'),
    ]

    operations = [
        migrations.CreateModel(
            name='MyPhoto',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('image', models.ImageField(max_length=255, null=True, upload_to='myphoto/%Y/%m/%d/')),
            ],
        ),
        migrations.RemoveField(
            model_name='snippet',
            name='image',
        ),
    ]
