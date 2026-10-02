from django.contrib import admin

from .models import Mesaj


@admin.register(Mesaj)
class MesajAdmin(admin.ModelAdmin):
    list_display = ("isim", "eposta", "tarih")
    readonly_fields = ("tarih",)
