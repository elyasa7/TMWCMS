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

TYPE_CHOICES = (
	('article', 'Single article'),
	('article_list', 'Article list'),
	('article_blog', 'Article blog'),
	('meta_link', 'User defined link'),
	)


class Menu(models.Model):
    class Meta():
        db_table = "menu"
        verbose_name = "menu_item"
        verbose_name_plural = "menu items"

    menu_title = models.CharField(verbose_name="Menu item title", max_length=200)
    menu_description = models.CharField(verbose_name="Menu description", max_length=200)
    menu_type = models.CharField(verbose_name="Select menu type", choices=TYPE_CHOICES, max_length=200)
    menu_subitem = models.CharField(verbose_name="Select upperitems ID", blank=True, max_length=200)
    menu_link = models.CharField(verbose_name="Menu link", max_length=190, blank=True)
    menu_position = models.CharField(verbose_name="Specify item position", blank=True, max_length=200)
    menu_language = models.CharField(verbose_name="Язык", max_length=9, choices=LANGUAGE_CHOICES, blank=True)

    def __unicode__(self):
        return u'%s' % self.menu_title