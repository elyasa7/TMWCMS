# -*- coding:utf-8 -*-

"""TURKMENWEB URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
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

from django.conf.urls import include, url
from django.contrib import admin, sitemaps
from mega_admin import views as mega_admin_views
from extension import views as extension_views
from module import views as module_views

# from filebrowser.sites import site


urlpatterns = [
	#    url(r'^admin_tools/', include('admin_tools.urls')),
	url(r'^admin/', admin.site.urls),
#	url(r'^$', 'mega_admin.views.homepage'),

	url(r'^$', mega_admin_views.homepage),
	url(r'^demo/$', mega_admin_views.homepage_demo),

	url(r'^mega-admin/$', mega_admin_views.mega_home),

	# url(r'^development/$', 'article.views.development'),
	# url(r'^ssl/$', 'article.views.ssl'),
	# url(r'^avast/$', 'article.views.avast'),
	# url(r'^blog/$', 'article.views.blogs'),
	# url(r'^support/$', 'article.views.contact'),
	# url(r'^(?P<menu>\w+)/(?P<article_id>[0-9]+)/$', 'article.views.single_article'),

	url(r'^mega-admin/add-menu-category/$', mega_admin_views.add_menu_category),
	url(r'^mega-admin/add-menu-type/$', mega_admin_views.add_menu_type),
	url(r'^mega-admin/add-menu/$', mega_admin_views.add_menu),
	url(r'^mega-admin/add-menu-item/$', mega_admin_views.add_menu_item),
	url(r'^mega-admin/menus/$', mega_admin_views.menu_manager),

	url(r'^mega-admin/menu-items/$', mega_admin_views.menu_items),
	url(r'^mega-admin/menu-items/(\d+)/$', mega_admin_views.menu_items),
	url(r'^mega-admin/menu-items/save-menu-item/$', mega_admin_views.save_menu_item),
	url(r'^mega-admin/menu-items/change-item-state/$', mega_admin_views.change_menu_item_state),

	url(r'^mega-admin/languages/$', mega_admin_views.menu_languages),
	url(r'^mega-admin/languages-config/$', mega_admin_views.menu_languages_config),
	url(r'^mega-admin/add-language/$', mega_admin_views.add_language),
	url(r'^mega-admin/change-language-default/$', mega_admin_views.change_language_default),
	url(r'^mega-admin/change-language-delete/$', mega_admin_views.change_language_delete),
	url(r'^mega-admin/change-language-state/$', mega_admin_views.change_language_state),
	url(r'^mega-admin/change-language-configuration/$', mega_admin_views.change_language_configuration),

	url(r'^mega-admin/content/category-manager/$', extension_views.category_manager),
	url(r'^mega-admin/content/category-manager/(\d+)/$', extension_views.category_manager),
	url(r'^mega-admin/content/add-category/$', extension_views.add_category),
	url(r'^mega-admin/content/save-category/$', extension_views.save_category),
	url(r'^mega-admin/content/change-category-state/$', extension_views.change_article_category_state),

	url(r'^mega-admin/content/article-manager/$', extension_views.article_manager),
	url(r'^mega-admin/content/article-manager/(\d+)/$', extension_views.article_manager),
	url(r'^mega-admin/content/add-article/$', extension_views.add_article),
	url(r'^mega-admin/content/save-article/$', extension_views.save_article),
	url(r'^mega-admin/content/change-article-state/$', extension_views.change_article_state),

	url(r'^mega-admin/module/module-manager/$', module_views.module_manager),
	url(r'^mega-admin/module/module-manager/(\d+)/$', module_views.module_manager),
	url(r'^mega-admin/module/select-module-type/$', module_views.select_module),
	url(r'^mega-admin/module/add-module/$', module_views.add_module),
	url(r'^mega-admin/module/save-module/$', module_views.save_module),

	url(r'^content/article/(?P<article_alias>[\w\-]+)/$', extension_views.single_article),
	url(r'^content/blog/(?P<category_alias>[\w\-]+)/$', extension_views.category_blog),
	url(r'^content/blog/(?P<category_alias>[\w\-]+)/(\d+)/$', extension_views.category_blog),
	url(r'^content/blog/(?P<category_alias>[\w\-]+)/(?P<article_alias>[\w\-]+)/$', extension_views.category_blog_article),

	# url(r'^ssl/(?P<article_id>[0-9]+)/$', 'article.views.single_article'),
	# url(r'^sitemap.xml$', 'django.contrib.sitemaps.views.sitemap', {'sitemaps': sitemaps}),
	# handler404 = 'article.views.not_found'
]
