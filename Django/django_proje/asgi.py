"""
asgi.py  =  asenkron yayın kapısı.

ASGI: WSGI'nin async hali. Kanal (Channels), WebSocket, SSE gibi
uzun yaşamlı bağlantılar burada bağlanır. Bu ders uygulaması
klasik istek/cevap kullandığı için asgi.py'yi şimdilik açmana gerek yok.
"""

import os

from django.core.asgi import get_asgi_application

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "django_proje.settings")

application = get_asgi_application()
