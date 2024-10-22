from rest_framework import serializers
from IntegritasTecnica.apps.users.models import User


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'email', 'phone_number', 'type', 'profile_image']
