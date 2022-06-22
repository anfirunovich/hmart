from django.contrib import admin

from cars.models import Car, Product


@admin.register(Car)
class CarAdmin(admin.ModelAdmin):
    list_display = ("name", "description",)


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ("type", "price", "car",)
