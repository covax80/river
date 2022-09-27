from django.contrib import admin

# Register your models here.
from .models import Category, Product #, CategoryLink

class ProductAdmin(admin.ModelAdmin):
    list_display = ('id', 'show_categories_admin', 'name', 'price', 'deleted', 'published')
    list_filter = ('deleted', 'published')
    search_fields = ('name',)
    list_editable = ('name', 'price', 'deleted', 'published',)



admin.site.register(Category)
admin.site.register(Product, ProductAdmin)
# admin.site.register(Product)
# admin.site.register(CategoryLink)

