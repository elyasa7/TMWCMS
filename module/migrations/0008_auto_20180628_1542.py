# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-06-28 15:42
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion
import module.models


class Migration(migrations.Migration):

    dependencies = [
        ('module', '0007_auto_20180624_1538'),
    ]

    operations = [
        migrations.CreateModel(
            name='ModuleImageSlider',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('module_image_slider_speed', models.IntegerField(default=2000, max_length=5)),
                ('module_image_slider_arrow', models.BooleanField(default=1)),
                ('module_image_slider_bullet', models.BooleanField(default=0)),
                ('module_image_slider_thumb', models.BooleanField(default=0)),
                ('module_image_slider_thumb_width', models.IntegerField(default=80)),
                ('module_image_slider_thumb_geight', models.IntegerField(default=45)),
                ('module_image_slider_layout', models.CharField(blank=True, max_length=100, null=True)),
                ('module_image_slider_module', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='module_image_slider_module_key', to='module.Module')),
            ],
            options={
                'db_table': 'module_image_slider',
                'verbose_name_plural': 'Module image sliders',
                'verbose_name': 'Module image slider',
            },
        ),
        migrations.CreateModel(
            name='ModuleImageSliderContent',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('module_image_slider_content_text', models.TextField(blank=True, null=True)),
                ('module_image_slider_content_image', models.ImageField(blank=True, null=True, upload_to=module.models.ModuleImageSliderContent.slider_image_path)),
                ('module_image_slider_content_slider', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='module_image_slider_content_slider_key', to='module.ModuleImageSlider')),
            ],
            options={
                'db_table': 'module_image_slider_content',
                'verbose_name_plural': 'Module image slider contents',
                'verbose_name': 'Module image slider content',
            },
        ),
        migrations.AddField(
            model_name='modulearticleslider',
            name='module_article_slider_arrow',
            field=models.BooleanField(default=1),
        ),
        migrations.AddField(
            model_name='modulearticleslider',
            name='module_article_slider_bullet',
            field=models.BooleanField(default=1),
        ),
        migrations.AddField(
            model_name='modulearticleslider',
            name='module_article_slider_speed',
            field=models.IntegerField(default=2000),
        ),
    ]
