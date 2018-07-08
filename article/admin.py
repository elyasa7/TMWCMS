from django.contrib import admin
from article.models import Article, ArticleImage, ArticleCategory

# Register your models here.

def duplicate_event(modeladmin, request, queryset):
    for object in queryset:
        object.id = None
        object.save()
duplicate_event.short_description = "Duplicate selected record"
    
class ArticleInline(admin.StackedInline):
	model = ArticleImage
	extra = 1

class ArticleAdmin(admin.ModelAdmin):
	fields = ['article_title', 'article_intro', 'article_text', 'article_language', 'article_category', 'article_date', 'article_image_intro', 'article_image_full', 'article_author']
	list_display = ['article_title', 'article_date', 'article_category']
	list_filter = ['article_language', 'article_date', 'article_category']
	inlines = [ArticleInline];
	save_as = True;

class ArticleCategoryAdmin(admin.ModelAdmin):
	fields = ['name', 'article_category_language']
	list_filter = ['article_category_language']
	list_display = ['name', 'article_category_language' ]


admin.site.register(Article, ArticleAdmin)
admin.site.register(ArticleCategory, ArticleCategoryAdmin)