# -*- coding: utf-8 -*-

from __future__ import unicode_literals
from django.db import models
from datetime import date
from pytils import translit
from django.contrib.auth.models import User


# Create your models here.
# encoding=unicode
# !/usr/bin/python
# -*- coding: unicode -*-

LANGUAGE_CHOICES = (
	('ru', 'русский'),
	('en', 'английский'),
	('tm', 'туркменский'),
	)

def get_image_path(instance, filename):
        path = ''.join([date.today().strftime('../static/article/%Y/%m/%d/'), translit.slugify(filename), ".jpg"])
        return path

class ArticleCategory(models.Model):
    class Meta():
        db_table = "article_category"
        verbose_name = "Категорию"
        verbose_name_plural = "Категории"

    name = models.CharField('Name', max_length=100)
    article_category_language = models.CharField(verbose_name="Язык", max_length=9, choices=LANGUAGE_CHOICES,
                                                 default='ru', blank=False)

    def __unicode__(self):
        return u'%s' % self.name


class Article(models.Model):
    class Meta():
        db_table = "article"
        verbose_name = "Статью"
        verbose_name_plural = "Статьи"

    article_title = models.CharField(verbose_name="Заголовок", max_length=200)
    article_intro = models.TextField(verbose_name="Всткпительный текст")
    article_text = models.TextField(verbose_name="Основной текст")
    article_language = models.CharField(verbose_name="Язык", max_length=9, choices=LANGUAGE_CHOICES, default='ru',
                                        blank=False)
    article_category = models.ForeignKey(ArticleCategory, verbose_name="Категория", blank=False)
    article_date = models.DateField(verbose_name="Дата публикации", default=date.today, blank=False)
    article_views = models.IntegerField(default=0)
    article_image_intro = models.ImageField(upload_to=get_image_path, null=True, blank=True,
                                           verbose_name="Вступительная картинка")
    article_image_full = models.ImageField(upload_to=get_image_path, null=True, blank=True,
                                          verbose_name="Изображение для полной статьи")
    article_author = models.ForeignKey(User)

    def __unicode__(self):
        return u'%s' % self.article_title

class ArticleImage(models.Model):
    class Meta():
        db_table = "article_image"
        verbose_name = "Изображение к статье"
        verbose_name_plural = "Изображения к статье"

    article_image = models.ImageField(upload_to=get_image_path, null=True, blank=True,verbose_name="Изображение")
    article_image_text = models.CharField(max_length=600, null=True, blank=True, verbose_name="Подпись к изображению")
    article_image_date = models.DateField(verbose_name="Дата публикации", default=date.today, blank=False)
    article_image_article = models.ForeignKey(Article)


class ArticleComment(models.Model):
    class Meta():
        db_table = "article_comment"
        verbose_name = "Коментарий к статье"
        verbose_name_plural = "Коментарии к статье"

    article_comment_text = models.TextField(verbose_name="Текст коментария")
    article_comment_date = models.DateField(verbose_name="Дата публикации", default=date.today, blank=False)
    article_comment_author = models.ForeignKey(User)
    article_comment_article = models.ForeignKey(Article)

    def __unicode__(self):
        return u'%s' % self.article_comment_article
