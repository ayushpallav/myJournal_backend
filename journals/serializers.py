from rest_framework import serializers

from journals.models import Profile


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
