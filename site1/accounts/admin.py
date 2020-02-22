from django.contrib import admin
from .models import uploader
from import_export.admin import ImportExportModelAdmin
from django.db import models

class uploaderAdmin(admin.ModelAdmin):
    fieldsets = [
        ("Title", {'fields': ["title"]}),
        ("Content", {"fields": ["document"]})
    ]

admin.site.register(uploader,uploaderAdmin)