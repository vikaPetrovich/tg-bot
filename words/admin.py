from django.contrib import admin

from . import models

class WordAdmin(admin.ModelAdmin):
    list_display = ['pk', 'text']
    list_editable = ['text']

admin.site.register(models.Words, WordAdmin)