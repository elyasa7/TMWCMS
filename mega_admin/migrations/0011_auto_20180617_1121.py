# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-06-17 11:21
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('mega_admin', '0010_auto_20180616_2106'),
    ]

    operations = [
        migrations.AlterField(
            model_name='menuitem',
            name='menu_item_parent_item',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='menu_item_key', to='mega_admin.MenuItem'),
        ),
    ]