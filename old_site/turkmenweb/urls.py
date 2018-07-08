"""oguzkent URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.9/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import patterns, include, url
from django.contrib import admin, sitemaps
from filebrowser.sites import site


urlpatterns = [
    url(r'^admin_tools/', include('admin_tools.urls')),
    url(r'^admin/', admin.site.urls),
    url(r'^$', 'article.views.homepage'),
    url(r'^development/$', 'article.views.development'),
    url(r'^ssl/$', 'article.views.ssl'),
    url(r'^avast/$', 'article.views.avast'),
    url(r'^blog/$', 'article.views.blogs'),
    url(r'^support/$', 'article.views.contact'),
    url(r'^(?P<menu>\w+)/(?P<article_id>[0-9]+)/$', 'article.views.single_article'),
    #url(r'^ssl/(?P<article_id>[0-9]+)/$', 'article.views.single_article'),
    #url(r'^sitemap.xml$', 'django.contrib.sitemaps.views.sitemap', {'sitemaps': sitemaps}),
    #handler404 = 'article.views.not_found'
]