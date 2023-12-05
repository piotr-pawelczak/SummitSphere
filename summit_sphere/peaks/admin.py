from django.contrib import admin

from summit_sphere.commons.admin import ModelAdminNotCaseSensitiveSearch

from .models import Peak, Region


@admin.register(Peak)
class PeakAdmin(ModelAdminNotCaseSensitiveSearch):
    list_display = ["name", "region", "elevation", "country_code"]
    search_fields = ["name", "unicode_name"]
    list_filter = ["region", "country_code"]
    list_editable = ["region"]
    # raw_id_fields = ["region"]


@admin.register(Region)
class RegionAdmin(admin.ModelAdmin):
    list_display = ["pk", "name", "country_code"]
    search_fields = ["name"]
