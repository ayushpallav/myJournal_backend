from __future__ import absolute_import, unicode_literals
import os

from celery import Celery
import dotenv

# set the default Django settings module for the 'celery' program.
os.environ.setdefault(
    'DJANGO_SETTINGS_MODULE',
    'myJournal.settings.development'
)
os.environ.setdefault('DJANGO_CONFIGURATION', 'Settings')


import configurations
configurations.setup()

from django.conf import settings


app = Celery('myJournal')

# Using a string here means the worker will not have to
# pickle the object when using Windows.
app.config_from_object('django.conf:settings', namespace='CELERY')

app.autodiscover_tasks()
