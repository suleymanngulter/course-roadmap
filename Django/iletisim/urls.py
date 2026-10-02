from django.urls import path

from . import views

app_name = "iletisim"

urlpatterns = [
    path("", views.form_view, name="form"),
    path("tesekkur/", views.tesekkur, name="tesekkur"),
]
