from django.contrib import admin

from .models import Peak


@admin.register(Peak)
class PeakAdmin(admin.ModelAdmin):
    list_display = ["name", "elevation", "country_code"]
    search_fields = ["name", "unicode_name"]
