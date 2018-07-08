# -*- coding: utf-8 -*-

from __future__ import unicode_literals
from django import forms
from module.models import *


class ModuleForm(forms.ModelForm):
	class Meta:
		model = Module
		exclude = (
			'module_title',
			'module_subtitle',
			'module_type',
			'module_language',
			'module_menu_item',
			'module_show_option',
			'module_position',
			'module_published',
		)


class ModuleCustomHtmlForm(forms.ModelForm):
	class Meta:
		model = ModuleCustomHtml
		exclude = (
			'module_custom_html_module',
			'module_custom_html_content',
			'module_custom_html_layout',
		)


class ModuleArticleAccordionForm(forms.ModelForm):
	class Meta:
		model = ModuleArticleAccordion
		exclude = (
			'module_article_accordion_module',
			'module_article_accordion_category',
			'module_article_accordion_count',
			'module_article_accordion_feature',
			'module_article_accordion_image',
			'module_article_accordion_date',
			'module_article_accordion_parent',
			'module_article_accordion_button',
			'module_article_accordion_layout',
		)


class ModuleArticleSliderForm(forms.ModelForm):
	class Meta:
		model = ModuleArticleSlider
		exclude = (
			'module_article_slider_module',
			'module_article_slider_category',
			'module_article_slider_count',
			'module_article_slider_feature',
			'module_article_slider_image',
			'module_article_slider_date',
			'module_article_slider_parent',
			'module_article_slider_button',
			'module_article_slider_layout',
		)


class ModuleImageSliderForm(forms.ModelForm):
	class Meta:
		model = ModuleImageSlider
		exclude = (
			'module_image_slider_module',
			'module_image_slider_speed',
			'module_image_slider_arrow',
			'module_image_slider_bullet',
			'module_image_slider_thumb',
			'module_article_slider_date',
			'module_image_slider_thumb_width',
			'module_image_slider_thumb_height',
			'module_image_slider_layout',
		)


class ModuleImageSliderContentForm(forms.ModelForm):
	class Meta:
		model = ModuleImageSliderContent
		exclude = (
			'module_image_slider_content_slider',
			'module_image_slider_content_text',
			'module_image_slider_content_image',
		)


class ModuleArticleListForm(forms.ModelForm):
	class Meta:
		model = ModuleArticleList
		exclude = (
			'module_article_list_module',
			'module_article_list_category',
			'module_article_list_main_count',
			'module_article_list_main_image',
			'module_article_list_main_image_thumb',
			'module_article_list_main_intro',
			'module_article_list_main_intro_slice',
			'module_article_list_main_button',
			'module_article_list_main_button_text',
			'module_article_list_main_layout',
			'module_article_list_link_count',
			'module_article_list_link_image',
			'module_article_list_link_image_thumb',
			'module_article_list_link_intro',
			'module_article_list_link_intro_slice',
			'module_article_list_link_button',
			'module_article_list_link_button_text',
			'module_article_list_link_layout',
		)


class ModuleMenuForm(forms.ModelForm):
	class Meta():
		model = ModuleMenu
		exclude = (
			'module_menu_module',
			'module_menu_menu',
			'module_menu_layout'

		)