from datetime import datetime

from rest_framework import serializers

from journals.models import Profile, Entry, Journal


class ProfileSerializer(serializers.ModelSerializer):
    """
    Serializer to return profile details of user
    """
    username = serializers.SerializerMethodField()
    first_name = serializers.SerializerMethodField()
    last_name = serializers.SerializerMethodField()
    email = serializers.SerializerMethodField()

    def get_username(self, obj):
        return obj.user.username

    def get_first_name(self, obj):
        return obj.user.first_name

    def get_last_name(self, obj):
        return obj.user.last_name

    def get_email(self, obj):
        return obj.user.email

    class Meta:
        model = Profile
        fields = "__all__"



class JournalEntrySerializer(serializers.Serializer):
    """
    Serializer to make a new journal entry
    """
    entry = serializers.CharField()

    def create(self, validated_data):
        """
        Make a new journal entry
        
        If a row is present in Entry model for given user and date, add a new entry into the json entry
        as a key value pair {timestamp}:{entry}

        If no row is present for user and date, add a new row and add the json entry
        """
        entry = validated_data['entry']
        username = self.context.get('user')
        datetimestamp = datetime.now()
        profile = Profile.objects.filter(user__username=username).first()
        journal = Journal.objects.filter(profile_id=profile.id).first()
        if not journal:
            journal = Journal.objects.create(profile=profile)
        entry_obj, created = Entry.objects.get_or_create(
            date=str(datetimestamp.date()),
            journal=journal,
        )
        entry = {
            str(datetimestamp.time().strftime("%H:%M")): entry
        }
        entry_obj.add_entry(entry)
        return validated_data
