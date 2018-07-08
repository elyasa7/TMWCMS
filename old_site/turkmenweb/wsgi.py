"""
WSGI config for turkmenweb project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/1.9/howto/deployment/wsgi/
"""

import os

from django.core.wsgi import get_wsgi_application

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "turkmenweb.settings")

application = get_wsgi_application()

import mysite.monitor
mysite.monitor.start(interval=1.0)