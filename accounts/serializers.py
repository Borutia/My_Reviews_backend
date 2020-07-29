from accounts.models import User
from rest_framework import serializers


class Registration_serializer(serializers.ModelSerializer):
    class Meta(object):
        model = User
        fields = ('id', 'email', 'username', 'password', 'date_joined')
        extra_kwargs = {
            'password': {
                'write_only': True
            }
        }


class Login_serializer(serializers.ModelSerializer):
    class Meta(object):
        model = User
        fields = ('email', 'password')
