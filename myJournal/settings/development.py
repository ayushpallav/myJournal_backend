import os

from . import commons


class Settings(commons.Settings):

    DEBUG = True
    ENVIRONMENT_CODE = os.getenv('ENVIRONMENT_CODE', 'dev')
    ALLOWED_HOSTS = ['*']
