from django.contrib import admin

from .models import Brand, Category, Product


class BrandAdminInline(admin.TabularInline):
    model = Brand
    fields = ["name"]
    extra = 0


class ProductAdminInline(admin.TabularInline):
    model = Product
<<<<<<< HEAD
    fileds = ["name", "models", "price", "is_enable"]
=======
    fileds = ["name", "models", "price"]
>>>>>>> bab6acbf7d414b29a63d2c53c5bf5a81c4d70e19
    extra = 0
    inlines = [BrandAdminInline]


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ["name"]
    inlines = [ProductAdminInline]
