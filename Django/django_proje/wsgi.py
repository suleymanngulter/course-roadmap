"""
wsgi.py  =  klasik (senkron) yayın kapısı.

WSGI: Web sunucusu (gunicorn, Apache) ile Django arasında anlaşma.
Geliştirmede runserver bunu kullanır. Canlıda da çoğu site WSGI ile kalkar.

asgi.py ise WebSocket / async işler içindir. Temel sitede wsgi yeter.
"""

import os

from django.core.wsgi import get_wsgi_application

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "django_proje.settings")

application = get_wsgi_application()
