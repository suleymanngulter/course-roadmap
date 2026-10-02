"""
apps.py  =  bu uygulamanın kimlik kartı.

INSTALLED_APPS'e 'anasayfa' yazınca Django bu AppConfig'i okur.
name: Python paket adı (klasör adı ile aynı olmalı).
verbose_name: admin panelinde görünen Türkçe ad.
"""

from django.apps import AppConfig


class AnasayfaConfig(AppConfig):
    default_auto_field = "django.db.models.BigAutoField"
    name = "anasayfa"
    verbose_name = "Anasayfa"
