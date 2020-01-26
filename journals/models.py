"""
Each profile has a unique journal with jourrnal_id assigned to it
Each journal can have multiple entries, hence a one-to-many field from journal to entries
"""
from django.db import models
from django.contrib.auth.models import User

from django.contrib.postgres.fields import JSONField
from django.core.validators import RegexValidator

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
    primary_cell = models.CharField(
        RegexValidator(regex='^.{10}$', message='Length has to be 10', code='nomatch'),
        max_length=10,
    )
    profile_pic = models.ImageField(
        upload_to='profile_pic',
        blank=True
    )

    def __str__(self):
        return self.user.username


class Journal(models.Model):
    """
    Model to keep journal for each profile
    """
    profile = models.OneToOneField(
        Profile,
        on_delete=models.CASCADE
    )


class Entry(models.Model):
    """
    Model for daily cronological entries
    A new entry is to be made every day
    Each 'daily entry' will contain key value pair of time and entry
    """
    date = models.DateField()
    entries = JSONField(
        help_text="key value pair (time, entry) for each day",
        default=dict
    )
    journal = models.ForeignKey(
        Journal,
        on_delete=models.CASCADE
    )

    class Meta:
        unique_together = ('date', 'journal')

    def add_entry(self, entry):
        """Add a new entry"""
        self.entries.update(entry)
        self.save()
