from django.contrib import admin

from .models import Brand, Category, Product


class BrandAdminInline(admin.TabularInline):
    model = Brand
    fields = ["name"]
    extra = 0


class ProductAdminInline(admin.TabularInline):
    model = Product
    fileds = ["name", "models", "price"]
    extra = 0
    inlines = [BrandAdminInline]


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ["name"]
    inlines = [ProductAdminInline]
