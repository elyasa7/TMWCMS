# -*- coding:utf-8 -*-

from __future__ import unicode_literals
from django.shortcuts import render, render_to_response, redirect
from django.http.response import HttpResponse, HttpResponseRedirect
import datetime

from django.core.exceptions import ObjectDoesNotExist
from django.views.decorators.csrf import csrf_protect
from django.template.context_processors import csrf

from mega_admin.models import *
from extension.models import Article, ArticleCategory
from template.models import Template, TemplatePosition
from module.models import *
from module.forms import *

from django.core.paginator import Paginator
# Create your views here.

args = {}
args['menu_categories'] = MenuCategory.objects.all()
args['menu_types'] = MenuType.objects.all()
args['menus'] = MenuMenu.objects.all()
args['languages'] = languages = Language.objects.all().order_by('id')
languages.exists()


@csrf_protect
def module_manager(request, page_number=1):
	all_modules = Module.objects.all().order_by('id')
	modules_page = Paginator(all_modules, 20)
	args['caption'] = str('Module manager')
	args['menu_items'] = MenuItem.objects.all()
	args['menus'] = MenuMenu.objects.all()
	args['modules'] = modules = modules_page.page(page_number)
	# if request.GET.get('menu') >= 1:
	# 	args['menu_item_menu'] = menu_item_menu = MenuMenu.objects.get(
	# 		id__exact=request.GET.get('menu')
	# 	)
	# 	all_menu_items = MenuItem.objects.filter(
	# 		menu_item_menu=menu_item_menu
	# 	).order_by('id')
	# 	menu_items_page = Paginator(all_menu_items, 20)
	# 	args['menu_items'] = menu_items = menu_items_page.page(page_number)
	return render(request, 'pages/mega_admin_module_manager.html', args)


@csrf_protect
def select_module(request):
	args['caption'] = str('Select module type')
	args['module_types'] = ModuleType.objects.all().order_by('module_type_title')
	return render(request, 'pages/mega_admin_select_module.html', args)


@csrf_protect
def add_module(request):
	args['caption'] = str('Module manager')
	try:
		args['current_module'] = current_module = Module.objects.get(id__exact=request.GET.get('id', ''))
	except:
		args['current_module'] = current_module =  None
	if args['current_module'] is not None:
		args['module_type'] = module_type = current_module.module_type
	else:
		args['module_type'] = module_type = ModuleType.objects.get(module_type_alias__exact=request.GET.get('module_type_id'))
	args['menus'] = MenuMenu.objects.all()
	args['categories'] = ArticleCategory.objects.all().order_by('article_category_title')
	args['menu_items'] = MenuItem.objects.all()
	args['templates'] = Template.objects.all().order_by('template_title')
	args['positions'] = TemplatePosition.objects.all().order_by(
		'template_position_name'
	)
	return render(request, 'pages/mega_admin_add_module.html', args)

@csrf_protect
def save_module(request):
	if request.POST:
		### Menu ITEM GENERAL values ###
		module_title = request.POST.get('module_title').decode().encode('utf-8')
		module_subtitle = request.POST.get('module_subtitle')
		module_type = request.POST.get('module_type', '')
		module_language = request.POST.get('module_language', '')
		module_menu_item = request.POST.getlist('module_menu_item_id')
		module_show_option = request.POST.get('module_show_option')
		module_position = request.POST.get('module_position', '0')
		module_layout = request.POST.get('module_layout')
		module_published = request.POST.get('module_published')
		if module_published == "on":
			module_published = "1"
		else:
			module_published = "0"
		module_show_title = request.POST.get('module_show_title')
		if module_show_title == "on":
			module_show_title = "1"
		else:
			module_show_title = "0"

		save_module_form = ModuleForm(request.POST)
		### Menu ITEM GENERAL values ###

		### CHECK MODULE TYPE ###
		if module_type == 'custom-html':
			try:
				module_type = ModuleType.objects.get(module_type_alias__exact=module_type)
			except:
				module_type = None

		if module_type == 'article-accordion':
			try:
				module_type = ModuleType.objects.get(module_type_alias__exact=module_type)
			except:
				module_type = None

		if module_type == 'article-slider':
			try:
				module_type = ModuleType.objects.get(module_type_alias__exact=module_type)
			except:
				module_type = None

		if module_type == 'article-list':
			try:
				module_type = ModuleType.objects.get(module_type_alias__exact=module_type)
			except:
				module_type = None

		if module_type == 'image-slider':
			try:
				module_type = ModuleType.objects.get(module_type_alias__exact=module_type)
			except:
				module_type = None

		### CHECK MODULE TYPE ###

		if module_type is not None:

			menu_item_custom_url = request.POST.get('menu_item_custom_url')
			menu_item_single_article_article = request.POST.get('menu_item_single_article_article')

			try:
				module = Module.objects.get(id=request.POST.get('current_module_id'))
			except:
				module = None

			if module is None:

				if save_module_form.is_valid():
					module = save_module_form.save(commit=False)
					module.module_title = module_title
					module.module_subtitle = module_subtitle
					module.module_type_id = module_type.id
					module.module_language_id = module_language
					module.module_show_option = module_show_option
					module.module_position_id = module_position
					module.module_published = module_published
					module.module_show_title = module_show_title
					module.module_layout = module_layout
					save_module_form.save()
					for selected_menu_item in module.module_menu_item.all():
						module.module_menu_item.remove(selected_menu_item)
					for module_menu in module_menu_item:
						try:
							module.module_menu_item.add(module_menu)
						except:
							pass
					if module_type.module_type_alias == 'custom-html':
						save_module_custom_html_form = ModuleCustomHtmlForm(request.POST)
						if save_module_custom_html_form.is_valid():
							module_custom_html = save_module_custom_html_form.save(commit=False)
							module_custom_html.module_custom_html_module = module
							module_custom_html.module_custom_html_content = request.POST.get('module_custom_html_content')
							module_custom_html.module_custom_html_layout = request.POST.get('module_custom_html_layout')
							save_module_custom_html_form.save()
							message = str("?message_type=success&message=")
							args['msg_txt'] = msg_txt = str("Module saved")
							return HttpResponseRedirect('/mega-admin/module/module-manager/' + message + msg_txt)
						else:
							module.delete()
							message = str("?message_type=error&message=")
							args['msg_txt'] = msg_txt = str("Error while saving. Form is not valid" + str("save_menu_item_custom_url_form"))
							return HttpResponseRedirect('/mega-admin/module/module-manager/' + message + msg_txt)
					elif module_type.module_type_alias == 'article-accordion':
						save_module_article_accordion_form = ModuleArticleAccordionForm(request.POST)
						if save_module_article_accordion_form.is_valid():
							module_article_accordion = save_module_article_accordion_form.save(commit=False)
							module_article_accordion.module_article_accordion_module = module
							module_article_accordion.module_article_accordion_category_id = request.POST.get('module_article_accordion_category')
							module_article_accordion.module_article_accordion_count = request.POST.get('module_article_accordion_count')
							if request.POST.get('module_article_accordion_feature') == "on":
								module_article_accordion.module_article_accordion_feature = 1
							else:
								module_article_accordion.module_article_accordion_feature = 0
							if request.POST.get('module_article_accordion_image') == "on":
								module_article_accordion.module_article_accordion_image = 1
							else:
								module_article_accordion.module_article_accordion_image = 0
							if request.POST.get('module_article_accordion_date') == "on":
								module_article_accordion.module_article_accordion_date = 1
							else:
								module_article_accordion.module_article_accordion_date = 0
							if request.POST.get('module_article_accordion_parent') == "on":
								module_article_accordion.module_article_accordion_parent = 1
							else:
								module_article_accordion.module_article_accordion_parent = 0
							module_article_accordion.module_article_accordion_button = request.POST.get('module_article_accordion_button')
							save_module_article_accordion_form.save()
							message = str("?message_type=success&message=")
							args['msg_txt'] = msg_txt = str("Module saved")
							return HttpResponseRedirect('/mega-admin/module/module-manager/' + message + msg_txt)
						else:
							module.delete()
							message = str("?message_type=error&message=")
							args['msg_txt'] = msg_txt = str("Error while saving. Form is not valid" + str("save_menu_item_custom_url_form"))
							return HttpResponseRedirect('/mega-admin/module/module-manager/' + message + msg_txt)
					elif module_type.module_type_alias == 'article-slider':
						save_module_article_slider_form = ModuleArticleSliderForm(request.POST)
						if save_module_article_slider_form.is_valid():
							module_article_slider = save_module_article_slider_form.save(commit=False)
							module_article_slider.module_article_slider_module = module
							module_article_slider.module_article_slider_category_id = request.POST.get('module_article_slider_category')
							module_article_slider.module_article_slider_count = request.POST.get('module_article_slider_count')
							if request.POST.get('module_article_slider_feature') == "on":
								module_article_slider.module_article_slider_feature = 1
							else:
								module_article_slider.module_article_slider_feature = 0
							if request.POST.get('module_article_slider_image') == "on":
								module_article_slider.module_article_slider_image = 1
							else:
								module_article_slider.module_article_slider_image = 0
							if request.POST.get('module_article_slider_date') == "on":
								module_article_slider.module_article_slider_date = 1
							else:
								module_article_slider.module_article_slider_date = 0
							if request.POST.get('module_article_slider_parent') == "on":
								module_article_slider.module_article_slider_parent = 1
							else:
								module_article_slider.module_article_slider_parent = 0
							module_article_slider.module_article_slider_button = request.POST.get('module_article_slider_button')
							save_module_article_slider_form.save()
							message = str("?message_type=success&message=")
							args['msg_txt'] = msg_txt = str("Module saved")
							return HttpResponseRedirect('/mega-admin/module/module-manager/' + message + msg_txt)
						else:
							module.delete()
							message = str("?message_type=error&message=")
							args['msg_txt'] = msg_txt = str("Error while saving. Form is not valid" + str("save_menu_item_custom_url_form"))
							return HttpResponseRedirect('/mega-admin/module/module-manager/' + message + msg_txt)
					elif module_type.module_type_alias == 'article-list':
						save_module_article_list_form = ModuleArticleListForm(request.POST)
						if save_module_article_list_form.is_valid():
							module_article_list = save_module_article_list_form.save(commit=False)
							module_article_list.module_article_list_module = module
							module_article_list.module_article_list_category_id = request.POST.get('module_article_list_category')
							module_article_list.module_article_list_main_count = request.POST.get('module_article_list_main_count')

							if request.POST.get('module_article_list_main_image') == "on":
								module_article_list.module_article_list_main_image = 1
							else:
								module_article_list.module_article_list_main_image = 0

							if request.POST.get('module_article_list_main_image_thumb') == "on":
								module_article_list.module_article_list_main_image_thumb = 1
							else:
								module_article_list.module_article_list_main_image_thumb = 0

							if request.POST.get('module_article_list_main_intro') == "on":
								module_article_list.module_article_list_main_intro = 1
							else:
								module_article_list.module_article_list_main_intro = 0

							module_article_list.module_article_list_main_intro_slice = request.POST.get('module_article_list_main_intro_slice')

							if request.POST.get('module_article_list_main_button') == "on":
								module_article_list.module_article_list_main_button = 1
							else:
								module_article_list.module_article_list_main_button = 0

							module_article_list.module_article_list_main_button_text = request.POST.get('module_article_list_main_button_text')
							module_article_list.module_article_list_main_layout = request.POST.get('module_article_list_main_layout')
							module_article_list.module_article_list_link_count = request.POST.get('module_article_list_link_count')

							if request.POST.get('module_article_list_link_image') == "on":
								module_article_list.module_article_list_link_image = 1
							else:
								module_article_list.module_article_list_link_image = 0

							if request.POST.get('module_article_list_link_image_thumb') == "on":
								module_article_list.module_article_list_link_image_thumb = 1
							else:
								module_article_list.module_article_list_link_image_thumb = 0

							if request.POST.get('module_article_list_link_intro') == "on":
								module_article_list.module_article_list_link_intro = 1
							else:
								module_article_list.module_article_list_link_intro = 0

							module_article_list.module_article_list_link_intro_slice = request.POST.get('module_article_list_link_intro_slice')

							if request.POST.get('module_article_list_link_button') == "on":
								module_article_list.module_article_list_link_button = 1
							else:
								module_article_list.module_article_list_link_button = 0

							module_article_list.module_article_list_link_button_text = request.POST.get('module_article_list_link_button_text')
							module_article_list.module_article_list_link_layout = request.POST.get('module_article_list_link_layout')
							save_module_article_list_form.save()
							message = str("?message_type=success&message=")
							args['msg_txt'] = msg_txt = str("Module saved")
							return HttpResponseRedirect('/mega-admin/module/module-manager/' + message + msg_txt)
						else:
							module.delete()
							message = str("?message_type=error&message=")
							args['msg_txt'] = msg_txt = str("Error while saving. Form is not valid" + str("save_menu_item_custom_url_form"))
							return HttpResponseRedirect('/mega-admin/module/module-manager/' + message + msg_txt)
					elif module_type.module_type_alias == 'image-slider':
						save_module_image_slider_form = ModuleImageSliderForm(request.POST)
						if save_module_image_slider_form.is_valid():
							module_image_slider = save_module_image_slider_form.save(commit=False)
							module_image_slider.module_image_slider_module = module
							module_image_slider.module_image_slider_speed = request.POST.get('module_image_slider_speed')

							if request.POST.get('module_image_slider_arrow') == "on":
								module_image_slider.module_image_slider_arrow = 1
							else:
								module_image_slider.module_image_slider_arrow = 0

							if request.POST.get('module_image_slider_bullet') == "on":
								module_image_slider.module_image_slider_bullet = 1
							else:
								module_image_slider.module_image_slider_bullet = 0

							if request.POST.get('module_image_slider_thumb') == "on":
								module_image_slider.module_image_slider_thumb = 1
							else:
								module_image_slider.module_image_slider_thumb = 0

							module_image_slider.module_image_slider_thumb_width = request.POST.get('module_image_slider_thumb_width')
							module_image_slider.module_image_slider_thumb_height = request.POST.get('module_image_slider_thumb_height')
							module_image_slider.module_image_slider_thumb_layout = request.POST.get('module_image_slider_thumb_layout')
							save_module_image_slider_form.save()
							message = str("?message_type=success&message=")
							args['msg_txt'] = msg_txt = str("Module saved")
							return HttpResponseRedirect('/mega-admin/module/module-manager/' + message + msg_txt)
						else:
							module.delete()
							message = str("?message_type=error&message=")
							args['msg_txt'] = msg_txt = str("Error while saving. Form is not valid" + str("save_menu_item_custom_url_form"))
							return HttpResponseRedirect('/mega-admin/module/module-manager/' + message + msg_txt)
					else:
						module.delete()
						message = str("?message_type=error&message=")
						args['msg_txt'] = msg_txt = str("Error while saving. Form is not valid")
						return HttpResponseRedirect('/mega-admin/module/module-manager/' + message + msg_txt)
				else:
					message = str("?message_type=error&message=")
					args['msg_txt'] = msg_txt = str("Error while saving. Form is not valid")
					return HttpResponseRedirect('/mega-admin/menu-items/' + message + msg_txt + str("save_menu_item_form"))
			else:
				module.module_title = module_title
				module.module_subtitle = module_subtitle
				module.module_type_id = module_type.id
				module.module_language_id = module_language
				module.module_show_option = module_show_option
				module.module_position_id = module_position
				module.module_published = module_published
				module.module_show_title = module_show_title
				module.module_layout = module_layout
				module.save()
				for selected_menu_item in module.module_menu_item.all():
					module.module_menu_item.remove(selected_menu_item)
				for module_menu in module_menu_item:
					try:
						module.module_menu_item.add(module_menu)
					except:
						pass
				if module_type.module_type_alias == 'custom-html':
					module_custom_html = ModuleCustomHtml.objects.get(id__exact=request.POST.get('module_custom_html_id', ''))
					module_custom_html.module_custom_html_content = request.POST.get('module_custom_html_content')
					module_custom_html.module_custom_html_layout = request.POST.get('module_custom_html_layout')
					module_custom_html.save()
					message = str("?message_type=success&message=")
					args['msg_txt'] = msg_txt = str("Module saved")
					return HttpResponseRedirect('/mega-admin/module/module-manager/' + message + msg_txt)
				elif module_type.module_type_alias == 'article-accordion':
					module_article_accordion = ModuleArticleAccordion.objects.get(id__exact=request.POST.get('module_article_accordion_id', ''))
					module_article_accordion.module_article_accordion_module = module
					module_article_accordion.module_article_accordion_category_id = request.POST.get(
						'module_article_accordion_category')
					module_article_accordion.module_article_accordion_count = request.POST.get(
						'module_article_accordion_count')
					if request.POST.get('module_article_accordion_feature') == "on":
						module_article_accordion.module_article_accordion_feature = 1
					else:
						module_article_accordion.module_article_accordion_feature = 0
					if request.POST.get('module_article_accordion_image') == "on":
						module_article_accordion.module_article_accordion_image = 1
					else:
						module_article_accordion.module_article_accordion_image = 0
					if request.POST.get('module_article_accordion_date') == "on":
						module_article_accordion.module_article_accordion_date = 1
					else:
						module_article_accordion.module_article_accordion_date = 0
					if request.POST.get('module_article_accordion_parent') == "on":
						module_article_accordion.module_article_accordion_parent = 1
					else:
						module_article_accordion.module_article_accordion_parent = 0
					module_article_accordion.module_article_accordion_button = request.POST.get(
						'module_article_accordion_button')
					module_article_accordion.save()
					message = str("?message_type=success&message=")
					args['msg_txt'] = msg_txt = str("Module saved")
					return HttpResponseRedirect('/mega-admin/module/module-manager/' + message + msg_txt)
				elif module_type.module_type_alias == 'article-slider':
					module_article_slider = ModuleArticleSlider.objects.get(id__exact=request.POST.get('module_article_slider_id', ''))
					module_article_slider.module_article_slider_module = module
					module_article_slider.module_article_slider_category_id = request.POST.get('module_article_slider_category')
					module_article_slider.module_article_slider_count = request.POST.get('module_article_slider_count')
					if request.POST.get('module_article_slider_feature') == "on":
						module_article_slider.module_article_slider_feature = 1
					else:
						module_article_slider.module_article_slider_feature = 0
					if request.POST.get('module_article_slider_image') == "on":
						module_article_slider.module_article_slider_image = 1
					else:
						module_article_slider.module_article_slider_image = 0
					if request.POST.get('module_article_slider_date') == "on":
						module_article_slider.module_article_slider_date = 1
					else:
						module_article_slider.module_article_slider_date = 0
					if request.POST.get('module_article_slider_parent') == "on":
						module_article_slider.module_article_slider_parent = 1
					else:
						module_article_slider.module_article_slider_parent = 0
					module_article_slider.module_article_slider_button = request.POST.get('module_article_slider_button')
					module_article_slider.save()
					message = str("?message_type=success&message=")
					args['msg_txt'] = msg_txt = str("Module saved")
					return HttpResponseRedirect('/mega-admin/module/module-manager/' + message + msg_txt)
				elif module_type.module_type_alias == 'article-list':
					module_article_list = ModuleArticleList.objects.get(id__exact=request.POST.get('module_article_list_id', ''))
					module_article_list.module_article_list_module = module
					module_article_list.module_article_list_category_id = request.POST.get('module_article_list_category')
					module_article_list.module_article_list_main_count = request.POST.get(
						'module_article_list_main_count')

					if request.POST.get('module_article_list_main_image') == "on":
						module_article_list.module_article_list_main_image = 1
					else:
						module_article_list.module_article_list_main_image = 0

					if request.POST.get('module_article_list_main_image_thumb') == "on":
						module_article_list.module_article_list_main_image_thumb = 1
					else:
						module_article_list.module_article_list_main_image_thumb = 0

					if request.POST.get('module_article_list_main_intro') == "on":
						module_article_list.module_article_list_main_intro = 1
					else:
						module_article_list.module_article_list_main_intro = 0

					module_article_list.module_article_list_main_intro_slice = request.POST.get(
						'module_article_list_main_intro_slice')

					if request.POST.get('module_article_list_main_button') == "on":
						module_article_list.module_article_list_main_button = 1
					else:
						module_article_list.module_article_list_main_button = 0

					module_article_list.module_article_list_main_button_text = request.POST.get(
						'module_article_list_main_button_text')
					module_article_list.module_article_list_main_layout = request.POST.get(
						'module_article_list_main_layout')
					module_article_list.module_article_list_link_count = request.POST.get(
						'module_article_list_link_count')

					if request.POST.get('module_article_list_link_image') == "on":
						module_article_list.module_article_list_link_image = 1
					else:
						module_article_list.module_article_list_link_image = 0

					if request.POST.get('module_article_list_link_image_thumb') == "on":
						module_article_list.module_article_list_link_image_thumb = 1
					else:
						module_article_list.module_article_list_link_image_thumb = 0

					if request.POST.get('module_article_list_link_intro') == "on":
						module_article_list.module_article_list_link_intro = 1
					else:
						module_article_list.module_article_list_link_intro = 0

					module_article_list.module_article_list_link_intro_slice = request.POST.get(
						'module_article_list_link_intro_slice')

					if request.POST.get('module_article_list_link_button') == "on":
						module_article_list.module_article_list_link_button = 1
					else:
						module_article_list.module_article_list_link_button = 0

					module_article_list.module_article_list_link_button_text = request.POST.get(
						'module_article_list_link_button_text')
					module_article_list.module_article_list_link_layout = request.POST.get(
						'module_article_list_link_layout')
					module_article_list.save()
					message = str("?message_type=success&message=")
					args['msg_txt'] = msg_txt = str("Module saved")
					return HttpResponseRedirect('/mega-admin/module/module-manager/' + message + msg_txt)
				elif module_type.module_type_alias == 'image-slider':
					module_image_slider = ModuleImageSlider.objects.get(id__exact=request.POST.get('module_image_slider_id', ''))
					module_image_slider.module_image_slider_module = module
					module_image_slider.module_image_slider_speed = request.POST.get('module_image_slider_speed')

					if request.POST.get('module_image_slider_arrow') == "on":
						module_image_slider.module_image_slider_arrow = 1
					else:
						module_image_slider.module_image_slider_arrow = 0

					if request.POST.get('module_image_slider_bullet') == "on":
						module_image_slider.module_image_slider_bullet = 1
					else:
						module_image_slider.module_image_slider_bullet = 0

					if request.POST.get('module_image_slider_thumb') == "on":
						module_image_slider.module_image_slider_thumb = 1
					else:
						module_image_slider.module_image_slider_thumb = 0

					module_image_slider.module_image_slider_thumb_width = request.POST.get(
						'module_image_slider_thumb_width')
					module_image_slider.module_image_slider_thumb_height = request.POST.get(
						'module_image_slider_thumb_height')
					module_image_slider.module_image_slider_thumb_layout = request.POST.get(
						'module_image_slider_thumb_layout')
					module_image_slider.save()
					message = str("?message_type=success&message=")
					args['msg_txt'] = msg_txt = str("Module saved")
					return HttpResponseRedirect('/mega-admin/module/module-manager/' + message + msg_txt)
				else:
					message = str("?message_type=success&message=")
					args['msg_txt'] = msg_txt = str("Error. Save method need to be POST")
					return HttpResponseRedirect('/mega-admin/module/module-manager/' + message + msg_txt)
	else:
		message = str("?message_type=success&message=")
		args['msg_txt'] = msg_txt = str("Error. Save method need to be POST")
		return HttpResponseRedirect('/mega-admin/module/module-manager/' + message + msg_txt)