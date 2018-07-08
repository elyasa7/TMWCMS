# -*- coding:utf-8 -*-

from __future__ import unicode_literals
from django.shortcuts import render, render_to_response, redirect
from django.http.response import HttpResponse, HttpResponseRedirect
import datetime

from django.core.exceptions import ObjectDoesNotExist
from django.views.decorators.csrf import csrf_protect
from django.template.context_processors import csrf

from mega_admin.forms import *
from mega_admin.models import *
from extension.models import Article, ArticleCategory
from template.models import Template, TemplatePosition
from module.models import *

from django.core.paginator import Paginator
from itertools import chain
# Create your views here.

args = {}
args['menu_categories'] = MenuCategory.objects.all()
args['menu_types'] = MenuType.objects.all()
args['menus'] = MenuMenu.objects.all()
args['languages'] = languages = Language.objects.all().order_by('id')
languages.exists()


@csrf_protect
def homepage(request):
	args['lang_prefix'] = "ru"
	args['today'] = datetime.date.today()
	args['tomorrow'] = datetime.date.today() + datetime.timedelta(days=1)
	#	args['article'] = Article.objects.get(id=1, article_language='ru')
	#	args['menus'] = Menu.objects.all().order_by('menu_position', 'id')
	template = Template.objects.get(template_default__exact=1)
	template_page = template.template_alias + str("/") + template.template_alias + str("_blank.html")
	args['main_menu'] = MenuMenu.objects.get(id__exact=template.template_main_menu_id)
	args['menu_items'] = MenuItem.objects.filter(
		menu_item_menu=args['main_menu'],
		menu_item_published=1,
	)
	args['current_menu_item'] = MenuItem.objects.get(
		menu_item_type__menu_type_alias="system-custom-url",
		menu_item_custom_url_menu_item_key__menu_item_custom_url= "/"
	)
	all_modules = Module.objects.filter(
		module_show_option__exact='all',
		module_published=1
	)
	selected_modules = Module.objects.filter(
		module_show_option__exact='selected',
		module_published=1,
		module_menu_item = args['current_menu_item']
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
def homepage_demo(request):
	args['lang_prefix'] = "ru"
	args['today'] = datetime.date.today()
	args['tomorrow'] = datetime.date.today() + datetime.timedelta(days=1)
	#	args['article'] = Article.objects.get(id=1, article_language='ru')
	#	args['menus'] = Menu.objects.all().order_by('menu_position', 'id')
	return render(request, 'homepage-ru.html', args)


@csrf_protect
def mega_home(request):
	#	args.update(csrf(request))
	#	args['lang_prefix'] = "ru"
	args['title'] = "Mega-Admin v1.0 Dashboard"
	args['today'] = datetime.date.today()
	args['tomorrow'] = datetime.date.today() + datetime.timedelta(days=1)
	args['categories'] = ArticleCategory.objects.all()[:4]
	args['articles'] = Article.objects.all().order_by('-id')[:10]
	return render(request, 'mega_admin_home.html', args)


@csrf_protect
def menu_manager(request):
	args['caption'] = str('Menu Manager')
	args['current_menu'] = str("menus")
	return render(request, 'mega_admin_menus.html', args)


@csrf_protect
def menu_languages(request):
	args['current_menu'] = str("languages")
	args['languages'] = languages = Language.objects.all().order_by('id')
	language_config = LanguageConfiguration.objects.get(lang_config_alias__exact="system_lang_config_multi")
	return render(request, 'mega_admin_languages.html', args)


@csrf_protect
def menu_languages_config(request):
	args['current_menu'] = str("languages-config")
	args['language_config'] = LanguageConfiguration.objects.get(lang_config_alias__exact="system_lang_config_multi")
	return render(request, 'mega_admin_languages_config.html', args)


@csrf_protect
def menu_items(request, page_number=1):
	all_menu_items = MenuItem.objects.all().order_by('id')
	menu_items_page = Paginator(all_menu_items, 20)
	args['categories'] = menu_items_page.page(page_number)
	args['caption'] = str('Menu Items')
	args['current_menu'] = str("menu-items")
	args['menu_items'] = menu_items = menu_items_page.page(page_number)
	if request.GET.get('menu') >= 1:
		args['menu_item_menu'] = menu_item_menu = MenuMenu.objects.get(
			id__exact=request.GET.get('menu')
		)
		all_menu_items = MenuItem.objects.filter(
			menu_item_menu=menu_item_menu
		).order_by('id')
		menu_items_page = Paginator(all_menu_items, 20)
		args['menu_items'] = menu_items = menu_items_page.page(page_number)
	return render(request, 'mega_admin_menu_items.html', args)


@csrf_protect
def add_menu_item(request):
	args['caption'] = str("Add or edit menu item")
	args['articles'] = Article.objects.all().order_by('-id')
	args['categories'] = ArticleCategory.objects.all().order_by('-id')
	try:
		args['current_menu_item'] = current_menu_item = MenuItem.objects.get(
			id__exact=request.GET.get('id', '')
		)
	except:
		args['current_menu_item'] = current_menu_item = None
	args['menus'] = MenuMenu.objects.all().order_by('menu_menu_title')
	if current_menu_item is not None:
		args['menu_items'] = MenuItem.objects.filter(
			menu_item_menu=current_menu_item.menu_item_menu
		).exclude(
			id__exact=current_menu_item.id
		)
		args['menu_item_type'] = menu_item_type = MenuType.objects.get(
			id__exact=current_menu_item.menu_item_type_id
		)
		if menu_item_type.menu_type_alias == "system-custom-url":
			args['custom_url'] = MenuItemCustomUrl.objects.get(menu_item_custom_url_menu_item=current_menu_item)
		elif menu_item_type.menu_type_alias == "single-article":
			args['single_article'] = MenuItemSingleArticle.objects.get(menu_item_single_article_menu_item=current_menu_item)
		elif menu_item_type.menu_type_alias == "article-category-blog":
			args['category_blog'] = MenuItemCategoryBlog.objects.get(menu_item_category_blog_menu_item=current_menu_item)
	else:
		args['menu_item_type'] = MenuType.objects.get(
			menu_type_alias__exact=request.GET.get('item-type-id', '')
		)
	return render(request, 'mega_admin_add_menu_item.html', args)


@csrf_protect
def save_menu_item(request):
	if request.POST:
		### Menu ITEM GENERAL values ###
		menu_item_title = request.POST.get('menu_item_title').decode().encode('utf-8')
		menu_item_subtitle = request.POST.get('menu_item_subtitle')
		menu_item_type = request.POST.get('menu_item_type', '')
		menu_item_language = request.POST.get('menu_item_language', '')
		menu_item_menu = request.POST.get('menu_item_menu', '')
		menu_item_parent_item = request.POST.get('menu_item_parent_item')
		menu_item_position = request.POST.get('menu_item_position', '0')
		menu_item_published = request.POST.get('menu_item_published')
		if menu_item_published == "on":
			menu_item_published = "1"
		else:
			menu_item_published = "0"
		save_menu_item_form = MenuItemForm(request.POST)
		### Menu ITEM GENERAL values ###

		### CHECK MENU ITEM TYPE ###
		if menu_item_type == 'system-custom-url':
			try:
				menu_item_type = MenuType.objects.get(menu_type_alias__exact=menu_item_type)
			except:
				menu_item_type = None

		if menu_item_type == 'single-article':
			try:
				menu_item_type = MenuType.objects.get(menu_type_alias__exact=menu_item_type)
			except:
				menu_item_type = None

		if menu_item_type == 'article-category-blog':
			try:
				menu_item_type = MenuType.objects.get(menu_type_alias__exact=menu_item_type)
			except:
				menu_item_type = None
		### CHECK MENU ITEM TYPE ###

		if menu_item_type is not None:

			menu_item_custom_url = request.POST.get('menu_item_custom_url')
			menu_item_single_article_article = request.POST.get('menu_item_single_article_article')

			try:
				menu_item = MenuItem.objects.get(id=request.POST.get('current_menu_item_id'))
			except:
				menu_item = None
			if menu_item is None:
				if save_menu_item_form.is_valid():
					menu_item = save_menu_item_form.save(commit=False)
					menu_item.menu_item_title = menu_item_title
					menu_item.menu_item_subtitle = menu_item_subtitle
					menu_item.menu_item_type_id = menu_item_type.id
					menu_item.menu_item_language_id = menu_item_language
					menu_item.menu_item_menu_id = menu_item_menu
					menu_item.menu_item_parent_item_id = menu_item_parent_item
					menu_item.menu_item_position = menu_item_position
					menu_item.menu_item_published = menu_item_published
					save_menu_item_form.save()
					if menu_item_type.menu_type_alias == 'system-custom-url':
						save_menu_item_custom_url_form = MenuItemCustomUrlForm(request.POST)
						if save_menu_item_custom_url_form.is_valid():
							save_menu_item_custom_url = save_menu_item_custom_url_form.save(commit=False)
							save_menu_item_custom_url.menu_item_custom_url = request.POST.get('menu_item_custom_url')
							save_menu_item_custom_url.menu_item_custom_url_menu_item = menu_item
							save_menu_item_custom_url_form.save()
							message = str("?message_type=success&message=")
							args['msg_txt'] = msg_txt = str("Menu item '") + str(menu_item_title).encode('utf8') + str("' saved")
							return HttpResponseRedirect('/mega-admin/menu-items/' + message + msg_txt)
						else:
							menu_item.delete()
							message = str("?message_type=error&message=")
							args['msg_txt'] = msg_txt = str("Error while saving. Form is not valid" + str("save_menu_item_custom_url_form"))
							return HttpResponseRedirect('/mega-admin/menu-items/' + message + msg_txt)
					elif menu_item_type.menu_type_alias == 'single-article':
						save_menu_item_single_article_form = MenuItemSingleArticleForm(request.POST)
						if save_menu_item_single_article_form.is_valid():
							save_menu_item_single_article = save_menu_item_single_article_form.save(commit=False)
							save_menu_item_single_article.menu_item_single_article_article_id = request.POST.get('menu_item_single_article_article_id')
							save_menu_item_single_article.menu_item_single_article_menu_item = menu_item
							save_menu_item_single_article_form.save()
							message = str("?message_type=success&message=")
							args['msg_txt'] = msg_txt = str("Menu item '") + str(menu_item_title).encode('utf8') + str("' saved")
							return HttpResponseRedirect('/mega-admin/menu-items/' + message + msg_txt)
						else:
							menu_item.delete()
							message = str("?message_type=error&message=")
							args['msg_txt'] = msg_txt = str("Error while saving. Form is not valid" + str("save_menu_item_custom_url_form"))
							return HttpResponseRedirect('/mega-admin/menu-items/' + message + msg_txt)
					elif menu_item_type.menu_type_alias == 'article-category-blog':
						save_menu_item_category_blog_form = MenuItemCategoryBlogForm(request.POST)
						if save_menu_item_category_blog_form.is_valid():
							save_menu_item_category_blog = save_menu_item_category_blog_form.save(commit=False)
							save_menu_item_category_blog.menu_item_category_blog_category_id = request.POST.get('menu_item_category_blog_category_id')
							save_menu_item_category_blog.menu_item_category_blog_menu_item = menu_item
							save_menu_item_category_blog_form.save()
							message = str("?message_type=success&message=")
							args['msg_txt'] = msg_txt = str("Menu item '") + str(menu_item_title).encode('utf8') + str("' saved")
							return HttpResponseRedirect('/mega-admin/menu-items/' + message + msg_txt)
						else:
							menu_item.delete()
							message = str("?message_type=error&message=")
							args['msg_txt'] = msg_txt = str("Error while saving. Form is not valid" + str("save_menu_item_custom_url_form"))
							return HttpResponseRedirect('/mega-admin/menu-items/' + message + msg_txt)
					else:
						menu_item.delete()
						message = str("?message_type=error&message=")
						args['msg_txt'] = msg_txt = str("Error while saving. Form is not valid")
						return HttpResponseRedirect('/mega-admin/menu-items/' + message + msg_txt)
				else:
					message = str("?message_type=error&message=")
					args['msg_txt'] = msg_txt = str("Error while saving. Form is not valid")
					return HttpResponseRedirect('/mega-admin/menu-items/' + message + msg_txt + str("save_menu_item_form"))
			else:
				menu_item = MenuItem.objects.get(id=request.POST.get('current_menu_item_id'))
				menu_item.menu_item_title = menu_item_title
				menu_item.menu_item_subtitle = menu_item_subtitle
				menu_item.menu_item_type_id = menu_item_type.id
				menu_item.menu_item_language_id = menu_item_language
				menu_item.menu_item_menu_id = menu_item_menu
				menu_item.menu_item_parent_item_id = menu_item_parent_item
				menu_item.menu_item_position = menu_item_position
				menu_item.menu_item_published = menu_item_published
				menu_item.save()
				if menu_item.menu_item_type.menu_type_alias == 'system-custom-url':
					save_menu_item_custom_url = MenuItemCustomUrl.objects.get(id__exact=request.POST.get('menu_item_custom_url_id', ''))
					save_menu_item_custom_url.menu_item_custom_url = request.POST.get('menu_item_custom_url')
					save_menu_item_custom_url.menu_item_custom_url_menu_item = menu_item
					save_menu_item_custom_url.save()
					message = str("?message_type=success&message=")
					args['msg_txt'] = msg_txt = str(str("Menu Item '") + str(menu_item_title) + str("' saved")).encode(encoding="utf-8")
					return HttpResponseRedirect('/mega-admin/menu-items/' + message + msg_txt)
				elif menu_item.menu_item_type.menu_type_alias == 'single-article':
					save_menu_item_single_article = MenuItemSingleArticle.objects.get(id__exact=request.POST.get('menu_item_single_article_article', ''))
					save_menu_item_single_article.menu_item_single_article_article_id = request.POST.get('menu_item_single_article_article_id')
					save_menu_item_single_article.menu_item_single_article_menu_item = menu_item
					save_menu_item_single_article.save()
					message = str("?message_type=success&message=")
					args['msg_txt'] = msg_txt = str("Menu Item '") + str(menu_item_title).encode('utf8') + str("' saved")
					return HttpResponseRedirect('/mega-admin/menu-items/' + message + msg_txt)
				elif menu_item.menu_item_type.menu_type_alias == 'article-category-blog':
					menu_item_category_blog = MenuItemCategoryBlog.objects.get(id__exact=request.POST.get('menu_item_category_blog_category', ''))
					menu_item_category_blog.menu_item_category_blog_category_id = request.POST.get('menu_item_category_blog_category_id')
					menu_item_category_blog.menu_item_category_blog_menu_item = menu_item
					menu_item_category_blog.save()
					message = str("?message_type=success&message=")
					args['msg_txt'] = msg_txt = str("Menu Item '") + str(menu_item_title).encode('utf8') + str("' saved")
					return HttpResponseRedirect('/mega-admin/menu-items/' + message + msg_txt)
				else:
					message = str("?message_type=success&message=")
					args['msg_txt'] = msg_txt = str("Error. Save method need to be POST")
					return HttpResponseRedirect('/mega-admin/menu-items/' + message + msg_txt)
	else:
		message = str("?message_type=success&message=")
		args['msg_txt'] = msg_txt = str("Error. Save method need to be POST")
		return HttpResponseRedirect('/mega-admin/menu-items/' + message + msg_txt)

@csrf_protect
def change_menu_item_state(request):
	if request.POST:
		try:
			menu_item_id = (request.POST.get('menu_item_id'))
			menu_item = MenuItem.objects.get(id__exact=menu_item_id)
			if menu_item.menu_item_published == 1:
				menu_item.menu_item_published = 0
				menu_item.save(update_fields=['menu_item_published'])
				return HttpResponseRedirect(request.META.get('HTTP_REFERER', '/'), args)
			else:
				menu_item.menu_item_published = 1
				menu_item.save(update_fields=['menu_item_published'])
				return HttpResponseRedirect(request.META.get('HTTP_REFERER', '/'), args)
		except ObjectDoesNotExist:
			menu_item = None
			return HttpResponseRedirect(request.META.get('HTTP_REFERER', '/'), args)

@csrf_protect
def add_menu_category(request):
	if request.POST:
		menu_category_title = request.POST.get('menu_category_title')
		menu_category_alias = request.POST.get('menu_category_alias')
		menu_category_description = request.POST.get('menu_category_description')
		add_menu_category_form = MenuCategoryForm(request.POST)
		if add_menu_category_form.is_valid():
			menu_category = add_menu_category_form.save(commit=False)
			menu_category.menu_category_title = menu_category_title
			menu_category.menu_category_alias = menu_category_alias
			menu_category.menu_category_description = menu_category_description
			add_menu_category_form.save()
			args['success'] = str("New category menu '") + str(menu_category_title) + str("' created")
			return HttpResponseRedirect(request.META.get('HTTP_REFERER', '/'), args)
		else:
			args['error'] = str("Form is not valid")
			return HttpResponseRedirect(request.META.get('HTTP_REFERER', '/'), args)
	else:
		args['error'] = str("Method need to be POST!")
		return HttpResponseRedirect(request.META.get('HTTP_REFERER', '/'), args)


@csrf_protect
def add_menu_type(request):
	if request.POST:
		menu_type_category = request.POST.get('menu_type_category')
		menu_type_title = request.POST.get('menu_type_title')
		menu_type_alias = request.POST.get('menu_type_alias')
		menu_type_description = request.POST.get('menu_type_description')
		add_menu_type_form = MenuTypeForm(request.POST)
		if add_menu_type_form.is_valid():
			menu_type = add_menu_type_form.save(commit=False)
			menu_type.menu_type_category_id = menu_type_category
			menu_type.menu_type_title = menu_type_title
			menu_type.menu_type_alias = menu_type_alias
			menu_type.menu_type_description = menu_type_description
			add_menu_type_form.save()
			args['success'] = str("New category menu '") + str(menu_type_title) + str("' created")
			return HttpResponseRedirect(request.META.get('HTTP_REFERER', '/'), args)
		else:
			args['error'] = str("Form is not valid")
			return HttpResponseRedirect(request.META.get('HTTP_REFERER', '/'), args)
	else:
		args['error'] = str("Method need to be POST!")
		return HttpResponseRedirect(request.META.get('HTTP_REFERER', '/'), args)


@csrf_protect
def add_menu(request):
	if request.POST:
		menu_menu_title = request.POST.get('menu_menu_title')
		menu_menu_alias = request.POST.get('menu_menu_alias')
		menu_menu_description = request.POST.get('menu_menu_description')
		add_menu_form = MenuMenuForm(request.POST)
		if add_menu_form.is_valid():
			menu = add_menu_form.save(commit=False)
			menu.menu_menu_title = menu_menu_title
			menu.menu_menu_alias = menu_menu_alias
			menu.menu_menu_description = menu_menu_description
			add_menu_form.save()
			args['success'] = str("New category menu '") + str(menu_menu_title) + str("' created")
			return HttpResponseRedirect(request.META.get('HTTP_REFERER', '/'), args)
		else:
			args['error'] = str("Form is not valid")
			return HttpResponseRedirect(request.META.get('HTTP_REFERER', '/'), args)
	else:
		args['error'] = str("Method need to be POST!")
		return HttpResponseRedirect(request.META.get('HTTP_REFERER', '/'), args)


@csrf_protect
def add_language(request):
	if request.POST:
		lang_code = request.POST.get('lang_sef')
		lang_title = request.POST.get('lang_title')
		lang_title_native = request.POST.get('lang_title_native')
		lang_sef = request.POST.get('lang_sef')
		lang_description = request.POST.get('lang_description')
		add_language_form = LanguageForm(request.POST)
		if add_language_form.is_valid():
			language = add_language_form.save(commit=False)
			language.lang_code = lang_code
			language.lang_title = lang_title
			language.lang_title_native = lang_title_native
			language.lang_sef = lang_sef
			language.lang_description = lang_description
			language.lang_published = "1"
			add_language_form.save()
			args['success'] = str("New language '") + str(lang_title) + str("' created")
			return HttpResponseRedirect(request.META.get('HTTP_REFERER', '/'), args)
		else:
			args['error'] = str("Form is not valid")
			return HttpResponseRedirect(request.META.get('HTTP_REFERER', '/'), args)
	else:
		args['error'] = str("Method need to be POST!")
		return HttpResponseRedirect(request.META.get('HTTP_REFERER', '/'), args)


@csrf_protect
def change_language_default(request):
	if request.POST:
		try:
			cur_language = Language.objects.get(lang_default=1)
			cur_language.lang_default = 0
			cur_language.save(update_fields=['lang_default'])
		except ObjectDoesNotExist:
			cur_language = None
		current_default_languages = Language.objects.filter(lang_default=1)
		if current_default_languages.count() < 1:
			lang_id = (request.POST.get('lang_id'))
			language = Language.objects.get(id=lang_id)
			language.lang_default = 1
			language.save(update_fields=['lang_default'])
			return HttpResponseRedirect('/mega-admin/languages/')
		else:
			return HttpResponseRedirect('/mega-admin/languages/')


@csrf_protect
def change_language_delete(request):
	if request.POST:
		try:
			lang_id = (request.POST.get('lang_id'))
			language = Language.objects.get(id=lang_id)
			language.delete()
			return HttpResponseRedirect('/mega-admin/languages/')
		except ObjectDoesNotExist:
			cur_language = None
			return HttpResponseRedirect('/mega-admin/languages/')


@csrf_protect
def change_language_state(request):
	if request.POST:
		try:
			lang_id = (request.POST.get('lang_id'))
			language = Language.objects.get(id=lang_id)
			if language.lang_published == 1:
				language.lang_published = 0
				language.save(update_fields=['lang_published'])
				return HttpResponseRedirect(request.META.get('HTTP_REFERER', '/'), args)
			else:
				language.lang_published = 1
				language.save(update_fields=['lang_published'])
				return HttpResponseRedirect(request.META.get('HTTP_REFERER', '/'), args)
		except ObjectDoesNotExist:
			language = None
			return HttpResponseRedirect(request.META.get('HTTP_REFERER', '/'), args)


@csrf_protect
def change_language_configuration(request):
	if request.POST:
		try:
			lang_config_multi = (request.POST.get('lang_config_multi'))
			if lang_config_multi == str("on"):
				lang_config_multi = 1
			else:
				lang_config_multi = 0
			language_config = LanguageConfiguration.objects.get(lang_config_alias__exact="system_lang_config_multi")
			language_config.lang_config_multi = lang_config_multi
			language_config.save(update_fields=['lang_config_multi'])
			return HttpResponseRedirect(request.META.get('HTTP_REFERER', '/'), args)
		except ObjectDoesNotExist:
			language_config = None
			return HttpResponseRedirect(request.META.get('HTTP_REFERER', '/'), args)
