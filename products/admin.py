from django.contrib import admin
from products.models import ProductsModel, CategoryModel

@admin.register(CategoryModel)
class CategoryModelAdmin(admin.ModelAdmin):
    list_display = ['name', 'created_at']
    list_filter = ['created_at', 'updated_at']
    search_fields = ['name']


@admin.register(ProductsModel)
class ProductsModelAdmin(admin.ModelAdmin):
    list_display = ['name', 'price', 'created_at']
    search_fields = ['name', 'description']
    list_filter = ['created_at', 'updated_at']