"""
Ziyaretçi mesajı. Form kaydedilince buraya bir satır eklenir.
"""

from django.db import models


class Mesaj(models.Model):
    isim = models.CharField("İsim", max_length=80)
    eposta = models.EmailField("E-posta")  #? e-posta formatını kontrol eder
    icerik = models.TextField("Mesaj")
    tarih = models.DateTimeField("Tarih", auto_now_add=True)

    class Meta:
        verbose_name = "Mesaj"
        verbose_name_plural = "Mesajlar"
        ordering = ["-tarih"]  #? - = yeniden eskiye

    def __str__(self):
        return f"{self.isim} — {self.tarih:%Y-%m-%d}"
