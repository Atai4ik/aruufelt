from django.contrib import admin
from mptt.admin import MPTTModelAdmin

from . import models


@admin.register(models.Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ['title', 'category', 'author', 'created_at', 'views', 'id']


admin.site.register(models.Category, MPTTModelAdmin)
admin.site.register(models.Comment)
admin.site.register(models.Tag)
