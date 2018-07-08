# -*- coding: utf-8 -*-

from __future__ import unicode_literals
from django import forms
from extension.models import ArticleCategory, Article


class ArticleCategoryForm(forms.ModelForm):
	class Meta:
		model = ArticleCategory
		exclude = (
			'article_category_title',
			'article_category_alias',
			'article_category_parent',
			'article_category_level',
			'article_category_language',
			'article_category_published',
			'article_category_metadesc',
			'article_category_metakey',
			'article_category_user',
			'article_category_date',
			'article_category_description',
			'article_category_note'
		)

class ArticleForm(forms.ModelForm):
	class Meta:
		model = Article
		exclude = (
			'article_title',
			'article_alias',
			'article_category',
			'article_intro',
			'article_content',
			'article_language',
			'article_published',
			'article_metadesc',
			'article_metakey',
			'article_user',
			'article_created_date',
			'article_edited_date',
			'article_note'
		)













