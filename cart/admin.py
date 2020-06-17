from django.contrib import admin
from .models import Items

@admin.register(Items)
class OrderAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'product', 'price', 'quantity', 'total', 'created']
    list_filter = ['name']
