"""
WSGI config for dedupper_app project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/2.0/howto/deployment/wsgi/
"""

import os

from django.core.wsgi import get_wsgi_application
from whitenoise.django import DjangoWhiteNoise
import sys
from dedupper_app.settings import BASE_DIR


os.environ.setdefault("DJANGO_SETTINGS_MODULE", "dedupper_app.settings")

application = get_wsgi_application()

application = DjangoWhiteNoise(application)