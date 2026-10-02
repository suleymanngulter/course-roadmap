#!/usr/bin/env python
"""
manage.py  =  Django projesinin kumanda kolu.

Bu dosyayı sen yazmazsın; `django-admin startproject` üretir.
Görevi: Django'ya "ayarların django_proje/settings.py içinde" demek
ve komutları (runserver, migrate, createsuperuser ...) çalıştırmak.

Sık kullanılan komutlar (Django klasörünün içinde çalıştır):

    python manage.py runserver          # geliştirme sunucusu (http://127.0.0.1:8000)
    python manage.py migrate            # modelleri veritabanına işle
    python manage.py makemigrations     # model değişikliklerinden göç dosyası üret
    python manage.py createsuperuser    # /admin paneli için kullanıcı
    python manage.py startapp yeniapp   # yeni bir modül (uygulama) oluştur
"""

import os
import sys


def main():
    #? Django, ayar dosyasını ortam değişkeninden okur.
    #? Nokta yolu: paket.modül  →  django_proje/settings.py
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "django_proje.settings")
    try:
        from django.core.management import execute_from_command_line
    except ImportError as exc:
        raise ImportError(
            "Django import edilemedi. Sanal ortam açık mı? "
            "pip install -r requirements.txt çalıştırıldı mı?"
        ) from exc
    execute_from_command_line(sys.argv)


if __name__ == "__main__":
    main()
