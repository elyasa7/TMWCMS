# -*- coding:utf-8 -*-

from __future__ import unicode_literals
from django.db import models
from django.apps import apps
from django.utils.text import slugify
from datetime import date

# Create your models here.


class ModuleType(models.Model):
	class Meta():
		db_table = "module_type"
		verbose_name = "Module type"
		verbose_name_plural = "Module types"

	module_type_title = models.CharField(
		verbose_name="Module type name",
		max_length=200
	)
	module_type_alias = models.CharField(
		verbose_name="Module type alias",
		max_length=200
	)
	module_type_description = models.CharField(
		verbose_name="Module type description",
		max_length=2000
	)

	def __unicode__(self):
		return u'%s' % self.module_title

class Module(models.Model):
	class Meta():
		db_table = "module"
		verbose_name = "Module"
		verbose_name_plural = "Modules"
		ordering = ['module_order']

	module_title = models.CharField(
		verbose_name="Module title",
		max_length=200,
		blank=False,
		null=False,
	)
	module_subtitle = models.CharField(
		verbose_name="Module subtitle",
		max_length=200,
		blank=True,
		null=True,
	)
	module_type = models.ForeignKey(
		'module.ModuleType',
		related_name="module_type_key",
		blank=False,
		null=False,
	)
	module_language = models.ForeignKey(
		'mega_admin.Language',
		default=1,
		blank=False,
		null=False,
	)
	module_show_option = models.CharField(
		default="all",
		max_length=10,
		blank=False,
		null=False,
	)
	module_menu_item = models.ManyToManyField(
		'mega_admin.MenuItem',
		blank=True,
	)
	module_position = models.ForeignKey(
		'template.TemplatePosition',
		related_name="module_position_key",
		blank=True,
		null=True,
	)
	module_published = models.BooleanField(
		default=1,
		blank=False,
		null=False,
	)
	module_show_title = models.BooleanField(
		default=1,
		blank=False,
		null=False,
	)
	module_order = models.IntegerField(
		default=0,
		blank=True,
		null=True,
	)
	module_layout = models.CharField(
		max_length=100,
		blank=True,
		null=True,
	)

	# def __unicode__(self):
	# 	return u'%s' % self.module_title

class ModuleCustomHtml(models.Model):
	class Meta():
		db_table = "module_custom_html"
		verbose_name = "Module Custom HTML"
		verbose_name_plural = "Modules custom HTML"

	module_custom_html_module = models.OneToOneField(
		Module,
		unique=True,
		on_delete=models.CASCADE,
		related_name="module_custom_html_module_key",
		blank=False,
		null=False,
	)
	module_custom_html_content = models.TextField (
		blank=True,
		null=True,
	)
	module_custom_html_layout = models.CharField (
		max_length=200,
		blank=True,
		null=True,
	)

class ModuleArticleAccordion(models.Model):
	class Meta():
		db_table = "module_article_accordion"
		verbose_name = "Module article accordion"
		verbose_name_plural = "Module article accordions"

	module_article_accordion_module = models.OneToOneField(
		Module,
		unique=True,
		on_delete=models.CASCADE,
		related_name="module_article_accordion_module_key",
		blank=False,
		null=False,
	)
	module_article_accordion_category = models.ForeignKey (
		'extension.ArticleCategory',
		related_name="module_article_accordion_category_key",
		blank=False,
		null=False,
	)
	module_article_accordion_count = models.IntegerField (
		default=5,
		blank=False,
		null=False,
	)
	module_article_accordion_feature = models.BooleanField (
		default=0,
		blank=False,
		null=False,
	)
	module_article_accordion_image = models.BooleanField (
		default=0,
		blank=False,
		null=False,
	)
	module_article_accordion_thumb = models.BooleanField (
		default=0,
		blank=False,
		null=False,
	)
	module_article_accordion_thumb_width = models.IntegerField (
		default=80,
		blank=False,
		null=False,
	)
	module_article_accordion_thumb_height = models.IntegerField (
		default=45,
		blank=False,
		null=False,
	)
	module_article_accordion_date = models.BooleanField (
		default=0,
		blank=False,
		null=False,
	)
	module_article_accordion_parent = models.BooleanField (
		default=0,
		blank=False,
		null=False,
	)
	module_article_accordion_button = models.CharField (
		max_length=50,
		default="read more",
		blank=True,
		null=True,
	)
	module_article_accordion_layout = models.CharField (
		max_length=100,
		blank=True,
		null=True,
	)



class ModuleArticleSlider(models.Model):
	class Meta():
		db_table = "module_article_slider"
		verbose_name = "Module article slider"
		verbose_name_plural = "Module article sliders"

	module_article_slider_module = models.OneToOneField(
		Module,
		unique=True,
		on_delete=models.CASCADE,
		related_name="module_article_slider_module_key",
		blank=False,
		null=False,
	)
	module_article_slider_category = models.ForeignKey (
		'extension.ArticleCategory',
		related_name="module_article_slider_category_key",
		blank=False,
		null=False,
	)
	module_article_slider_count = models.IntegerField (
		default=5,
		blank=False,
		null=False,
	)
	module_article_slider_speed = models.IntegerField (
		default=2000,
		blank=False,
		null=False,
	)
	module_article_slider_feature = models.BooleanField (
		default=0,
		blank=False,
		null=False,
	)
	module_article_slider_image = models.BooleanField (
		default=0,
		blank=False,
		null=False,
	)
	module_article_slider_date = models.BooleanField (
		default=0,
		blank=False,
		null=False,
	)
	module_article_slider_parent = models.BooleanField (
		default=0,
		blank=False,
		null=False,
	)
	module_article_slider_arrow = models.BooleanField (
		default=1,
		blank=False,
		null=False,
	)
	module_article_slider_bullet = models.BooleanField (
		default=1,
		blank=False,
		null=False,
	)
	module_article_slider_button = models.CharField (
		max_length=50,
		default="read more",
		blank=True,
		null=True,
	)
	module_article_slider_layout = models.CharField (
		max_length=100,
		blank=True,
		null=True,
	)



class ModuleImageSlider(models.Model):
	class Meta():
		db_table = "module_image_slider"
		verbose_name = "Module image slider"
		verbose_name_plural = "Module image sliders"

	module_image_slider_module = models.OneToOneField(
		Module,
		unique=True,
		on_delete=models.CASCADE,
		related_name="module_image_slider_module_key",
		blank=False,
		null=False,
	)
	module_image_slider_speed = models.IntegerField (
		default=2000,
		blank=False,
		null=False,
	)
	module_image_slider_arrow = models.BooleanField (
		default=1,
		blank=False,
		null=False,
	)
	module_image_slider_bullet = models.BooleanField (
		default=0,
		blank=False,
		null=False,
	)
	module_image_slider_thumb = models.BooleanField (
		default=0,
		blank=False,
		null=False,
	)
	module_image_slider_thumb_width = models.IntegerField (
		default=80,
		blank=False,
		null=False,
	)
	module_image_slider_thumb_height = models.IntegerField (
		default=45,
		blank=False,
		null=False,
	)
	module_image_slider_layout = models.CharField (
		max_length=100,
		blank=True,
		null=True,
	)


class ModuleImageSliderContent(models.Model):
	class Meta():
		db_table = "module_image_slider_content"
		verbose_name = "Module image slider content"
		verbose_name_plural = "Module image slider contents"
		ordering = ['module_image_slider_content_order']

	module_image_slider_content_slider = models.ForeignKey(
		ModuleImageSlider,
		related_name="module_image_slider_content_slider_key",
		blank=False,
		null=False,
	)
	module_image_slider_content_text = models.TextField (
		blank=True,
		null=True,
	)

	def slider_image_path(self, filename):
		path = ''.join([str('slider/') + str(self.module_image_slider_content_slider.id) + str('/'), slugify(filename) + str('.jpg')])
		return path

	module_image_slider_content_image = models.ImageField (
		upload_to=slider_image_path,
		blank=True,
		null=True,
	)

	module_image_slider_content_order = models.IntegerField (
		default=0,
		blank=True,
		null=True,
	)


class ModuleArticleList(models.Model):
	class Meta():
		db_table = "module_article_list"
		verbose_name = "Module Article list"
		verbose_name_plural = "Module Article lists"

	module_article_list_module = models.OneToOneField(
		Module,
		unique=True,
		on_delete=models.CASCADE,
		related_name="module_article_list_module_key",
		blank=False,
		null=False,
	)
	module_article_list_category = models.ForeignKey (
		'extension.ArticleCategory',
		related_name="module_article_list_category_key",
		blank=False,
		null=False,
	)
	module_article_list_main_count = models.IntegerField (
		default=1,
		blank=False,
		null=False,
	)
	module_article_list_main_image = models.BooleanField (
		default=1,
		blank=False,
		null=False,
	)
	module_article_list_main_image_thumb = models.BooleanField (
		default=0,
		blank=False,
		null=False,
	)
	module_article_list_main_intro = models.BooleanField (
		default=1,
		blank=False,
		null=False,
	)
	module_article_list_main_intro_slice = models.IntegerField (
		default=140,
		blank=False,
	)
	module_article_list_main_button = models.BooleanField (
		default=1,
		blank=False,
		null=False,
	)
	module_article_list_main_button_text = models.CharField (
		max_length=100,
		default="Read more",
		blank=False,
		null=False,
	)
	module_article_list_main_layout = models.CharField (
		max_length=100,
		blank=True,
		null=True,
	)
	module_article_list_link_count = models.IntegerField (
		default=5,
		blank=False,
		null=False,
	)
	module_article_list_link_image = models.BooleanField (
		default=1,
		blank=False,
		null=False,
	)
	module_article_list_link_image_thumb = models.BooleanField (
		default=1,
		blank=False,
		null=False,
	)
	module_article_list_link_intro = models.BooleanField (
		default=1,
		blank=False,
		null=False,
	)
	module_article_list_link_intro_slice = models.IntegerField (
		default=140,
		blank=False,
	)
	module_article_list_link_button = models.BooleanField (
		default=1,
		blank=False,
		null=False,
	)
	module_article_list_link_button_text = models.CharField (
		max_length=100,
		default="Read more",
		blank=False,
		null=False,
	)
	module_article_list_link_layout = models.CharField (
		max_length=100,
		blank=True,
		null=True,
	)

class ModuleMenu(models.Model):
	class Meta():
		db_table = "module_menu"
		verbose_name = "Module Menu"
		verbose_name_plural = "Module Menus"


	module_menu_module = models.OneToOneField(
		Module,
		unique=True,
		on_delete=models.CASCADE,
		related_name="module_menu_module",
		blank=False,
		null=False,
	)
	module_menu_menu = models.ForeignKey (
		'mega_admin.MenuMenu',
		related_name="module_menu_menu_key",
		blank=False,
		null=False,
	)
	module_menu_layout = models.CharField (
		max_length=100,
		blank=True,
		null=True,
	)