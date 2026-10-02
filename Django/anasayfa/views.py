"""
views.py  =  sayfayı hazırlayan fonksiyon.

Kısa akış:
    urls.py  →  bu fonksiyon  →  HTML şablon
"""

from django.shortcuts import render


def index(request):
    #? request: tarayıcıdan gelen istek (adres, form verisi, ...)
    #? baglam: şablona gönderilen sözlük. Anahtar adı HTML'de {{ baslik }} olur.
    baglam = {
        "baslik": "Django'ya hoş geldin",
        "ozet": "Bu küçük site 3 parçadan oluşur: anasayfa, ürünler, iletişim.",
        "kartlar": [
            {
                "baslik": "Anasayfa",
                "yazi": "Karşılama ve hakkımızda. Model yok, sadece HTML.",
                "adres": "/",
            },
            {
                "baslik": "Ürünler",
                "yazi": "Veritabanından liste ve detay sayfası.",
                "adres": "/urunler/",
            },
            {
                "baslik": "İletişim",
                "yazi": "Form doldurulur, mesaj kaydedilir.",
                "adres": "/iletisim/",
            },
        ],
    }
    return render(request, "anasayfa/index.html", baglam)


def hakkimizda(request):
    #? Dosya adları ders için: hangisi ne işe yarar.
    dosyalar = [
        {"ad": "models.py", "ne": "Tablo (veritabanı)."},
        {"ad": "views.py", "ne": "Sayfanın mantığı."},
        {"ad": "urls.py", "ne": "Hangi adres hangi view."},
        {"ad": "templates/", "ne": "HTML dosyaları."},
        {"ad": "admin.py", "ne": "/admin panelinde ne görünsün."},
        {"ad": "forms.py", "ne": "HTML formu (iletişim modülünde)."},
    ]
    return render(request, "anasayfa/hakkimizda.html", {"dosyalar": dosyalar})
