from django.contrib import admin

# Register your models here.
from .models import Category, Product

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['id','name', 'slug']
    prepopulated_fields = {'slug': ('name',)} # 用一個字段來生成另一個字段 使用name生成slug 可以方便的生成slug

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ['id','name', 'slug', 'price', 'available', 'created', 'updated','image']
    list_filter = ['available', 'created', 'updated']
    list_editable = ['price', 'available', 'image']
    prepopulated_fields = {'slug': ('name',)}
