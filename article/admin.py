from django.contrib import admin

# Register your models here.
from .models import ArticleColumn

class ArticleColumnAdmin(admin.ModelAdmin):
    list_display=('column','user','created')
    list_filter=('column',)

admin.site.register(ArticleColumn,ArticleColumnAdmin)

