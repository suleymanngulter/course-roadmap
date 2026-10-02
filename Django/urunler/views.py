"""
Ürün listesi ve tek ürün sayfası.

Urun.objects.all()   tüm ürünler
get_object_or_404    yoksa 404 (boş sayfa yerine)
"""

from django.shortcuts import get_object_or_404, render

from .models import Urun

#? Tablo boşsa ilk açılışta 3 örnek. Admin'den de ekleyebilirsin.
ORNEKLER = [
    {"ad": "Defter", "fiyat": "45.00", "aciklama": "Kareli, 80 yaprak."},
    {"ad": "Kalem", "fiyat": "15.00", "aciklama": "Mavi tükenmez."},
    {"ad": "Silgi", "fiyat": "8.00", "aciklama": "Beyaz, küçük."},
]


def _ornek_doldur():
    #? exists(): en az bir kayıt var mı?
    if Urun.objects.exists():
        return
    for o in ORNEKLER:
        Urun.objects.create(**o)


def liste(request):
    _ornek_doldur()
    urunler = Urun.objects.all()
    return render(request, "urunler/liste.html", {"urunler": urunler})


def detay(request, pk):
    #? pk: URL'deki sayı. /urunler/2/  →  pk=2
    urun = get_object_or_404(Urun, pk=pk)
    return render(request, "urunler/detay.html", {"urun": urun})
