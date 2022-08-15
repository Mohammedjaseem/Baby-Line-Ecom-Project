from django.contrib import admin
from django.urls import path, include
from .models import profileregister_model

# Register your models here.

class profileregister_modelAdmin(admin.ModelAdmin):
    list_display  = ('user_id', 'name', 'dob', 'pincode', 'address')
    list_filter   = ('user_id', 'name', 'dob', 'pincode', 'address')
    search_fields = ('user_id', 'name', 'dob', 'pincode', 'address')
    list_per_page = 25

admin.site.register(profileregister_model, profileregister_modelAdmin)
