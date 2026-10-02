"""
urls.py (uygulama)  =  bu modüle ait yollar.

Proje urls.py  path("", include("anasayfa.urls")) dediği için:

    ""           +  ""            →  /
    ""           +  "hakkimizda/" →  /hakkimizda/

app_name: şablonda {% url 'anasayfa:index' %} diye çağırmak için.
"""

from django.urls import path

from . import views

app_name = "anasayfa"

urlpatterns = [
    path("", views.index, name="index"),
    path("hakkimizda/", views.hakkimizda, name="hakkimizda"),
]
