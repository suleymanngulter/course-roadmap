from django.urls import path

from . import views

app_name = "urunler"

urlpatterns = [
    path("", views.liste, name="liste"),
    #? <int:pk>  URL'deki sayıyı view'a pk diye gönderir
    #? örnek: /urunler/3/  →  detay(request, pk=3)
    path("<int:pk>/", views.detay, name="detay"),
]
