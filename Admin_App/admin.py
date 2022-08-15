from django.contrib import admin
from django.urls import path, include
from .models import category_model, subcategory_model, age_category_model, product_model

# Register your models here.
class category_Admin(admin.ModelAdmin):
    list_display  = ('name', 'description', 'image')
    list_filter   = ('name', 'description', 'image')
    search_fields = ('name', 'description', 'image')
    list_per_page = 25

admin.site.register(category_model, category_Admin)

class subcategory_Admin(admin.ModelAdmin):
    list_display  = ('name', 'description', 'category')
    list_filter   = ('name', 'category')
    search_fields = ('name',)
    list_per_page = 35

admin.site.register(subcategory_model, subcategory_Admin)

class age_category_Admin(admin.ModelAdmin):
    list_display  = ('age', 'description')
    list_filter   = ('age',)
    search_fields = ('age',)
    list_per_page = 25

admin.site.register(age_category_model, age_category_Admin)

class product_Admin(admin.ModelAdmin):
    list_display  = ('name', 'Brand','price', 'offer_price', 'category', 'subcategory', 'size', 'stock', 'available')
    list_filter   = ( 'size', 'category', 'subcategory', 'available')
    search_fields = ('name', 'description', 'price', 'size')
    list_per_page = 25

admin.site.register(product_model, product_Admin)
