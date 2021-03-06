# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-06-24 15:38
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('extension', '0007_article_article_image'),
        ('module', '0006_auto_20180623_2208'),
    ]

    operations = [
        migrations.CreateModel(
            name='ModuleArticleSlider',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('module_article_slider_count', models.IntegerField(default=5)),
                ('module_article_slider_feature', models.BooleanField(default=0)),
                ('module_article_slider_image', models.BooleanField(default=0)),
                ('module_article_slider_date', models.BooleanField(default=0)),
                ('module_article_slider_parent', models.BooleanField(default=0)),
                ('module_article_slider_button', models.CharField(blank=True, default='read more', max_length=50, null=True)),
                ('module_article_slider_layout', models.CharField(blank=True, max_length=100, null=True)),
                ('module_article_slider_category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='module_article_slider_category_key', to='extension.ArticleCategory')),
                ('module_article_slider_module', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='module_article_slider_module_key', to='module.Module')),
            ],
            options={
                'verbose_name': 'Module article slider',
                'verbose_name_plural': 'Module article sliders',
                'db_table': 'module_article_slider',
            },
        ),
        migrations.AddField(
            model_name='modulearticleaccordion',
            name='module_article_accordion_layout',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]
