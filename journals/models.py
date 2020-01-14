"""
Each profile has a unique journal with jourrnal_id assigned to it
Each journal can have multiple entries, hence a one-to-many field from journal to entries
"""
from django.db import models
from django.contrib.auth.models import User

from django.contrib.postgres.fields import JSONField

from django.conf import settings


class Profile(models.Model):
    """
    Extends user model of django.auth
    stores further information needed for a user
    """
    user = models.OneToOneField(
        User,
        on_delete=models.CASCADE
    )
    email_id = models.EmailField(max_length=254)


class Journal(models.Model):
    """
    Model to keep journal for each profile
    """
    profile = models.OneToOneField(
        Profile,
        on_delete=models.DO_NOTHING
    )


class Entry(models.Model):
    """
    Model for daily cronological entries
    A new entry is to be made every day
    Each 'daily entry' will contain key value pair of time and entry
    """
    date = models.DateTimeField()
    entries = JSONField(
        help_text="key value pair (time, entry) for each day"
    )
    journal = models.ForeignKey(
        Journal,
        on_delete=models.DO_NOTHING
    )
