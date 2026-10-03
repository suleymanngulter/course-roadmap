# Django ders projesi

Küçük bir site: anasayfa, ürün listesi, iletişim formu. Veritabanı SQLite (`db.sqlite3`). Dil: `tr-tr`.

## Çalıştırma

`manage.py` olan bu klasörde:

```bash
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
python manage.py migrate
python manage.py runserver
```

Tarayıcı: http://127.0.0.1:8000/

Durdurmak için `Ctrl+C`. Sanal ortam zaten varsa ilk iki satırı atlayıp `source .venv/bin/activate` yeter.

## Sayfalar

| Adres | Uygulama | Ne |
| --- | --- | --- |
| `/` | anasayfa | Karşılama |
| `/hakkimizda/` | anasayfa | Hakkımızda |
| `/urunler/` | urunler | Liste |
| `/urunler/<id>/` | urunler | Detay |
| `/iletisim/` | iletisim | Form |
| `/iletisim/tesekkur/` | iletisim | Teşekkür |
| `/admin/` | Django | Yönetim paneli |

## Klasörler

```
Django/
  manage.py           komutlar (runserver, migrate, ...)
  django_proje/       ayarlar + ana urls.py
  anasayfa/           karşılama sayfaları
  urunler/            model + liste/detay
  iletisim/           form + mesaj kaydı
  templates/          ortak HTML (base.html)
  requirements.txt    Django 5.2
```

İstek yolu: tarayıcı → `django_proje/urls.py` → uygulamanın `urls.py` → `views.py` → şablon.

## Admin

```bash
python manage.py createsuperuser
```

Sonra http://127.0.0.1:8000/admin/

## Sık komutlar

```bash
python manage.py makemigrations   # model değişince göç üret
python manage.py migrate          # göçü veritabanına işle
python manage.py runserver        # geliştirme sunucusu
```
