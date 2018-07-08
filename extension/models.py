# -*- coding:utf-8 -*-

from __future__ import unicode_literals
from django.db import models
from django.apps import apps

from django.contrib.auth.models import User
from django.utils.text import slugify
from datetime import date

# Create your models here.

##--## CONTENT EXTENSION START ##--##

class ArticleCategory(models.Model):
	class Meta():
		db_table = "article_category"
		verbose_name = "Article category"
		verbose_name_plural = "Article categories"

	article_category_title = models.CharField(
		verbose_name="Menu category name",
		max_length=200
	)
	article_category_alias = models.CharField(
		verbose_name="Menu category alias",
		max_length=200
	)
	article_category_description = models.TextField(
		verbose_name="Menu category description",
		blank=True,
	)
	article_category_parent = models.ForeignKey(
		"ArticleCategory",
		related_name="article_category_parent_key",
		verbose_name="Menu category name",
		null=True,
		blank=True,
	)
	article_category_level = models.IntegerField(
		default=1,
		blank=False,
	)
	article_category_language = models.ForeignKey(
		'mega_admin.Language',
		default=1,
		blank=False,
	)
	article_category_published = models.BooleanField(
		"ArticleCategory",
		default=1,
		blank=False,
	)
	article_category_metadesc = models.CharField(
		verbose_name="Article category Meta Description",
		max_length=2000,
		null=True,
	)
	article_category_metakey = models.CharField(
		verbose_name="Article category Meta Keys",
		max_length=2000
	)
	article_category_user = models.ForeignKey(
		User,
		verbose_name="Article category created by",
		blank=False,
	)
	article_category_date = models.DateTimeField(
		auto_now_add=True,
		blank=False,
	)
	article_category_note = models.CharField(
		verbose_name="Menu category note",
		max_length=2000
	)

	def __unicode__(self):
		return u'%s' % self.article_category_title


class Article(models.Model):
	class Meta():
		db_table = "article"
		verbose_name = "Article"
		verbose_name_plural = "Article"
		ordering = ['-article_published', 'id']

	def get_image_path(self, filename):
		path = ''.join([date.today().strftime('content/article//%Y/%m/'), slugify(filename) + str('.jpg')])
		return path

	article_title = models.CharField(
		verbose_name="Article title",
		max_length=250
	)
	article_alias = models.CharField(
		verbose_name="Article alias",
		max_length=250
	)
	article_category = models.ForeignKey(
		"ArticleCategory",
		related_name="article_category_key",
		verbose_name="Category to which belongs article",
		null=False,
		blank=False,
		default='3',
	)
	article_intro = models.TextField(
		verbose_name="Article intro (before read more)",
		blank=True,
		null=True,
	)
	article_content = models.TextField(
		verbose_name="Article content",
		blank=True,
		null=True,
	)
	article_language = models.ForeignKey(
		'mega_admin.Language',
		default=1,
		blank=False,
		null=False,
	)
	article_published = models.BooleanField(
		"ArticleCategory",
		default=1,
		blank=True,
		null=False,
	)
	article_metadesc = models.CharField(
		verbose_name="Article category Meta Description",
		max_length=2000,
		null=True,
		blank=True,
	)
	article_metakey = models.CharField(
		verbose_name="Article Meta Keys",
		max_length=2000,
		blank=True,
		null=True,
	)
	article_user = models.ForeignKey(
		User,
		verbose_name="Article created by",
		blank=False,
		null=False,
	)
	article_created_date = models.DateTimeField(
		verbose_name="Article created date",
		auto_now_add=True,
		blank=False,
	)
	article_edited_date = models.DateTimeField(
		verbose_name="Article modified date",
		auto_now_add=True,
		blank=False,
	)
	article_note = models.CharField(
		verbose_name="Article notes",
		max_length=2000,
		blank=True,
		null=True,
	)
	article_image = models.ImageField(
		upload_to=get_image_path,
		null=True,
		blank=True,
		verbose_name="Article main image")

	def __unicode__(self):
		return u'%s' % self.article_title + str(" (") + self.article_category.article_category_title + str(")")

	##--## CONTENT EXTENSION END ##--##
