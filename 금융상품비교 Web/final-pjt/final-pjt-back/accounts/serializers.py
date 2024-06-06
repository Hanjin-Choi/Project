from rest_framework import serializers
from django.contrib.auth import get_user_model
from .models import UserInfo

class UserInfoSerializer(serializers.ModelSerializer):
    class UserSerializer(serializers.ModelSerializer):
        class Meta:
            model = get_user_model()
            fields = ('id', 'username', 'email', 'is_superuser')

    user = UserSerializer(read_only=True)

    class Meta:
        model = UserInfo
        fields = '__all__'
        read_only_fields = ('user',)