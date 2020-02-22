from django.contrib import admin
from .models import Intro
from tinymce.widgets import TinyMCE
from django.db import models


class IntroAdmin(admin.ModelAdmin):
    formfield_overrides = {
        models.TextField: {'widget': TinyMCE()},
        }

# Register your models here.
admin.site.register(Intro,IntroAdmin)