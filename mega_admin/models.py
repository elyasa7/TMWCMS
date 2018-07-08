# -*- coding:utf-8 -*-

from __future__ import unicode_literals
from django.db import models
from django.apps import apps

# Create your models here.

class Language(models.Model):
	class Meta():
		db_table = "language"
		verbose_name = "Language"
		verbose_name_plural = "Languages"

	lang_code = models.CharField(
		verbose_name="Language code",
		max_length=7
	)
	lang_title = models.CharField(
		verbose_name="Language title",
		max_length=200
	)
	lang_title_native = models.CharField(
		verbose_name="Language title native",
		max_length=200
	)
	lang_sef = models.CharField(
		verbose_name="language SEF prefix",
		max_length=2000
	)
	lang_description = models.CharField(
		verbose_name="language description",
		max_length=2000
	)
	lang_published = models.BooleanField(
		default="1",
		verbose_name="language published",
	)
	lang_default = models.BooleanField(
		default="0",
		verbose_name="language is default",
	)

	def __unicode__(self):
		return u'%s' % self.lang_title.encode('utf8')


class LanguageConfiguration(models.Model):
	class Meta():
		db_table = "language_config"
		verbose_name = "Language Configuration"
		verbose_name_plural = "Language Configurations"

	lang_config_multi = models.BooleanField(
		default="0",
		verbose_name="Site is multilingual",
		blank=None,
	)
	lang_config_alias = models.CharField(
		verbose_name="Language configuration alias",
		max_length=100,
		blank=True,
	)

	def __unicode__(self):
		return u'%s' % self.lang_config_multi


class MenuCategory(models.Model):
	class Meta():
		db_table = "menu_category"
		verbose_name = "Menu category"
		verbose_name_plural = "Menu categories"

	menu_category_title = models.CharField(
		verbose_name="Menu category name",
		max_length=200
	)
	menu_category_alias = models.CharField(
		verbose_name="Menu category alias",
		max_length=200
	)
	menu_category_description = models.CharField(
		verbose_name="Menu category description",
		max_length=2000
	)

	def __unicode__(self):
		return u'%s' % self.menu_category_title


class MenuType(models.Model):
	class Meta():
		db_table = "menu_type"
		verbose_name = "Menu type"
		verbose_name_plural = "Menu types"

	menu_type_title = models.CharField(
		verbose_name="Menu type name",
		max_length=200
	)
	menu_type_alias = models.CharField(
		verbose_name="Menu type alias",
		max_length=200
	)
	menu_type_description = models.CharField(
		verbose_name="Menu type description",
		max_length=2000
	)
	menu_type_category = models.ForeignKey(
		MenuCategory,
		related_name="menu_type_category_key",
		verbose_name="Menu type category"
	)

	def __unicode__(self):
		return u'%s' % self.menu_type_title


class MenuMenu(models.Model):
	class Meta():
		db_table = "menu_menu"
		verbose_name = "Menu"
		verbose_name_plural = "Menus"

	menu_menu_title = models.CharField(
		verbose_name="Menu name",
		max_length=200
	)
	menu_menu_alias = models.CharField(
		verbose_name="Menu alias",
		max_length=200
	)
	menu_menu_description = models.CharField(
		verbose_name="Menu description",
		max_length=2000
	)

	def __unicode__(self):
		return u'%s' % self.menu_menu_title


class MenuItem(models.Model):
	class Meta():
		db_table = "menu_item"
		verbose_name = "Menu Item"
		verbose_name_plural = "Menu Items"
		ordering = ['menu_item_order']

	menu_item_title = models.CharField(
		verbose_name="Menu Item Custom URL title",
		max_length=200,
		blank=False,
		null=False,
	)
	menu_item_subtitle = models.CharField(
		verbose_name="Menu item subtitle",
		max_length=200,
		blank=True,
		null=True,
	)
	menu_item_type = models.ForeignKey(
		MenuType,
		related_name="menu_item_type_key",
		blank=False,
		null=False,
	)
	menu_item_language = models.ForeignKey(
		'mega_admin.Language',
		default=1,
		blank=False,
		null=False,
	)
	menu_item_menu = models.ForeignKey(
		MenuMenu,
		blank=False,
		null=False,
	)
	menu_item_parent_item = models.ForeignKey(
		'self',
		related_name="menu_item_key",
		blank=True,
		null=True,
	)
	menu_item_position = models.IntegerField(
		default=0,
		blank=False,
		null=False,
	)
	menu_item_order = models.IntegerField(
		default=0,
		blank=False,
		null=False,
	)
	menu_item_published = models.BooleanField(
		default=1,
		blank=False,
		null=False,
	)

	def __unicode__(self):
		return u'%s' % self.menu_item_title

class MenuItemCustomUrl(models.Model):
	class Meta():
		db_table = "menu_item_custom_url"
		verbose_name = "Menu Item Custom URL"
		verbose_name_plural = "Menu Items Custom URL"

	menu_item_custom_url = models.CharField(
		verbose_name="URL address that points menu item",
		max_length=200,
		blank=False,
		null=False,
	)
	menu_item_custom_url_menu_item = models.OneToOneField(
		MenuItem,
		unique=True,
		on_delete=models.CASCADE,
		related_name="menu_item_custom_url_menu_item_key",
		blank=False,
		null=False
	)

	def __unicode__(self):
		return u'%s' % self.menu_item_custom_url


class MenuItemSingleArticle(models.Model):
	class Meta():
		db_table = "menu_item_single_article"
		verbose_name = "Menu Item Single Article"
		verbose_name_plural = "Menu Item Single Articles"

	menu_item_single_article_article = models.ForeignKey(
		'extension.Article',
		related_name="menu_item_single_article_article_key",
		max_length=200,
		blank=False,
		null=False,
	)
	menu_item_single_article_menu_item = models.OneToOneField(
		MenuItem,
		unique=True,
		on_delete=models.CASCADE,
		related_name="menu_item_single_article_menu_item_key",
		blank=False,
		null=False
	)

	def __unicode__(self):
		return u'%s' % self.menu_item_single_article_article.article_title


class MenuItemCategoryBlog(models.Model):
	class Meta():
		db_table = "menu_item_category_blog"
		verbose_name = "Menu Item Category Blog"
		verbose_name_plural = "Menu Item Categories Blog"

	menu_item_category_blog_category = models.ForeignKey(
		'extension.ArticleCategory',
		related_name="menu_item_category_blog_category_key",
		max_length=200,
		blank=False,
		null=False,
	)
	menu_item_category_blog_menu_item = models.OneToOneField(
		MenuItem,
		unique=True,
		on_delete=models.CASCADE,
		related_name="menu_item_category_blog_menu_item_key",
		blank=False,
		null=False
	)

	def __unicode__(self):
		return u'%s' % self.menu_item_category_blog_category.article_category_title


class MenuItemCategoryList(models.Model):
	class Meta():
		db_table = "menu_item_category_list"
		verbose_name = "Menu Item Category List"
		verbose_name_plural = "Menu Item Categories List"

	menu_item_category_list_category = models.ForeignKey(
		'extension.ArticleCategory',
		related_name="menu_item_category_list_category_key",
		max_length=200,
		blank=False,
		null=False,
	)
	menu_item_category_list_menu_item = models.OneToOneField(
		MenuItem,
		unique=True,
		on_delete=models.CASCADE,
		related_name="menu_item_category_list_menu_item",
		blank=False,
		null=False
	)

	def __unicode__(self):
		return u'%s' % self.menu_item_category_list_category.article_category_title

# COMPONENTS CONFIGURATION --start-- #

# COMPONENTS CONFIGURATION --end-- #

# COMPONENTS EXTENSIONS --start-- #

# COMPONENTS EXTENSIONS --end-- #
