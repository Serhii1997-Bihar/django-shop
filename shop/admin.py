from django.contrib import admin
from .models import *

class ProductAdmin(admin.ModelAdmin):
    fields = ['name', 'category', 'country', 'brand', 'image', 'video', 'price', 'about', 'size', 'sex']
    search_fields = ['name']
    list_display = ['name', 'category', 'country', 'sex', 'date']
admin.site.register(ProductsModel, ProductAdmin)


class CategoryAdmin(admin.ModelAdmin):
    fields = ['name']
admin.site.register(CategoryModel, CategoryAdmin)

class CountryAdmin(admin.ModelAdmin):
    fields = ['name']
admin.site.register(CountryModel, CountryAdmin)

class BrandAdmin(admin.ModelAdmin):
    fields = ['name']
admin.site.register(BrandModel, BrandAdmin)

class SizeAdmin(admin.ModelAdmin):
    fields = ['size']
admin.site.register(SizeModel, SizeAdmin)

class SexAdmin(admin.ModelAdmin):
    fields = ['sex']
admin.site.register(SexModel, SexAdmin)

class AdminPanel(admin.ModelAdmin):
    fields = ['name', 'achievement', 'experience', 'skills', 'image', 'bio']
    search_fields = ['name']
admin.site.register(AdministrationModel, AdminPanel)







#Serhii_Bih Hardwell1997