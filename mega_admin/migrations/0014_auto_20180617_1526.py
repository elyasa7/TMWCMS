# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-06-17 15:26
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('mega_admin', '0013_auto_20180617_1525'),
    ]

    operations = [
        migrations.AlterField(
            model_name='menuitemcategoryblog',
            name='menu_item_category_blog_menu_item',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='menu_item_category_blog_menu_item_key', to='mega_admin.MenuItem'),
        ),
        migrations.AlterField(
            model_name='menuitemcategorylist',
            name='menu_item_category_list_menu_item',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='menu_item_category_list_menu_item', to='mega_admin.MenuItem'),
        ),
        migrations.AlterField(
            model_name='menuitemsinglearticle',
            name='menu_item_single_article_menu_item',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='menu_item_single_article_menu_item_key', to='mega_admin.MenuItem'),
        ),
    ]
