"""
WSGI config for myJournal project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/2.2/howto/deployment/wsgi/
"""

import os

from django.core.wsgi import get_wsgi_application

import dotenv

dotenv.load_dotenv(os.path.join( os.path.dirname( (os.path.dirname(__file__)) ), '.env' ))

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'myJournal.settings')

application = get_wsgi_application()
