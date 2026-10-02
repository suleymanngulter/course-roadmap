"""
settings.py  =  projenin merkezi ayar dosyası.

Django mimarisi (kısa):

    tarayıcı
       │  istek (URL)
       ▼
    urls.py          hangi view çalışacak?
       │
       ▼
    views.py         iş mantığı (veri al, işle, cevap ver)
       │
       ▼  gerekirse
    models.py        veritabanı tabloları
    templates/       HTML iskeleti
       │
       ▼
    tarayıcıya HTML / JSON döner

Bu dosyada "nasıl bağlanacaklar" kararları durur:
hangi uygulamalar yüklü, veritabanı nerede, şablonlar nerede...
"""

from pathlib import Path

#? BASE_DIR: manage.py'nin bulunduğu klasör (Django/).
#? Path(__file__) = bu settings.py dosyası
#? .resolve().parent.parent = iki klasör yukarı = proje kökü
BASE_DIR = Path(__file__).resolve().parent.parent


# ------------------------------------------------------------
#  GÜVENLİK (ders ortamı — gerçek sitede SECRET_KEY gizlenir)
# ------------------------------------------------------------

#? SECRET_KEY: oturum çerezi, CSRF token gibi imzalar için kullanılır.
#? Ders için sabit yazıyoruz. Canlıya alırken ortam değişkenine taşı.
SECRET_KEY = "ders-ortami-icin-ornek-anahtar-canlida-kullanma"

#? DEBUG=True: hata sayfasında ayrıntı görünür. Sadece kendi bilgisayarında.
#? Canlı sitede False olmalı.
DEBUG = True

#? Hangi domainlerden istek kabul edilsin?
#? DEBUG=True iken boş liste çoğu durumda yeter (localhost).
ALLOWED_HOSTS = []


# ------------------------------------------------------------
#  UYGULAMALAR (modüller)
# ------------------------------------------------------------
#? Django "monolit tek dosya" değil; işleri app'lere böler.
#? Bu derste 3 modül var:
#?   anasayfa  →  karşılama sayfaları
#?   urunler   →  model + liste/detay
#?   iletisim  →  form + mesaj kaydı

INSTALLED_APPS = [
    # Django'nun kendi paneli ve kimlik sistemi
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    # bizim 3 modülümüz
    "anasayfa",
    "urunler",
    "iletisim",
]


# ------------------------------------------------------------
#  MIDDLEWARE
# ------------------------------------------------------------
#? İstek view'a gitmeden ÖNCE ve cevap dönerken SONRA çalışan katmanlar.
#? Sıra önemlidir. Güvenlik, oturum, mesajlar burada bağlanır.

MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",  # form sahteciliğine karşı
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
]


#? ROOT_URLCONF: ana URL haritası. Trafik ilk buradan dağılır.
ROOT_URLCONF = "django_proje.urls"


# ------------------------------------------------------------
#  ŞABLONLAR (HTML)
# ------------------------------------------------------------
#? Django HTML'i Python'a gömmez; templates klasöründeki dosyaları doldurur.
#? DIRS: proje genelinde ortak şablonlar (base.html burada).
#? APP_DIRS=True: her uygulamanın kendi templates/ klasörüne de bakar.

TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [BASE_DIR / "templates"],
        "APP_DIRS": True,
        "OPTIONS": {
            "context_processors": [
                #? context_processor: her şablona otomatik eklenen değişkenler
                "django.template.context_processors.request",
                "django.contrib.auth.context_processors.auth",
                "django.contrib.messages.context_processors.messages",
            ],
        },
    },
]


#? WSGI: klasik web sunucusunun Django'yu çağırma kapısı (asgi.py ise async).
WSGI_APPLICATION = "django_proje.wsgi.application"


# ------------------------------------------------------------
#  VERİTABANI
# ------------------------------------------------------------
#? SQLite = tek dosyalık veritabanı. Kurulum yok, ders için ideal.
#? Dosya: Django/db.sqlite3  (migrate komutu oluşturur)

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.sqlite3",
        "NAME": BASE_DIR / "db.sqlite3",
    }
}


# ------------------------------------------------------------
#  PAROLA KURALLARI (admin kullanıcısı için)
# ------------------------------------------------------------

AUTH_PASSWORD_VALIDATORS = [
    {"NAME": "django.contrib.auth.password_validation.UserAttributeSimilarityValidator"},
    {"NAME": "django.contrib.auth.password_validation.MinimumLengthValidator"},
    {"NAME": "django.contrib.auth.password_validation.CommonPasswordValidator"},
    {"NAME": "django.contrib.auth.password_validation.NumericPasswordValidator"},
]


# ------------------------------------------------------------
#  DİL VE SAAT
# ------------------------------------------------------------

LANGUAGE_CODE = "tr-tr"
TIME_ZONE = "Europe/Istanbul"
USE_I18N = True
USE_TZ = True


#? STATIC_URL: CSS / JS / görseller tarayıcıda hangi yoldan istenir.
#? Dosyaları sonra static/ klasörüne koyarsın; {% static %} ile bağlarsın.
STATIC_URL = "static/"

#? Yeni modellerde otomatik birincil anahtar tipi.
DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"
