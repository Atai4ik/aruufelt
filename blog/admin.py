from django.contrib import admin
from mptt.admin import MPTTModelAdmin

from . import models


admin.site.register(models.Category, MPTTModelAdmin)
admin.site.register(models.Post)
admin.site.register(models.Comment)
admin.site.register(models.Tag)