# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-06-28 10:21
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('extension', '0007_article_article_image'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='article',
            options={'ordering': ['-id', '-article_published'], 'verbose_name': 'Article', 'verbose_name_plural': 'Article'},
        ),
    ]
