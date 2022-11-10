from django.contrib import admin
from .models import Category, Product, City,ads

# Register your models here.
@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug']
    prepopulated_fields = {'slug': ('name',)}
@admin.register(City)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug']
    prepopulated_fields = {'slug': ('name',)}
@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
  list_display = ['id','category','city','name', 'slug', 'price', 'available', 'created', 'updated']
  list_filter = ['available', 'created', 'updated']
  list_editable = ['price', 'available']
  prepopulated_fields = {'slug':('name',)}
  # search_fields = []
  raw_id_fields = ('category',)


admin.site.register(ads)


