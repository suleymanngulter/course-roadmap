"""
urls.py (proje kökü)  =  sitenin ana yol haritası.

İstek gelir:  http://127.0.0.1:8000/urunler/
                 └── path ─────────┘
Django bu listedeki ilk eşleşen kuralı kullanır.

path("urunler/", include("urunler.urls"))
     └── önek           └── o modülün kendi urls.py'sine devret

Böylece her uygulama kendi adreslerini kendi urls.py'sinde tutar.
"""

from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    #? /admin/  →  Django yönetim paneli (superuser gerekir)
    path("admin/", admin.site.urls),
    #? 3 modül: kök, /urunler/, /iletisim/
    path("", include("anasayfa.urls")),
    path("urunler/", include("urunler.urls")),
    path("iletisim/", include("iletisim.urls")),
]
