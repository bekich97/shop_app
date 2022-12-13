from django.contrib import admin
from shop.models import Product


class ProductAdmin(admin.ModelAdmin):
    exclude = ['webp_image']

    class Meta:
        model = Product


admin.site.register(Product, ProductAdmin)