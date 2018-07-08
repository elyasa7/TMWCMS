# -*- coding: utf-8 -*-

from __future__ import unicode_literals
from django import forms
from mega_admin.models import *


class MenuCategoryForm(forms.ModelForm):
	class Meta:
		model = MenuCategory
		exclude = (
			'menu_category_title',
			'menu_category_alias',
			'menu_category_description',
		)


class MenuTypeForm(forms.ModelForm):
	class Meta:
		model = MenuType
		exclude = (
			'menu_type_title',
			'menu_type_alias',
			'menu_type_description',
			'menu_type_category',
		)


class MenuMenuForm(forms.ModelForm):
	class Meta:
		model = MenuMenu
		exclude = (
			'menu_menu_title',
			'menu_menu_alias',
			'menu_menu_description',
		)


class LanguageForm(forms.ModelForm):
	class Meta:
		model = Language
		exclude = (
			'lang_code',
			'lang_title',
			'lang_title_native',
			'lang_sef',
			'lang_description',
			'lang_published',
		)


class MenuItemForm(forms.ModelForm):
	class Meta:
		model = MenuItem
		exclude = (
			'menu_item_title',
			'menu_item_subtitle',
			'menu_item_type',
			'menu_item_language',
			'menu_item_menu',
			'menu_item_parent_item',
			'menu_item_position',
			'menu_item_published',
		)


class MenuItemCustomUrlForm(forms.ModelForm):
	class Meta:
		model = MenuItemCustomUrl
		exclude = (
			'menu_item_custom_url',
			'menu_item_custom_url_menu_item',
		)


class MenuItemSingleArticleForm(forms.ModelForm):
	class Meta:
		model = MenuItemSingleArticle
		exclude = (
			'menu_item_single_article_article',
			'menu_item_single_article_menu_item',
		)


class MenuItemCategoryBlogForm(forms.ModelForm):
	class Meta:
		model = MenuItemCategoryBlog
		exclude = (
			'menu_item_category_blog_category',
			'menu_item_category_blog_menu_item',
		)


class MenuItemCategoryListForm(forms.ModelForm):
	class Meta:
		model = MenuItemCategoryList
		exclude = (
			'menu_item_category_list_category',
			'menu_item_category_list_menu_item',
		)