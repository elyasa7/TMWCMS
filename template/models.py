# -*- coding:utf-8 -*-

from __future__ import unicode_literals

from django.db import models

from mega_admin.models import MenuMenu

# Create your models here.

class Template(models.Model):
	class Meta():
		db_table = "template"
		verbose_name = "Template"
		verbose_name_plural = "Templates"

	template_title = models.CharField(
		verbose_name="Template title",
		max_length=200
	)
	template_alias = models.CharField(
		verbose_name="Template alias",
		max_length=200
	)
	template_description = models.TextField(
		verbose_name="Template description",
		blank=True,
	)
	template_version = models.IntegerField(
		verbose_name="Template version",
		null=True,
		blank=True,
	)
	template_default = models.BooleanField(
		default=0,
		blank=False,
		null=False
	)
	template_main_menu = models.ForeignKey(
		MenuMenu,
		blank=True,
		null=True,
	)

	def __unicode__(self):
		return u'%s' % self.template_title + str(" v") + str(self.template_version)

class TemplatePosition(models.Model):
	class Meta():
		db_table = "template_position"
		verbose_name = "Template position"
		verbose_name_plural = "Template positions"

	template_position_template = models.ForeignKey(
		Template,
		related_name="template_position_template_key",
		verbose_name="Template positions template",
		blank=False,
		null=False,
	)
	template_position_name = models.CharField(
		verbose_name="Template position name",
		max_length=200,
		blank=False,
		null=False,
	)
	template_position_alias = models.CharField(
		verbose_name="Template position alias",
		max_length=200,
		blank=False,
		null=False,
	)

	def __unicode__(self):
		return u'%s' % self.template_position_name