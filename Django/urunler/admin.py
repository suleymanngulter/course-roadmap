"""
admin.py  =  modeli panele bağla.

@admin.register(Urun)  yerine  admin.site.register(Urun) de yazılabilir.
list_display: tabloda hangi sütunlar görünsün.
"""

from django.contrib import admin

from .models import Urun


@admin.register(Urun)
class UrunAdmin(admin.ModelAdmin):
    list_display = ("ad", "fiyat", "olusturulma")
    search_fields = ("ad",)
