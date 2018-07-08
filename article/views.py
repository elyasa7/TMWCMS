# -*- coding:utf-8 -*-

from django.shortcuts import render, render_to_response, redirect
from django.http.response import HttpResponse
from django.http import HttpResponseRedirect
from django.template.loader import get_template
from django.template import Context
from django.template import RequestContext


from django.core.exceptions import ObjectDoesNotExist
from django.core.context_processors import csrf
from django.core.urlresolvers import reverse
from datetime import date, timedelta
import datetime
# from PIL import Image
from django.conf import settings
from django.contrib.syndication.views import Feed
from django.contrib import auth
from django.core.mail import send_mail
from django.core.mail import EmailMultiAlternatives


# Create your views here.

def homepage(request):
	args = {}
	args.update(csrf(request))
	args['lang_prefix'] = "ru"
	args['today'] = datetime.date.today()
	args['tomorrow'] = datetime.date.today() + datetime.timedelta(days=1)
#	args['article'] = Article.objects.get(id=1, article_language='ru')
#	args['menus'] = Menu.objects.all().order_by('menu_position', 'id')
	return render_to_response('homepage-ru.html', args)


# def development(request):
# 	args = {}
# 	args.update(csrf(request))
# 	args['lang_prefix'] = "ru"
# 	args['today'] = datetime.date.today()
# 	args['tomorrow'] = datetime.date.today() + datetime.timedelta(days=1)
# 	args['article'] = Article.objects.get(id=2, article_language='ru')
# 	args['menus'] = Menu.objects.all().order_by('menu_position', 'id')
# 	return render_to_response('homepage-ru.html', args)
#
#
# def ssl(request):
# 	args = {}
# 	args.update(csrf(request))
# 	args['lang_prefix'] = "ru"
# 	args['today'] = datetime.date.today()
# 	args['tomorrow'] = datetime.date.today() + datetime.timedelta(days=1)
# 	args['article'] = Article.objects.get(id=3, article_language='ru')
# 	args['menus'] = Menu.objects.all().order_by('menu_position', 'id')
# 	return render_to_response('homepage-ru.html', args)
#
#
# def avast(request):
# 	args = {}
# 	args.update(csrf(request))
# 	args['lang_prefix'] = "ru"
# 	args['article'] = Article.objects.get(id=7, article_language='ru')
# 	args['menus'] = Menu.objects.all().order_by('menu_position', 'id')
# 	return render_to_response('homepage-ru.html', args)
#
#
# def blogs(request):
# 	args = {}
# 	args.update(csrf(request))
# 	args['lang_prefix'] = "ru"
# 	args['article'] = Article.objects.filter(article_category_id=5, article_language='ru')
# 	args['menus'] = Menu.objects.all().order_by('menu_position', 'id')
# 	return render_to_response('homepage-ru.html', args)
#
#
# def contact(request):
# 	args = {}
# 	args.update(csrf(request))
# 	args['lang_prefix'] = "ru"
# 	args['article'] = Article.objects.get(id=8, article_language='ru')
# 	args['menus'] = Menu.objects.all().order_by('menu_position', 'id')
# 	return render_to_response('homepage-ru.html', args)
#
#
# def not_found(request):
# 	response.status_code = 404
# 	args = {}
# 	args.update(csrf(request))
# 	args['lang_prefix'] = "ru"
# 	args['article'] = Article.objects.get(id=9, article_language='ru')
# 	args['menus'] = Menu.objects.all().order_by('menu_position', 'id')
# 	return render_to_response('homepage-ru.html', args)
#
#
# def single_article(request, article_id, menu):
# 	args = {}
# 	args.update(csrf(request))
# 	args['lang_prefix'] = "ru"
# 	args['today'] = datetime.date.today()
# 	args['tomorrow'] = datetime.date.today() + datetime.timedelta(days=1)
# 	args['article'] = Article.objects.get(id=article_id, article_language='ru')
# 	args['menus'] = Menu.objects.all().order_by('menu_position', 'id')
# 	args['curmenu'] = Menu.objects.filter(menu_description=menu)
# 	return render_to_response('homepage-ru.html', args)
#
#
# #######################################################################
# ##########          ###########           ############         ########
# #######################################################################
#
#
# def about_ru(request):
# 	args = {}
# 	args.update(csrf(request))
# 	args['lang_prefix'] = "ru"
# 	args['title'] = "Добро Пожаловать | ОТЕЛЬ ОГУЗКЕНТ АШХАБАД"
# 	args['article'] = Article.objects.get(article_category_id=1, article_language='ru')
# 	args['minigals'] = ArticleImage.objects.filter(article_image_article_id=args['article'].id).order_by('id')[:6]
# 	return render_to_response('activity-ru.html', args)
#
#
# def about_en(request):
# 	args = {}
# 	args.update(csrf(request))
# 	args['lang_prefix'] = "en"
# 	args['title'] = "Welcome | HOTEL OGUZKENT ASHGABAD"
# 	args['article'] = Article.objects.get(article_category_id=2, article_language='en')
# 	args['minigals'] = ArticleImage.objects.filter(article_image_article_id=args['article'].id).order_by('id')[:6]
# 	return render_to_response('activity-en.html', args)
#
#
# def about_tm(request):
# 	args = {}
# 	args.update(csrf(request))
# 	args['lang_prefix'] = "tm"
# 	args['title'] = "Hoş geldiňiz | OGUZKENT OTELI AŞGABAT"
# 	args['article'] = Article.objects.get(article_category_id=3, article_language='tm')
# 	args['minigals'] = ArticleImage.objects.filter(article_image_article_id=args['article'].id).order_by('id')[:6]
# 	return render_to_response('activity-tm.html', args)
#
#
# #######################################################################
# ##########          ###########           ############         ########
# #######################################################################
#
#
# def accommodation_ru(request):
# 	args = {}
# 	args.update(csrf(request))
# 	args['lang_prefix'] = "ru"
# 	args['title'] = "Проживание | ОТЕЛЬ ОГУЗКЕНТ АШХАБАД"
# 	args['suites'] = Suite.objects.filter(suite_category_id=1).order_by('suite_price')
# 	args['article'] = Article.objects.get(article_category_id=4, article_language='ru')
# 	args['minigals'] = ArticleImage.objects.filter(article_image_article_id=args['article'].id).order_by('id')[:6]
# 	return render_to_response('accommodation-ru.html', args)
#
#
# def accommodation_en(request):
# 	args = {}
# 	args.update(csrf(request))
# 	args['lang_prefix'] = "en"
# 	args['title'] = "Accommodation | HOTEL OGUZKENT ASHGABAD"
# 	args['suites'] = Suite.objects.filter(suite_category_id=2).order_by('suite_price')
# 	args['article'] = Article.objects.get(article_category_id=5, article_language='en')
# 	args['minigals'] = ArticleImage.objects.filter(article_image_article_id=args['article'].id).order_by('id')[:6]
# 	return render_to_response('accommodation-en.html', args)
#
#
# def accommodation_tm(request):
# 	args = {}
# 	args.update(csrf(request))
# 	args['lang_prefix'] = "tm"
# 	args['title'] = "Ýaşamak | OGUZKENT OTELI AŞGABAT"
# 	args['suites'] = Suite.objects.filter(suite_category_id=3).order_by('suite_price')
# 	args['article'] = Article.objects.get(article_category_id=6, article_language='tm')
# 	args['minigals'] = ArticleImage.objects.filter(article_image_article_id=args['article'].id).order_by('id')[:6]
# 	return render_to_response('accommodation-tm.html', args)
#
#
# #######################################################################
# ##########          ###########           ############         ########
# #######################################################################
#
# def accommodation_suite_ru(request, suite_id):
# 	args = {}
# 	args.update(csrf(request))
# 	args['lang_prefix'] = "ru"
# 	args['title'] = Suite.objects.get(id=suite_id).suite_title
# 	args['today'] = datetime.date.today()
# 	args['tomorrow'] = datetime.date.today() + datetime.timedelta(days=1)
# 	args['suite'] = Suite.objects.get(id=suite_id)
# 	args['simsuites'] = Suite.objects.filter(suite_category_id=1).order_by('suite_price')
# 	args['services'] = SuiteService.objects.filter(suite_service_language="ru")
# 	args['prefers'] = SuitePreference.objects.filter(suite_preference_language="ru")
# 	args['minigals'] = SuiteImage.objects.filter(suite_image_suite_id=args['suite'].id).order_by('id')[:6]
# 	return render_to_response('accommodation-suite-ru.html', args)
#
#
# def accommodation_suite_en(request, suite_id):
# 	args = {}
# 	args.update(csrf(request))
# 	args['lang_prefix'] = "en"
# 	args['title'] = Suite.objects.get(id=suite_id).suite_title
# 	args['today'] = datetime.date.today()
# 	args['tomorrow'] = datetime.date.today() + datetime.timedelta(days=1)
# 	args['suite'] = Suite.objects.get(id=suite_id)
# 	args['simsuites'] = Suite.objects.filter(suite_category_id=2).order_by('suite_price')
# 	args['services'] = SuiteService.objects.filter(suite_service_language="en")
# 	args['prefers'] = SuitePreference.objects.filter(suite_preference_language="en")
# 	args['minigals'] = SuiteImage.objects.filter(suite_image_suite_id=args['suite'].id).order_by('id')[:6]
# 	return render_to_response('accommodation-suite-en.html', args)
#
#
# def accommodation_suite_tm(request, suite_id):
# 	args = {}
# 	args.update(csrf(request))
# 	args['lang_prefix'] = "tm"
# 	args['title'] = Suite.objects.get(id=suite_id).suite_title
# 	args['today'] = datetime.date.today()
# 	args['tomorrow'] = datetime.date.today() + datetime.timedelta(days=1)
# 	args['suite'] = Suite.objects.get(id=suite_id)
# 	args['simsuites'] = Suite.objects.filter(suite_category_id=3).order_by('suite_price')
# 	args['services'] = SuiteService.objects.filter(suite_service_language="tm")
# 	args['prefers'] = SuitePreference.objects.filter(suite_preference_language="tm")
# 	args['minigals'] = SuiteImage.objects.filter(suite_image_suite_id=args['suite'].id).order_by('id')[:6]
# 	return render_to_response('accommodation-suite-tm.html', args)
#
#
# #######################################################################
# ##########          ###########           ############         ########
# #######################################################################
#
# def activity_ru(request):
# 	args = {}
# 	args.update(csrf(request))
# 	args['lang_prefix'] = "ru"
# 	args['title'] = "Активный Отдых и Услуги | ОТЕЛЬ ОГУЗКЕНТ АШХАБАД"
# 	args['article'] = Article.objects.get(article_category_id=7, article_language='ru')
# 	args['minigals'] = ArticleImage.objects.filter(article_image_article_id=args['article'].id).order_by('id')[:6]
# 	return render_to_response('activity-ru.html', args)
#
#
# def activity_en(request):
# 	args = {}
# 	args.update(csrf(request))
# 	args['lang_prefix'] = "en"
# 	args['title'] = "Activities | HOTEL OGUZKENT ASHGABAD"
# 	args['article'] = Article.objects.get(article_category_id=8, article_language='en')
# 	args['minigals'] = ArticleImage.objects.filter(article_image_article_id=args['article'].id).order_by('id')[:6]
# 	return render_to_response('activity-en.html', args)
#
#
# def activity_tm(request):
# 	args = {}
# 	args.update(csrf(request))
# 	args['lang_prefix'] = "tm"
# 	args['title'] = "Işjeň dynç alyş we hyzmatlar | OGUZKENT OTELI AŞGABAT"
# 	args['article'] = Article.objects.get(article_category_id=9, article_language='tm')
# 	args['minigals'] = ArticleImage.objects.filter(article_image_article_id=args['article'].id).order_by('id')[:6]
# 	return render_to_response('activity-tm.html', args)
#
#
# #######################################################################
# ##########          ###########           ############         ########
# #######################################################################
#
# def complex_ru(request):
# 	args = {}
# 	args.update(csrf(request))
# 	args['lang_prefix'] = "ru"
# 	args['title'] = Article.objects.get(id=19).article_title
# 	args['article'] = Article.objects.get(id=19)
# 	args['minigals'] = ArticleImage.objects.filter(article_image_article_id=args['article'].id).order_by('id')[:6]
# 	return render_to_response('activity-ru.html', args)
#
#
# def residence_ru(request, article_id):
# 	args = {}
# 	args.update(csrf(request))
# 	args['lang_prefix'] = "ru"
# 	args['title'] = Article.objects.get(id=article_id).article_title
# 	args['article'] = Article.objects.get(id=article_id)
# 	args['simbars'] = Article.objects.filter(article_category_id=args['article'].article_category_id).order_by('id')[
# 	                  1:6]
# 	args['minigals'] = ArticleImage.objects.filter(article_image_article_id=args['article'].id).order_by('id')
# 	return render_to_response('restaurant-ru.html', args)
#
#
# def complex_en(request):
# 	args = {}
# 	args.update(csrf(request))
# 	args['lang_prefix'] = "en"
# 	args['title'] = Article.objects.get(id=57).article_title
# 	args['article'] = Article.objects.get(id=57)
# 	args['minigals'] = ArticleImage.objects.filter(article_image_article_id=args['article'].id).order_by('id')[:6]
# 	return render_to_response('activity-en.html', args)
#
#
# def residence_en(request, article_id):
# 	args = {}
# 	args.update(csrf(request))
# 	args['lang_prefix'] = "en"
# 	args['title'] = Article.objects.get(id=article_id).article_title
# 	args['article'] = Article.objects.get(id=article_id)
# 	args['simbars'] = Article.objects.filter(article_category_id=args['article'].article_category_id).order_by('id')[
# 	                  1:6]
# 	args['minigals'] = ArticleImage.objects.filter(article_image_article_id=args['article'].id).order_by('id')
# 	return render_to_response('restaurant-en.html', args)
#
#
# def complex_tm(request):
# 	args = {}
# 	args.update(csrf(request))
# 	args['lang_prefix'] = "tm"
# 	args['title'] = Article.objects.get(id=58).article_title
# 	args['article'] = Article.objects.get(id=58)
# 	args['minigals'] = ArticleImage.objects.filter(article_image_article_id=args['article'].id).order_by('id')[:6]
# 	return render_to_response('activity-tm.html', args)
#
#
# def residence_tm(request, article_id):
# 	args = {}
# 	args.update(csrf(request))
# 	args['lang_prefix'] = "tm"
# 	args['title'] = Article.objects.get(id=article_id).article_title
# 	args['article'] = Article.objects.get(id=article_id)
# 	args['simbars'] = Article.objects.filter(article_category_id=args['article'].article_category_id).order_by('id')[
# 	                  1:6]
# 	args['minigals'] = ArticleImage.objects.filter(article_image_article_id=args['article'].id).order_by('id')
# 	return render_to_response('restaurant-tm.html', args)
#
#
# #######################################################################
# ##########          ###########           ############         ########
# #######################################################################
#
# def restaurants_ru(request):
# 	args = {}
# 	args.update(csrf(request))
# 	args['lang_prefix'] = "ru"
# 	args['title'] = Article.objects.get(id=5).article_title
# 	args['article'] = Article.objects.get(id=5)
# 	args['simbars'] = Article.objects.filter(article_category_id=args['article'].article_category_id).order_by('id')[
# 	                  1:6]
# 	args['minigals'] = ArticleImage.objects.filter(article_image_article_id=args['article'].id).order_by('id')[:6]
# 	return render_to_response('restaurants-ru.html', args)
#
#
# def restaurants_en(request):
# 	args = {}
# 	args.update(csrf(request))
# 	args['lang_prefix'] = "en"
# 	args['title'] = Article.objects.get(id=29).article_title
# 	args['article'] = Article.objects.get(id=29)
# 	args['simbars'] = Article.objects.filter(article_category_id=args['article'].article_category_id).order_by('id')[
# 	                  1:6]
# 	args['minigals'] = ArticleImage.objects.filter(article_image_article_id=args['article'].id).order_by('id')[:6]
# 	return render_to_response('restaurants-en.html', args)
#
#
# def restaurants_tm(request):
# 	args = {}
# 	args.update(csrf(request))
# 	args['lang_prefix'] = "tm"
# 	args['title'] = Article.objects.get(id=30).article_title
# 	args['article'] = Article.objects.get(id=30)
# 	args['simbars'] = Article.objects.filter(article_category_id=args['article'].article_category_id).order_by('id')[
# 	                  1:6]
# 	args['minigals'] = ArticleImage.objects.filter(article_image_article_id=args['article'].id).order_by('id')[:6]
# 	return render_to_response('restaurants-tm.html', args)
#
#
# #######################################################################
# ##########          ###########           ############         ########
# #######################################################################
#
# def restaurant_ru(request, article_id):
# 	args = {}
# 	args.update(csrf(request))
# 	args['lang_prefix'] = "ru"
# 	args['title'] = Article.objects.get(id=article_id).article_title
# 	args['article'] = Article.objects.get(id=article_id)
# 	args['simbars'] = Article.objects.filter(article_category_id=args['article'].article_category_id).order_by('id')[
# 	                  1:6]
# 	args['minigals'] = ArticleImage.objects.filter(article_image_article_id=args['article'].id).order_by('id')
# 	return render_to_response('restaurant-ru.html', args)
#
#
# def restaurant_en(request, article_id):
# 	args = {}
# 	args.update(csrf(request))
# 	args['lang_prefix'] = "en"
# 	args['title'] = Article.objects.get(id=article_id).article_title
# 	args['article'] = Article.objects.get(id=article_id)
# 	args['simbars'] = Article.objects.filter(article_category_id=args['article'].article_category_id).order_by('id')[
# 	                  1:6]
# 	args['minigals'] = ArticleImage.objects.filter(article_image_article_id=args['article'].id).order_by('id')
# 	return render_to_response('restaurant-en.html', args)
#
#
# def restaurant_tm(request, article_id):
# 	args = {}
# 	args.update(csrf(request))
# 	args['lang_prefix'] = "tm"
# 	args['title'] = Article.objects.get(id=article_id).article_title
# 	args['article'] = Article.objects.get(id=article_id)
# 	args['simbars'] = Article.objects.filter(article_category_id=args['article'].article_category_id).order_by('id')[
# 	                  1:6]
# 	args['minigals'] = ArticleImage.objects.filter(article_image_article_id=args['article'].id).order_by('id')
# 	return render_to_response('restaurant-tm.html', args)
#
#
# #######################################################################
# ##########          ###########           ############         ########
# #######################################################################
#
# def spas_ru(request):
# 	args = {}
# 	args.update(csrf(request))
# 	args['lang_prefix'] = "ru"
# 	args['title'] = Article.objects.get(id=11).article_title
# 	args['article'] = Article.objects.get(id=11)
# 	args['simspas'] = Article.objects.filter(article_category_id=args['article'].article_category_id).order_by('id')[
# 	                  1:6]
# 	args['minigals'] = ArticleImage.objects.filter(article_image_article_id=args['article'].id).order_by('id')[:6]
# 	return render_to_response('spas-ru.html', args)
#
#
# def spas_en(request):
# 	args = {}
# 	args.update(csrf(request))
# 	args['lang_prefix'] = "en"
# 	args['title'] = Article.objects.get(id=41).article_title
# 	args['article'] = Article.objects.get(id=41)
# 	args['simspas'] = Article.objects.filter(article_category_id=args['article'].article_category_id).order_by('id')[
# 	                  1:6]
# 	args['minigals'] = ArticleImage.objects.filter(article_image_article_id=args['article'].id).order_by('id')[:6]
# 	return render_to_response('spas-en.html', args)
#
#
# def spas_tm(request):
# 	args = {}
# 	args.update(csrf(request))
# 	args['lang_prefix'] = "tm"
# 	args['title'] = Article.objects.get(id=42).article_title
# 	args['article'] = Article.objects.get(id=42)
# 	args['simspas'] = Article.objects.filter(article_category_id=args['article'].article_category_id).order_by('id')[
# 	                  1:6]
# 	args['minigals'] = ArticleImage.objects.filter(article_image_article_id=args['article'].id).order_by('id')[:6]
# 	return render_to_response('spas-tm.html', args)
#
#
# #######################################################################
# ##########          ###########           ############         ########
# #######################################################################
#
# def spa_ru(request, article_id):
# 	args = {}
# 	args.update(csrf(request))
# 	args['lang_prefix'] = "ru"
# 	args['title'] = Article.objects.get(id=article_id).article_title
# 	args['article'] = Article.objects.get(id=article_id)
# 	args['simspas'] = Article.objects.filter(article_category_id=args['article'].article_category_id).order_by('id')[
# 	                  1:6]
# 	args['minigals'] = ArticleImage.objects.filter(article_image_article_id=args['article'].id).order_by('id')[:6]
# 	return render_to_response('spa-ru.html', args)
#
#
# def spa_en(request, article_id):
# 	args = {}
# 	args.update(csrf(request))
# 	args['lang_prefix'] = "en"
# 	args['title'] = Article.objects.get(id=article_id).article_title
# 	args['article'] = Article.objects.get(id=article_id)
# 	args['simspas'] = Article.objects.filter(article_category_id=args['article'].article_category_id).order_by('id')[
# 	                  1:6]
# 	args['minigals'] = ArticleImage.objects.filter(article_image_article_id=args['article'].id).order_by('id')[:6]
# 	return render_to_response('spa-en.html', args)
#
#
# def spa_tm(request, article_id):
# 	args = {}
# 	args.update(csrf(request))
# 	args['lang_prefix'] = "tm"
# 	args['title'] = Article.objects.get(id=article_id).article_title
# 	args['article'] = Article.objects.get(id=article_id)
# 	args['simspas'] = Article.objects.filter(article_category_id=args['article'].article_category_id).order_by('id')[
# 	                  1:6]
# 	args['minigals'] = ArticleImage.objects.filter(article_image_article_id=args['article'].id).order_by('id')[:6]
# 	return render_to_response('spa-tm.html', args)
#
#
# #######################################################################
# ##########          ###########           ############         ########
# #######################################################################
#
# def contacts_ru(request):
# 	args = {}
# 	args.update(csrf(request))
# 	args['lang_prefix'] = "ru"
# 	args['today'] = datetime.date.today()
# 	args['tomorrow'] = datetime.date.today() + datetime.timedelta(days=1)
# 	args['title'] = "Обратная связь с отелем Огузкент"
# 	return render_to_response('contacts-ru.html', args)
#
#
# def contacts_en(request):
# 	args = {}
# 	args.update(csrf(request))
# 	args['lang_prefix'] = "en"
# 	args['today'] = datetime.date.today()
# 	args['tomorrow'] = datetime.date.today() + datetime.timedelta(days=1)
# 	args['title'] = "Contact with hotel Oguzkent"
# 	return render_to_response('contacts-en.html', args)
#
#
# def contacts_tm(request):
# 	args = {}
# 	args.update(csrf(request))
# 	args['lang_prefix'] = "tm"
# 	args['today'] = datetime.date.today()
# 	args['tomorrow'] = datetime.date.today() + datetime.timedelta(days=1)
# 	args['title'] = "Oguzkent oteli bilen habarlaşmak"
# 	return render_to_response('contacts-tm.html', args)
#
#
# #######################################################################
# ##########          ###########           ############         ########
# #######################################################################
#
# def sendmail_ru(request):
# 	args = {}
# 	args['lang_prefix'] = "ru"
# 	args['title'] = "Обратная связь с отелем Огузкент"
# 	name = request.POST.get('name', '')
# 	email = request.POST.get('email', '')
# 	subject = request.POST.get('subject', '')
# 	message = request.POST.get('message', '')
# 	args['message'] = "<p>" + name + "</p>" + "<p>e-mail address: " + email + "</p>" + "<p>" + message + "</p>"
# 	subject, from_email, to = subject, 'web@oguzkenthotel.com', 're1@oguzkenthotel.com'
# 	text_content = 'This is an important message.'
# 	html_content = args['message']
# 	msg = EmailMultiAlternatives(subject, text_content, from_email, [to])
# 	msg.attach_alternative(html_content, "text/html")
# 	msg.send(args)
# 	return render_to_response('mail-success-ru.html', args)
#
#
# def sendmail_en(request):
# 	args = {}
# 	args['lang_prefix'] = "en"
# 	args['title'] = "Contact with hotel Oguzkent"
# 	name = request.POST.get('name', '')
# 	email = request.POST.get('email', '')
# 	subject = request.POST.get('subject', '')
# 	message = request.POST.get('message', '')
# 	args['message'] = "<p>" + name + "</p>" + "<p>e-mail address: " + email + "</p>" + "<p>" + message + "</p>"
# 	subject, from_email, to = subject, 'web@oguzkenthotel.com', 're1@oguzkenthotel.com'
# 	text_content = 'This is an important message.'
# 	html_content = args['message']
# 	msg = EmailMultiAlternatives(subject, text_content, from_email, [to])
# 	msg.attach_alternative(html_content, "text/html")
# 	msg.send(args)
# 	return render_to_response('mail-success-en.html', args)
#
#
# def sendmail_tm(request):
# 	args = {}
# 	args['lang_prefix'] = "tm"
# 	args['title'] = "Oguzkent oteli bilen habarlaşmak"
# 	name = request.POST.get('name', '')
# 	email = request.POST.get('email', '')
# 	subject = request.POST.get('subject', '')
# 	message = request.POST.get('message', '')
# 	args['message'] = "<p>" + name + "</p>" + "<p>e-mail address: " + email + "</p>" + "<p>" + message + "</p>"
# 	subject, from_email, to = subject, 'web@oguzkenthotel.com', 're1@oguzkenthotel.com'
# 	text_content = 'This is an important message.'
# 	html_content = args['message']
# 	msg = EmailMultiAlternatives(subject, text_content, from_email, [to])
# 	msg.attach_alternative(html_content, "text/html")
# 	msg.send(args)
# 	return render_to_response('mail-success-tm.html', args)
