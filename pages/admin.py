from django.contrib import admin

from pages.models import PicturesModel, ScrollModel


@admin.register(PicturesModel)
class PicturesModelAdmin(admin.ModelAdmin):
    search_fields = ['name']
    list_display = ['name', 'created_at', 'image']


@admin.register(ScrollModel)
class PicturesModelAdmin(admin.ModelAdmin):
    search_fields = ['name', 'discount']
    list_display = ['name', 'discount' ]
