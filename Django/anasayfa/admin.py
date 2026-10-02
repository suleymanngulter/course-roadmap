"""
admin.py  =  /admin panelinde hangi modeller listelensin?

Anasayfa modülünde veritabanı modeli yok.
Bu dosya yine durur; Django startapp her app'te bunu üretir.
Bir model eklediğinde:  admin.site.register(ModelinAdi)
"""

from django.contrib import admin  # noqa: F401  — ders için içe aktarım örneği
