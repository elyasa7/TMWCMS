# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-06-28 22:13
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mega_admin', '0014_auto_20180617_1526'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='menuitem',
            options={'ordering': ['menu_item_order'], 'verbose_name': 'Menu Item', 'verbose_name_plural': 'Menu Items'},
        ),
        migrations.AddField(
            model_name='menuitem',
            name='menu_item_order',
            field=models.IntegerField(default=0),
        ),
    ]
