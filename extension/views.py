# -*- coding:utf-8 -*-

from django.shortcuts import render, render_to_response, redirect
from django.http.response import HttpResponse, HttpResponseRedirect
import datetime

from django.core.exceptions import ObjectDoesNotExist
from django.views.decorators.csrf import csrf_protect, csrf_exempt
from django.template.context_processors import csrf

from django.contrib.auth.models import User

from django.core.paginator import Paginator
from itertools import chain

from extension.forms import ArticleCategoryForm, ArticleForm
from extension.models import ArticleCategory, Article
from mega_admin.models import Language, MenuMenu, MenuItem
from template.models import Template
from module.models import *
from pytils.translit import slugify

from django.contrib.auth.decorators import login_required

# Create your views here.


args = {}
args['languages'] = Language.objects.all().order_by('id')


@csrf_protect
@login_required
def category_manager(request, page_number=1):
	all_categories = ArticleCategory.objects.all().order_by('id')
	categories_page = Paginator(all_categories, 20)
	args['categories'] = categories_page.page(page_number)
	args['caption'] = str("Category manager")
	args['user'] = request.user.id
	response = render_to_response('content_category_manager.html', args)
	# response.set_cookie('logged_in_status', 'never_use_this_ever')
	return response


@csrf_protect
def add_category(request):
	args['categories'] = ArticleCategory.objects.filter(
		article_category_published=1
	).order_by('id')
	args['caption'] = str("Add or edit category")
	try:
		args['current_category'] = ArticleCategory.objects.get(id=request.GET.get('id'))
	except:
		args['current_category'] = None
	#	args['caption'] = str("Edit category")
	return render(request, 'content_add_new_category.html', args)


@csrf_exempt
def save_category(request):
	if request.POST:
		article_category_title = request.POST.get('article_category_title')
		article_category_alias = request.POST.get('article_category_alias')
		article_category_parent = request.POST.get('article_category_parent', '')
		article_category_level = request.POST.get('article_category_level', '1')
		article_category_language = request.POST.get('article_category_language')
		article_category_published = request.POST.get('article_category_published', '0')
		if article_category_published == "on":
			article_category_published = "1"
		else:
			article_category_published = "0"
		article_category_metadesc = request.POST.get('article_category_metadesc')
		article_category_metakey = request.POST.get('article_category_metakey')
		article_category_user = request.user.id
		article_category_date = datetime.datetime.now()
		article_category_description = request.POST.get('article_category_description')
		article_category_note = request.POST.get('article_category_note', '')
		save_category_form = ArticleCategoryForm(request.POST)
		try:
			article_category = ArticleCategory.objects.get(id=request.POST.get('article_category_id'))
		except:
			article_category = None
		if article_category is None:
			if save_category_form.is_valid():
				article_category = save_category_form.save(commit=False)
				article_category.article_category_title = article_category_title
				article_category.article_category_alias = article_category_alias
				article_category.article_category_parent_id = article_category_parent
				article_category.article_category_level = article_category_level
				article_category.article_category_language_id = article_category_language
				article_category.article_category_published = article_category_published
				article_category.article_category_metadesc = article_category_metadesc
				article_category.article_category_metakey = article_category_metakey
				article_category.article_category_user_id = article_category_user
				article_category.article_category_date = article_category_date
				article_category.article_category_description = article_category_description
				article_category.article_category_note = article_category_note
				save_category_form.save()
				message = str("?message_type=success&message=")
				args['msg_txt'] = msg_txt = str("Category '") + str(article_category_title) + str("' saved")
				return HttpResponseRedirect('/mega-admin/content/category-manager/' + message + msg_txt)
			else:
				message = str("?message_type=error&message=")
				args['msg_txt'] = msg_txt = str("Error while saving. Form is not valid")
				return HttpResponseRedirect('/mega-admin/content/category-manager/' + message + msg_txt)
		else:
			article_category = ArticleCategory.objects.get(id=request.POST.get('article_category_id'))
			article_category.article_category_title = article_category_title
			article_category.article_category_alias = article_category_alias
			article_category.article_category_parent_id = article_category_parent
			article_category.article_category_level = article_category_level
			article_category.article_category_language_id = article_category_language
			article_category.article_category_published = article_category_published
			article_category.article_category_metadesc = article_category_metadesc
			article_category.article_category_metakey = article_category_metakey
			article_category.article_category_description = article_category_description
			article_category.article_category_note = article_category_note
			article_category.save()
			message = str("?message_type=success&message=")
			args['success'] = success = str("Category '") + str(article_category_title) + str("' saved")
			return HttpResponseRedirect('/mega-admin/content/category-manager/' + message + success)
	else:
		message = str("?message_type=success&message=")
		args['msg_txt'] = msg_txt = str("Erro. Save method need to be POST")
		return HttpResponseRedirect('/mega-admin/content/category-manager/' + message + msg_txt)


def change_article_category_state(request):
	if request.POST:
		try:
			article_category_id = (request.POST.get('article_category_id'))
			article_category = ArticleCategory.objects.get(id=article_category_id)
			if article_category.article_category_published == 1:
				article_category.article_category_published = 0
				article_category.save(update_fields=['article_category_published'])
				return HttpResponseRedirect(request.META.get('HTTP_REFERER', '/'), args)
			else:
				article_category.article_category_published = 1
				article_category.save(update_fields=['article_category_published'])
				return HttpResponseRedirect(request.META.get('HTTP_REFERER', '/'), args)
		except ObjectDoesNotExist:
			article_category = None
			return HttpResponseRedirect(request.META.get('HTTP_REFERER', '/'), args)


def article_category_delete(request):
	if request.POST:
		try:
			article_category_id = (request.POST.get('article_category_id'))
			article_category = ArticleCategory.objects.get(id=article_category_id)
			article_category.delete()
			return HttpResponseRedirect('/mega-admin/content/category-manager/')
		except ObjectDoesNotExist:
			article_category = None
			return HttpResponseRedirect('/mega-admin/content/category-manager/')


@csrf_protect
def article_manager(request, page_number=1):
	all_articles = Article.objects.all().order_by('id')
	articles_page = Paginator(all_articles, 20)
	args['articles'] = articles_page.page(page_number)
	args['categories'] = ArticleCategory.objects.filter(
		article_category_published=1
	).order_by(
		'article_category_title'
	)
	args['caption'] = str("Article manager")
	args['user'] = request.user.id
	#	response = render_to_response
	# response.set_cookie('logged_in_status', 'never_use_this_ever')
	return render(request, 'content_article_manager.html', args)


@csrf_protect
def add_article(request):
	args['categories'] = ArticleCategory.objects.all().order_by('article_category_title')
	args['caption'] = str("Add or edit article")
	try:
		args['current_article'] = Article.objects.get(id=request.GET.get('id'))
	except:
		args['current_article'] = None
	#	args['caption'] = str("Edit category")
	return render(request, 'content_add_new_article.html', args)


@csrf_protect
@login_required
def save_article(request):
	if request.POST:
		article_title = request.POST.get('article_title')
		article_alias = request.POST.get('article_alias')
		article_category = request.POST.get('article_category', '')
		article_intro = request.POST.get('article_intro', '')
		article_content = request.POST.get('article_content', '')
		article_language = request.POST.get('article_language')
		article_published = request.POST.get('article_published', '0')
		if article_published == "on":
			article_published = "1"
		else:
			article_published = "0"
		article_metadesc = request.POST.get('article_metadesc')
		article_metakey = request.POST.get('article_metakey')
		article_user = request.user.id
		article_created_date = datetime.datetime.now()
		article_modified_date = datetime.datetime.now()
		article_note = request.POST.get('article_note')
		save_article_form = ArticleForm(request.POST)
		try:
			article = Article.objects.get(id=request.POST.get('article_id'))
		except:
			article = None
		if article is None:
			if save_article_form.is_valid():
				article = save_article_form.save(commit=False)
				article.article_title = article_title
				article.article_alias = article_alias
				article.article_category_id = article_category
				article.article_intro = article_intro
				article.article_content = article_content
				article.article_language_id = article_language
				article.article_published = article_published
				article.article_metakey = article_metakey
				article.article_metadesc = article_metadesc
				article.article_user_id = article_user
				article.article_created_date = article_created_date
				article.article_modified_date = article_modified_date
				article.article_note = article_note
				article.article_image = request.FILES['article_image']
				save_article_form.save()
				message = str("?message_type=success&message=")
				args['msg_txt'] = msg_txt = str("Article saved")
				return HttpResponseRedirect('/mega-admin/content/article-manager/' + message + msg_txt)
			else:
				message = str("?message_type=error&message=")
				args['msg_txt'] = msg_txt = str("Error while saving. Form is not valid")
				return HttpResponseRedirect('/mega-admin/content/article-manager/' + message + msg_txt)
		else:
			article = Article.objects.get(id=request.POST.get('article_id'))
			article.article_title = article_title
			article.article_alias = article_alias
			article.article_category_id = article_category
			article.article_intro = article_intro
			article.article_content = article_content
			article.article_language_id = article_language
			article.article_published = article_published
			article.article_metakey = article_metakey
			article.article_metadesc = article_metadesc
			article.article_user_id = article_user
			article.article_modified_date = article_modified_date
			article.article_note = article_note
			article.article_image = request.FILES['article_image']
			article.save()
			message = str("?message_type=success&message=")
			args['msg_txt'] = msg_txt = str("Article saved")
			return HttpResponseRedirect('/mega-admin/content/article-manager/' + message + msg_txt)
	else:
		message = str("?message_type=success&message=")
		args['msg_txt'] = msg_txt = str("Error. Save method need to be POST")
		return HttpResponseRedirect('/mega-admin/content/article-manager/' + message + msg_txt)


@csrf_protect
def change_article_state(request):
	if request.POST:
		try:
			article_id = (request.POST.get('article_id'))
			article = Article.objects.get(id=article_id)
			if article.article_published == 1:
				article.article_published = 0
				article.save(update_fields=['article_published'])
				return HttpResponseRedirect(request.META.get('HTTP_REFERER', '/'), args)
			else:
				article.article_published = 1
				article.save(update_fields=['article_published'])
				return HttpResponseRedirect(request.META.get('HTTP_REFERER', '/'), args)
		except ObjectDoesNotExist:
			article = None
			return HttpResponseRedirect(request.META.get('HTTP_REFERER', '/'), args)


@csrf_protect
def article_delete(request):
	if request.POST:
		try:
			article_id = (request.POST.get('article_id'))
			article = Article.objects.get(id=article_id)
			article.delete()
			return HttpResponseRedirect('/mega-admin/content/article-manager/')
		except ObjectDoesNotExist:
			article = None
			return HttpResponseRedirect('/mega-admin/content/article-manager/')


@csrf_protect
def single_article(request, article_alias):
	args['article'] = article = Article.objects.get(
		article_alias__exact=article_alias,
		article_published=1
	)
	template = Template.objects.get(template_default__exact=1)
	args['main_menu'] = MenuMenu.objects.get(id__exact=template.template_main_menu_id)
	args['menu_items'] = MenuItem.objects.filter(
		menu_item_menu=args['main_menu'],
		menu_item_published=1,
	)
	template_page = template.template_alias + str("/content/single_article.html")

	args['current_menu_item'] = MenuItem.objects.get(
		menu_item_type__menu_type_alias="single-article",
		menu_item_single_article_menu_item_key__menu_item_single_article_article__article_alias__exact=article_alias,
		menu_item_published=1,
	)
	all_modules = Module.objects.filter(
		module_show_option__exact='all',
		module_published=1
	)
	selected_modules = Module.objects.filter(
		module_show_option__exact='selected',
		module_published=1,
		module_menu_item=args['current_menu_item']
	)
	excluded_modules = Module.objects.filter(
		module_show_option__exact='except',
		module_published=1,
	).exclude(
		module_menu_item=args['current_menu_item']
	)
	args['modules'] = list(chain(all_modules, selected_modules, excluded_modules))
	return render(request, template_page, args)


@csrf_protect
def category_blog(request, category_alias, page_number=1):
	all_articles = Article.objects.filter(
		article_category__article_category_alias__exact=category_alias,
		article_published=1,
	).order_by('-id')
	articles_page = Paginator(all_articles, 20)
	args['category'] = ArticleCategory.objects.get(article_category_alias__exact=category_alias)
	args['articles'] = articles_page.page(page_number)
	template = Template.objects.get(template_default__exact=1)
	args['main_menu'] = MenuMenu.objects.get(id__exact=template.template_main_menu_id)
	args['menu_items'] = MenuItem.objects.filter(
		menu_item_menu=args['main_menu'],
		menu_item_published=1,
	)
	template_page = template.template_alias + str("/content/category_blog.html")
	args['current_menu_item'] = MenuItem.objects.get(
		menu_item_type__menu_type_alias="article-category-blog",
		menu_item_category_blog_menu_item_key__menu_item_category_blog_category__article_category_alias__exact=category_alias,
		menu_item_published=1,
	)
	all_modules = Module.objects.filter(
		module_show_option__exact='all',
		module_published=1
	)
	selected_modules = Module.objects.filter(
		module_show_option__exact='selected',
		module_published=1,
		module_menu_item=args['current_menu_item']
	)
	excluded_modules = Module.objects.filter(
		module_show_option__exact='except',
		module_published=1,
	).exclude(
		module_menu_item=args['current_menu_item']
	)
	args['modules'] = list(chain(all_modules, selected_modules, excluded_modules))
	return render(request, template_page, args)

@csrf_protect
def category_blog_article(request, article_alias, category_alias):
	args['article'] = article = Article.objects.get(
		article_alias__exact=article_alias,
		article_category__article_category_alias__exact=category_alias,
		article_published=1
	)
	template = Template.objects.get(template_default__exact=1)
	args['main_menu'] = MenuMenu.objects.get(id__exact=template.template_main_menu_id)
	args['menu_items'] = MenuItem.objects.filter(
		menu_item_menu=args['main_menu'],
		menu_item_published=1,
	)
	template_page = template.template_alias + str("/content/category_blog_article.html")
	args['current_menu_item'] = MenuItem.objects.get(
		menu_item_type__menu_type_alias="article-category-blog",
		menu_item_category_blog_menu_item_key__menu_item_category_blog_category__article_category_alias__exact=category_alias,
		menu_item_published=1,
	)
	all_modules = Module.objects.filter(
		module_show_option__exact='all',
		module_published=1
	)
	selected_modules = Module.objects.filter(
		module_show_option__exact='selected',
		module_published=1,
		module_menu_item=args['current_menu_item']
	)
	excluded_modules = Module.objects.filter(
		module_show_option__exact='except',
		module_published=1,
	).exclude(
		module_menu_item=args['current_menu_item']
	)
	args['modules'] = list(chain(all_modules, selected_modules, excluded_modules))
	return render(request, template_page, args)















