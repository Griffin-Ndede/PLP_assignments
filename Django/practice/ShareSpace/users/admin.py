from django.contrib import admin
from .models import User, Product

# Register your models here.

class MemberAdmin(admin.ModelAdmin):
    list_display = ("firstname", "lastname", "joined_date")

admin.site.register(User, MemberAdmin)

class ProductAdmin(admin.ModelAdmin):
    list_display = ("name", "description" , "date_added")

admin.site.register(Product, ProductAdmin)
