# -*- coding: utf-8 -*-
# Generated by Django 1.9.3 on 2018-03-29 03:41
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mega_admin', '0002_menumenu'),
    ]

    operations = [
        migrations.CreateModel(
            name='Language',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('lang_code', models.CharField(max_length=7, verbose_name='Language code')),
                ('lang_title', models.CharField(max_length=200, verbose_name='Language title')),
                ('lang_title_native', models.CharField(max_length=200, verbose_name='Language title native')),
                ('lang_sef', models.CharField(max_length=2000, verbose_name='language SEF prefix')),
                ('lang_description', models.CharField(max_length=2000, verbose_name='language description')),
                ('lang_published', models.BooleanField(default='1', verbose_name='language published')),
            ],
            options={
                'db_table': 'language',
                'verbose_name': 'Language',
                'verbose_name_plural': 'Languages',
            },
        ),
    ]