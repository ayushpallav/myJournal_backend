import os


class CelerySettingsMixin:
	CELERY_TIMEZONE = 'UTC'

	CELERY_BEAT_SCHEDULE = {}

	CELERY_ACCEPT_CONTENT = ['application/json']

	CELERY_TASK_SERIALIZER = 'json'
