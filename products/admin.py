from django.contrib import admin

from .models import Product


class ProductAdmin(admin.ModelAdmin):
    list_display = ('title', 'slug', 'author', 'price', 'stock', 'available', 'created_at', 'updated_at')
    list_filter = ('available', 'author', 'created_at')
    list_editable = ('price', 'stock', 'available')
    prepopulated_fields = {'slug': ('title',)}


admin.site.register(Product, ProductAdmin)