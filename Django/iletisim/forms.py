"""
forms.py  =  HTML formunun Python hali.

ModelForm model alanlarından input üretir.
is_valid()  kurallar tamam mı?
save()      Mesaj satırını yazar
"""

from django import forms

from .models import Mesaj


class MesajForm(forms.ModelForm):
    class Meta:
        model = Mesaj
        fields = ("isim", "eposta", "icerik")
        #? labels: input'un üstünde görünen yazı
        labels = {
            "isim": "Adın",
            "eposta": "E-posta",
            "icerik": "Mesajın",
        }
        #? help_text: kutunun altında kısa ipucu
        help_texts = {
            "eposta": "Geçerli bir adres yaz.",
        }
        widgets = {
            "icerik": forms.Textarea(attrs={"rows": 4, "placeholder": "Kısaca yaz..."}),
            "isim": forms.TextInput(attrs={"placeholder": "Ad soyad"}),
        }
