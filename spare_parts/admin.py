from django.contrib import admin

from spare_parts.models import Spare


@admin.register(Spare)
class SpareAdmin(admin.ModelAdmin):
    list_display = ("name", "type", "price", "description",)


