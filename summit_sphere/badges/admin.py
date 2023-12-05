from django.contrib import admin

from .models import Badge


@admin.register(Badge)
class BadgeAdmin(admin.ModelAdmin):
    list_display = ["pk", "name", "source"]
    search_fields = ["name"]
    filter_horizontal = ["peaks"]
