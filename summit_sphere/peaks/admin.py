from django.contrib import admin

from .models import Peak, Region


@admin.register(Peak)
class PeakAdmin(admin.ModelAdmin):
    list_display = ["name", "region", "elevation", "country_code"]
    search_fields = ["name", "unicode_name"]
    list_filter = ["region", "country_code"]
    list_editable = ["region"]


@admin.register(Region)
class RegionAdmin(admin.ModelAdmin):
    list_display = ["pk", "name", "country_code"]
    search_fields = ["name"]
