# -*- coding:utf-8 -*-

from django.shortcuts import render, render_to_response, redirect
from django.http.response import HttpResponse
from django.http import HttpResponseRedirect
from django.template.loader import get_template
from django.template import Context
from django.template import RequestContext
from article.models import Article, ArticleCategory, ArticleImage
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

def homepage_ru(request):
    args = {}
    args.update(csrf(request))
    args['lang_prefix'] = "ru"
    #args['title'] = "Отель Огузкент Ашхабад"
    args['title'] = "ОТЕЛЬ ОГУЗКЕНТ АШХАБАД"
    args['today'] = datetime.date.today()
    args['tomorrow'] = datetime.date.today() + datetime.timedelta(days=1)
    args['article'] = Article.objects.get(article_category_id=1, article_language='ru')
    args['minigals'] = ArticleImage.objects.filter(article_image_article_id=args['article'].id).order_by('id')[:6]
    args['suites'] = Suite.objects.filter(suite_category_id=1)
    return render_to_response('homepage-ru.html', args)