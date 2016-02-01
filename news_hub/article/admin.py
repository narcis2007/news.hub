from django.contrib import admin
from models import RawArticle
# Register your models here.


class RawArticleAdmin(admin.ModelAdmin):
    list_filter = ['toBeEdited','publish']

admin.site.register(RawArticle, RawArticleAdmin)