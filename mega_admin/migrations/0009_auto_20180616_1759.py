# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-06-16 17:59
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('mega_admin', '0008_menuitem_menuitemcategoryblog_menuitemcategorylist_menuitemcustomurl_menuitemsinglearticle'),
    ]

    operations = [
        migrations.AlterField(
            model_name='menuitemcustomurl',
            name='menu_item_custom_url_menu_item',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='menu_item_custom_url_menu_item_key', to='mega_admin.MenuItem'),
        ),
    ]
