from django.contrib import admin
from megamenu.models import Menu

# Register your models here.


class MenuAdmin(admin.ModelAdmin):
	fields = ['menu_title', 'menu_description', 'menu_type', 'menu_subitem', 'menu_link', 'menu_language', 'menu_position']
	list_display = ['menu_title', 'menu_type', 'menu_language', 'menu_position']
	list_filter = ['menu_type', 'menu_language']


admin.site.register(Menu, MenuAdmin)