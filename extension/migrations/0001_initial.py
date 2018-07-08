# -*- coding: utf-8 -*-
# Generated by Django 1.9.3 on 2018-03-30 11:00
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ArticleCategory',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('article_category_title', models.CharField(max_length=200, verbose_name='Menu category name')),
                ('article_category_alias', models.CharField(max_length=200, verbose_name='Menu category alias')),
                ('article_category_description', models.CharField(max_length=2000, verbose_name='Menu category description')),
            ],
            options={
                'db_table': 'article_category',
                'verbose_name': 'Article category',
                'verbose_name_plural': 'Article categories',
            },
        ),
    ]