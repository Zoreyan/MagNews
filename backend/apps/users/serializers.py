from rest_framework import serializers
from .models import *


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        exclude = ['user_permissions', 'groups', 'is_active', 'is_staff', 'last_name', 'first_name', 'is_superuser', 'password']
