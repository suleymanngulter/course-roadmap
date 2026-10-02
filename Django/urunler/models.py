"""
models.py  =  tablo.

Urun sınıfı  →  urunler_urun tablosu
Her satır bir ürün, her alan bir sütun.
"""

from django.db import models


class Urun(models.Model):
    ad = models.CharField("Ad", max_length=80)  #? kısa metin
    fiyat = models.DecimalField("Fiyat", max_digits=8, decimal_places=2)  #? para
    aciklama = models.TextField("Açıklama", blank=True)  #? blank=True: boş bırakılabilir
    olusturulma = models.DateTimeField("Oluşturulma", auto_now_add=True)  #? kayıt anı

    class Meta:
        verbose_name = "Ürün"
        verbose_name_plural = "Ürünler"
        ordering = ["ad"]  #? varsayılan sıra: ada göre

    def __str__(self):
        return self.ad  #? admin listesinde görünen ad
